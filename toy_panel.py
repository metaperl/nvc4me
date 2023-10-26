import panel as pn
from loguru import logger

feelings = dict()
positive_feelings = list()
negative_feelings = list()

# Below we create a bunch of feelings.
# the positive feelings are a list of lists. and so are the negative ones.
# The first item in each list is the category of that list of feelings.
# E.g. "affection" is the category for all of the feelings in that list of
# positive feelings.

positive_feelings.append("""affectionate
compassionate
fond
loving
openhearted
tender
warm""".split())

positive_feelings.append("""engaged
absorbed
curious
engrossed
enchanted
enthralled
entranced
fascinated
interested
intrigued
involved
open
spellbound
stimulated""".split())

negative_feelings.append("""anger
aggravated
angry
animosity
annoyed
contempt
disgruntled
enraged
exasperated
furious 
hate 
hostile
incensed
irate
irritated
irked
livid
miffed
nettled
outraged
peeved
resentful""".split())

negative_feelings.append("""aversion
abhorrence
appalled
bothered displeased
disgust
dislike 
enmity
horrified
loathing
repulsion
revulsion""".split())

feelings['positive'] = positive_feelings
feelings['negative'] = negative_feelings

_feeling_expr = 'feeling'  # a _feeling_expr is "feeling" or "guessing that you are feeling"
feelings_set = set()  # the feelings set comes from selecting values in the MultiSelect

ui_sentence = pn.widgets.TextAreaInput(auto_grow=True)

pn.pane.Markdown("# Let's Build an NVC Sentence")

i_am = pn.pane.Markdown("### I am").servable()


def build_sentence(feeling_expr, feeling_words):
    _ = ', '.join(feeling_words)
    sentence = "I am " + feeling_expr + " " + _
    return sentence


def update_ui_sentence():
    _ = build_sentence(_feeling_expr, list(feelings_set))
    ui_sentence.value = _


def update_feeling_expr(feeling_subject):
    global _feeling_expr
    _feeling_expr = feeling_subject
    print(f"feeling expr {_feeling_expr}")
    update_ui_sentence()


def clear_related_feelings(selected_feelings):
    global feelings_set
    print("--------- BEGIN clear_related_feelings")
    print(f"{feelings_set=}")
    for feeling_tone in feelings:
        for _ in feelings[feeling_tone]:
            for selected_feeling in selected_feelings:
                if selected_feeling in _:
                    for possible_former_feeling in _:
                        feelings_set.discard(possible_former_feeling)
    print(f"After clearing related feelings, {feelings_set=}")
    print("--------- END clear_related_feelings")


def update_feelings_set(selected_feelings):
    global feelings_set
    print(f"current pulldown is providing {selected_feelings=}")

    clear_related_feelings(selected_feelings)

    for _ in selected_feelings:
        feelings_set.add(_)

    print(f"After updating {feelings_set=}")
    print(f"After updating {feelings_set_history=}")
    print("=============================================")

    update_ui_sentence()


feeling_toggle = pn.widgets.RadioButtonGroup(
    name='Radio Button Group', options=['feeling', 'guessing you are feeling'],
    button_type='success')

sentence_reactor = pn.bind(update_feeling_expr, feeling_toggle)

pn.Column(feeling_toggle, sentence_reactor).servable()

for f in feelings:
    print(f"FEELING {f}")
    pn_row = pn.Row(f'### {f} feelings:', scroll=False).servable()
    for list_of_feelings in feelings[f]:
        # print(f"--> Currently working with {list_of_feelings}")
        card_label = list_of_feelings[0].upper()
        card_select = pn.widgets.MultiSelect(options=list_of_feelings)
        multiselect_reactor = pn.bind(update_feelings_set, card_select)
        card = pn.Card(pn.Column(card_select, multiselect_reactor), title=card_label, collapsed=True)
        pn_row.append(card)

pn.Column('# Here is our current NVC Sentence', ui_sentence).servable()
