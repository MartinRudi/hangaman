from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.vkeyboard import VKeyboard
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label
from functools import partial

from hangman import HangmanGame


class MainScreen(Widget):
    pass


class KeyboardScreen(Screen):
    """
    Screen containing all the available keyboard layouts. Clicking the buttons
    switches to these layouts.
    """
    displayLabel = ObjectProperty()
    kbContainer = ObjectProperty()
    game: HangmanGame

    def __init__(self, **kwargs):
        super(KeyboardScreen, self).__init__(**kwargs)
        self.game = HangmanGame()
        self.create_word_blocks()
        self._keyboard = None
        layouts = list(VKeyboard().available_layouts.keys())
        layouts.append("layout.json")
        self.prepare_keyboard()

    def create_word_blocks(self):
        """ Add a buttons for each available keyboard layout. When clicked,
        the buttons will change the keyboard layout to the one selected. """
        # self.kbContainer = ObjectProperty()
        self.kbContainer.clear_widgets()
        letters = self.game.letters if not self.game.is_finished(
        ) else self.game.chosen

        for key in self.game.chosen:
            if key not in letters:
                key = '   '
            self.kbContainer.add_widget(
                Label(
                    text=key, bold=True, font_size=36, underline=True))

    def say_hello(self):
        self.game = HangmanGame()
        self.create_word_blocks()

    def prepare_keyboard(self):
        """ Change the keyboard layout to the one specified by *layout*. """
        kb = Window.request_keyboard(
            self._keyboard_close, self)
        if kb.widget:
            # If the current configuration supports Virtual Keyboards, this
            # widget will be a kivy.uix.vkeyboard.VKeyboard instance.
            self._keyboard = kb.widget
            self._keyboard.layout = 'layout.json'
        else:
            self._keyboard = kb

        self._keyboard.bind(
            # on_key_down=self.key_down,
            on_key_up=self.key_up)

    def _keyboard_close(self, *args):
        """ The active keyboard is being closed. """
        if self._keyboard:
            # self._keyboard.unbind(on_key_down=self.key_down)
            self._keyboard.unbind(on_key_up=self.key_up)
            self._keyboard = None

    # def key_down(self, keyboard, keycode, text, modifiers):
    #     """ The callback function that catches keyboard events. """
    #     self.displayLabel.text = u"Key pressed - {0}".format(text)

    # def key_up(self, keyboard, keycode):
    def key_up(self, keyboard, keycode, text, *args):
        """ The callback function that catches keyboard events. """
        # system keyboard keycode: (122, 'z')
        # dock keyboard keycode: 'z'
        # if isinstance(keycode, tuple):
        #     keycode = keycode[1]
        if text not in self.game.letters:
            self.game.game_round(text)
            if not self.game.is_finished():
                result = '[b]Tries left: {}, letters used: {}[/b]'.format(
                    self.game.tries, ', '.join(
                        self.game.letters))
            elif self.game.is_win():
                result = 'Win!!!!'
            else:
                result = 'Lose :('

        self.displayLabel.text = result

        self.create_word_blocks()


class UIApp(MDApp):
    sm = ObjectProperty()  # The root screen manager
    # game: HangmanGame

    def build(self):
        # self.game = HangmanGame()

        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        self.sm = ScreenManager()
        self.sm.add_widget(KeyboardScreen(name="keyboard"))
        self.sm.current = "keyboard"

        return self.sm


if __name__ == '__main__':
    UIApp().run()
