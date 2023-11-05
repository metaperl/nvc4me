import panel as pn
from loguru import logger

APP_TITLE = "Help Me NVC!"

feelings = dict()
positive_feelings = list()
negative_feelings = list()

# Below we create a bunch of feelings.
# the positive feelings are a list of lists. and so are the negative ones.
# The first item in each list is the category of that list of feelings.
# E.g. "affection" is the category for all of the feelings in that list of
# positive feelings.

from feelings_and_needs.nycnvc.lists import feelings, needs

_feeling_expr = 'feeling'  # a _feeling_expr is "feeling" or "guessing that you are feeling"
feelings_set = set()  # the feelings set comes from selecting values in the MultiSelect

# needs ownership is based on who is feeling
needs_ownership = {
    'feeling': 'my',
    'guessing you are feeling': 'your'
}

needs_set = set()  # the feelings set comes from selecting values in the MultiSelect

ui_sentence = pn.widgets.TextAreaInput(auto_grow=True, sizing_mode="stretch_width")

pn.pane.Markdown("# Describe the conflict").servable()
pn.widgets.TextAreaInput(auto_grow=True).servable()

i_am = pn.pane.Markdown("### I am").servable()


def grammatical_join(lst):
    if not lst:
        return ""
    elif len(lst) == 1:
        return str(lst[0])
    return "{} and {}".format(", ".join(lst[:-1]), lst[-1])


def build_sentence(feeling_expr, current_feelings, current_needs):
    _ = grammatical_join(current_feelings)
    sentence = "I am " + feeling_expr + " " + _

    needs_expr = needs_ownership[feeling_expr]

    joined_needs = grammatical_join(current_needs)
    sentence += " " + "because " + needs_expr + " " + "needs for " + joined_needs + " " + "are not met."

    print(f"{sentence=}")

    return sentence


def update_ui_sentence():
    _ = build_sentence(_feeling_expr, list(feelings_set), list(needs_set))
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


def clear_all_feelings():
    global feelings_set

    for feeling_tone in feelings:
        for _ in feelings[feeling_tone]:
            for possible_former_feeling in _:
                feelings_set.discard(possible_former_feeling)


def clear_all_needs():
    global needs_set

    for needs_list in needs:
        for possible_former in needs_list:
            needs_set.discard(possible_former)


def clear_related_needs(selected):
    global needs_set
    print("--------- BEGIN clear_related")
    print(f"{needs_set=}")
    for _ in needs:
        for selected_need in selected:
            if selected_need in _:
                for possible_former in _:
                    needs_set.discard(possible_former)
    print(f"After clearing related , {needs_set=}")


def update_feelings_set(selected_feelings):
    global feelings_set
    print(f"current pulldown is providing {selected_feelings=}")

    clear_related_feelings(selected_feelings)

    for _ in selected_feelings:
        feelings_set.add(_)

    print(f"After updating {feelings_set=}")
    print("=============================================")

    update_ui_sentence()


def update_needs_set(selected):
    global needs_set
    print(f"current pulldown is providing {selected}")

    clear_related_needs(selected)

    for _ in selected:
        needs_set.add(_)

    update_ui_sentence()


feeling_toggle = pn.widgets.RadioButtonGroup(
    name='Radio Button Group', options=['feeling', 'guessing you are feeling'],
    button_type='success')

sentence_reactor = pn.bind(update_feeling_expr, feeling_toggle)

pn.Column(feeling_toggle, sentence_reactor).servable()

for f in feelings:
    print(f"FEELING {f}")
    pn_row = pn.FlexBox(f'### {f.capitalize()} Feelings:', scroll=False).servable()
    for list_of_feelings in feelings[f]:
        # print(f"--> Currently working with {list_of_feelings}")
        card_label = list_of_feelings[0].upper()
        card_select = pn.widgets.MultiSelect(options=list_of_feelings)
        multiselect_reactor = pn.bind(update_feelings_set, card_select)
        card = pn.Card(pn.Column(card_select, multiselect_reactor), title=card_label, collapsed=True)
        pn_row.append(card)

pn_row = pn.FlexBox(f'### Needs:', scroll=False).servable()
for need_list in needs:
    # print(f"--> Currently working with {list_of_feelings}")
    card_label = need_list[0].upper()
    card_select = pn.widgets.MultiSelect(options=[word.lower() for word in need_list])
    multiselect_reactor = pn.bind(update_needs_set, card_select)
    card = pn.Card(pn.Column(card_select, multiselect_reactor), title=card_label, collapsed=True)
    pn_row.append(card)

pn.Column('# Here is our current NVC Sentence', ui_sentence).servable(title=APP_TITLE)
