import panel as pn

from traitlets import HasTraits, Int, Unicode, default, Set, List, Any
from traitlets.config import Application

from feelings_and_needs.nycnvc.lists import feelings

from loguru import logger


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


class UI(HasTraits):
    card = Any()
    ui_sentence = Any()
    controller = Any()

    def model_update(self, f, v):
        f(v)
        self.ui_sentence.set_text(self.controller.nvc.sentence)

    def reset(self):
        self.card.clear()
        self.controller.start()

    def build(self):

        i_am = pn.pane.Markdown("I AM").servable()
        feeling_toggle = pn.widgets.RadioButtonGroup(
            name='Radio Button Group', options=['feeling', 'guessing you are feeling'],
            button_type='success').servable()

        for f in self.controller.nvc.feeling_types:
            logger.debug(f"FEELING {f}")
            pn_row = pn.FlexBox(f'### {f} feelings:', scroll=False).servable()
            for list_of_feelings in feelings[f]:
                print(f"--> Currently working with {list_of_feelings}")
                card_label = list_of_feelings[0].upper()
                card_select = pn.widgets.Select(options=list_of_feelings)
                card = pn.Column(f'### {card_label}', card_select)
                pn_row.append(card)

        self.ui_sentence = pn.widgets.TextAreaInput(auto_grow=True).servable()


class MyApp(Application):
    nvc = NVC()
    ui = UI()

    def start(self):
        logger.debug("1")
        self.nvc = NVC()

        logger.debug("1")
        self.ui = UI()

        logger.debug("1")
        self.ui.controller = self

        logger.debug("1")
        self.ui.build()


logger.info("in main")
# MyApp.launch_instance()

app = MyApp()
app.start()
