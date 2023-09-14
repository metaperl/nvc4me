from nicegui import ui

from feelings_and_needs.nycnvc.lists import feelings

needs = list()
chosen_feelings = set()
feeling_phrase = "feeling"

ui.label('I AM')

def store_feeling_phrase(p):
    global feeling_phrase
    print(f"Storing {p}")
    feeling_phrase = p
    generate_sentence()

def add_feeling(p):
    global chosen_feelings
    print(f"Storing {p}")
    chosen_feelings.add(p)
    generate_sentence()

feeling_toggle = ui.toggle(
    ["feeling", "guessing you are feeling"],
    value="feeling",
    on_change=lambda e: store_feeling_phrase(e.value)
)

selects = list()

for f in "negative positive".split():
    with ui.row():
        ui.label(f'{f} Feelings')
        for _ in feelings[f]:
            print(f"--> Currently working with {_}")
            with ui.column():
                ui.label(_[0].upper())
                selects.append(
                    ui.select(_, on_change=lambda e: add_feeling(e.value))
                )



def generate_sentence():
    global feeling_phrase
    feelings_joined = ", ".join(list(chosen_feelings))
    print(f"in gen sen, {feeling_phrase=}. {feelings_joined=} ")

    sentence = ["I am ", feeling_phrase, " ", feelings_joined]
    nvc_sentence.set_text(sentence)

nvc_sentence = ui.label()
ui.run()
