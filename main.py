from nicegui import ui

from traitlets import HasTraits, Int, Unicode, default, Set, List, Any
from traitlets.config import Application

from feelings_and_needs.nycnvc.lists import feelings


class NVC(HasTraits):
    needs = List()
    feeling_types = List("negative positive".split())
    chosen_feelings = Set()
    feeling_phrase = Unicode("feeling")
    sentence = Unicode()

    def store_feeling_phrase(self, p):
        print(f"Storing {p}")
        self.feeling_phrase = p
        self.generate_sentence()

    def add_feeling(self, p):
        print(f"Storing {p}")
        self.chosen_feelings.add(p)
        self.generate_sentence()

    def generate_sentence(self):
        feelings_joined = ", ".join(list(self.chosen_feelings))
        print(f"in gen sen, {self.feeling_phrase=}. {feelings_joined=} ")

        self.sentence = " ".join(["I am ", self.feeling_phrase, " ", feelings_joined])


class MyApp(Application):
    nvc = NVC()
    ui_sentence = Any()

    def model_update(self, f, v):
        f(v)
        self.ui_sentence.set_text(self.nvc.sentence)

    def reset(self):
        self.nvc = NVC()

    def build_ui(self):
        ui.label('I AM')

        feeling_toggle = ui.toggle(
            ["feeling", "guessing you are feeling"],
            value="feeling",
            on_change=lambda e: self.model_update(self.nvc.store_feeling_phrase, e.value)
        )

        selects = list()

        for f in self.nvc.feeling_types:
            with ui.row():
                ui.label(f'{f} Feelings')
                for _ in feelings[f]:
                    print(f"--> Currently working with {_}")
                    with ui.column():
                        ui.label(_[0].upper())
                        selects.append(
                            ui.select(_, on_change=lambda e: self.model_update(self.nvc.add_feeling, e.value))
                        )

        self.ui_sentence = ui.label()

    def start(self):
        self.build_ui()
        ui.run()


if __name__ in {"__main__", "__mp_main__"}:
    MyApp.launch_instance()
