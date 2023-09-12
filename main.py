from nicegui import ui

from feelings_and_needs.nycnvc.lists import positive_feelings, negative_feelings

needs = list()
feelings = list()
feeling_phrase = "feeling"

ui.label('I AM')

def store_feeling_phrase(p):
    global feeling_phrase
    print(f"Storing {p}")
    feeling_phrase = p
    generate_sentence()

def add_feeling(p):
    global feelings
    print(f"Storing {p}")
    feelings.append(p)
    generate_sentence()

feeling_toggle = ui.toggle(
    ["feeling", "guessing you are feeling"],
    value="feeling",
    on_change=lambda e: store_feeling_phrase(e.value)
)

selects = list()

with ui.row():
    ui.label('Positive Feelings')
    for _ in positive_feelings:
        print(f"--> Currently working with {_}")
        selects.append(
            ui.select(_, value=_[0], on_change=lambda e: add_feeling(e.value))
        )

with ui.row():
    ui.label('Negative Feelings')
    for _ in negative_feelings:
        print(f"--> Currently working with {_}")
        selects.append(
            ui.select(_, value=_[0], on_change=lambda e: add_feeling(e.value))
        )

def generate_sentence():
    global feeling_phrase
    feelings_joined = ",".join(feelings)
    print(f"in gen sen, {feeling_phrase=}. {feelings_joined=} ")

    sentence = ["I am ", feeling_phrase, feelings_joined]
    nvc_sentence.set_text(sentence)

nvc_sentence = ui.label()
ui.run()
