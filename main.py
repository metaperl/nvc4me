from nicegui import ui

needs = list()
feeling_phrase = 'x'

ui.label('I AM')

def store_feeling_phrase(p):
    global feeling_phrase
    print(f"Storing {p}")
    feeling_phrase = p
    generate_sentence()


feeling_toggle = ui.toggle(
    ["feeling", "guessing you are feeling"],
    value="feeling",
    on_change=lambda e: store_feeling_phrase(e.value)
)



feelings_select = ui.select(feelings, value=feelings[0])

def generate_sentence():
    global feeling_phrase
    print(f"in gen sen, feeling phrase = {feeling_phrase}")
    sentence = ["I am ", feeling_phrase]
    nvc_sentence.set_text(sentence)

nvc_sentence = ui.label()
print("can you add a print message before the ui.run()? I just want to be sure you are running things that you think you are running...")
ui.run()
