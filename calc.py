from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

import math

Window.size = (500,700)


Builder.load_file('calc.kv')

class MyLayout(Widget):
    # Operation state
    operation_ended = True

    def clear(self):
        self.ids.calc_input.text = "0"

    # Create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text
        # Check if operation is ended
        if self.operation_ended == True:
            prior = ''

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
            # Change operation state
            self.operation_ended = False
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            self.operation_ended = False

    # Create function to remove last character in textbox
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last item in the textbox
        prior = prior[:-1]
        # Output back to the textbox
        self.ids.calc_input.text = prior

    # Create function to make textbox positive or negative
    def pos_neg(self):
        prior = ''
        prior = self.ids.calc_input.text

        # Test to see if there's a - sign already at the beginning
        if prior[0] == "-":
            prior = prior[1:]
            self.ids.calc_input.text = f'{prior}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        # Split our textbox by +
        num_list = prior.split("+")

        if "+" or "-" or "*" or "/" in prior and "." not in num_list[-1]:
            # Add a decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the textbox
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            # Add a decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the textbox
            self.ids.calc_input.text = prior



    # create addition function
    def math_sign(self, sign):
        # create a variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text

        # self.check_state()
        
        # slap a plus sign to the textbox
        self.ids.calc_input.text = f'{prior}{sign}'
        # Change operation state
        self.operation_ended = False

    # create equals to function
    def equals(self):
        prior = self.ids.calc_input.text
        # Error handling
        try:
            # Evaluate the math from the textbox
            answer = eval(prior)
            # Output the answer
            self.ids.calc_input.text = str(round(answer, 6))
            # Change operation state
            self.operation_ended = True
        except:
            self.display_error()


    def power(self):
        prior = self.ids.calc_input.text
        try:
            power = float(prior)**2
            self.ids.calc_input.text = str(power)
            self.operation_ended = True
        except:
            self.display_error()

    def square_root(self):
        prior = self.ids.calc_input.text
        try:
            square = round(math.sqrt(float(prior)), 6)
            self.ids.calc_input.text = str(square)
            self.operation_ended = True
        except:
            self.display_error()
    
    def display_error(self):
        self.ids.calc_input.text = "ERR"
        self.operation_ended = True




class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()