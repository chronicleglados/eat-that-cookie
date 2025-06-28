from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class TapApp(App):
    def build(self):
        # Create a layout to hold everything
        self.layout = BoxLayout(orientation='vertical')

        # Create a Label to show the score
        self.count = 0
        self.label = Label(text="Chomps: 0", font_size=40)

        # Create a Button
        self.button = Button(text="Eat The Cookie!", font_size=40)
        self.button.bind(on_press=self.on_button_press)

        # Add the Label and Button to the layout
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)

        return self.layout

    # This is the callback
    def on_button_press(self, instance):
        self.count += 1
        self.label.text = f"Chomps: {self.count}"

# Start the app
if __name__ == "__main__":
    TapApp().run()

            