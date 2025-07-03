from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class GameState:
    def __init__(self):
        self.cookies = 0
        self.tap_power = 1

    def tap(self):
        self.cookies += self.tap_power

    def upgrade(self):
        if self.cookies >= 10:
            self.cookies -= 10
            self.tap_power += 1


class TapAppException(Exception):
    """
        This is our general exception class
    """


class TapApp(App):
    current_game = None
    def build(self):
        self.current_game = GameState()
        # Create a layout to hold everything
        self.layout = BoxLayout(orientation='vertical')

        # Create a Label to show the score
        self.label = Label(text=f"Chomps: {self.current_game.cookies}", font_size=40)

        # Create a Button
        self.button = Button(text="Eat The Cookie!", font_size=40)
        self.button.bind(on_press=self.on_button_press)

        # Add the Label and Button to the layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)

        return self.layout

    # This is the callback
    def on_button_press(self, instance):
        if self.current_game is None:
            raise TapAppException("This game has not yet been built!")
        
        self.current_game.tap()
        self.label.text = f"Cookies: {self.current_game.cookies}"
