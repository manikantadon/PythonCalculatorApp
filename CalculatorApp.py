import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class Layout(BoxLayout):
    def __init__(self, **kwargs):
        super(Layout, self).__init__(**kwargs)
        self.orientation = 'vertical'
        
        # Display area for input and result with placeholder
        self.display = TextInput(multiline=False, readonly=False, halign="right", font_size=55, hint_text="Please enter input")
        self.display.bind(on_text_validate=self.on_enter)
        self.add_widget(self.display)
        
        # Grid layout for the buttons
        self.buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['.', '0', '=', '+'],
            ['Clear']
        ]
        
        button_grid = GridLayout(cols=4)
        for row in self.buttons:
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                button.bind(on_press=self.on_button_press)
                button_grid.add_widget(button)
        
        self.add_widget(button_grid)

    def on_button_press(self, instance):
        current = self.display.text
        button_text = instance.text
        
        if button_text == '=':
            try:
                # Evaluate the expression and display the result
                self.display.text = str(eval(current))
            except Exception as e:
                self.display.text = 'Error'
        elif button_text == 'Clear':
            # Clear the display
            self.display.text = ''
        else:
            # Update the display with the pressed button text
            self.display.text += button_text

    def on_enter(self, instance):
        if instance.text:
            instance.hint_text = ''

class Calculator(App):
    def build(self):
        return Layout()

if __name__ == "__main__":
    Calculator().run()
