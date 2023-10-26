import panel as pn

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

i_am = pn.pane.Markdown("I AM").servable()
feeling_toggle = pn.widgets.RadioButtonGroup(
    name='Radio Button Group', options=['feeling', 'guessing you are feeling'],
    button_type='success').servable()

for f in feelings:
    print(f"FEELING {f}")
    pn_row = pn.Row(f'### {f} feelings:', scroll=False).servable()
    for list_of_feelings in feelings[f]:
        print(f"--> Currently working with {list_of_feelings}")
        card_label = list_of_feelings[0].upper()
        card_select = pn.widgets.MultiSelect(options=list_of_feelings)
        card = pn.Column(f'### {card_label}', card_select)
        pn_row.append(card)

ui_sentence = pn.widgets.TextAreaInput(auto_grow=True).servable()
