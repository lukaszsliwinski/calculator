from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

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

        # Test for error first
        if "Error" in prior or self.operation_ended == True:
            prior = ''

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
            # Change operation state
            self.operation_ended = False
        else:
            self.ids.calc_input.text = f'{prior}{button}'

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

    def power(self):
        prior = self.ids.calc_input.text
        power = float(prior)**2
        self.ids.calc_input.text = str(power)
        self.operation_ended = True


            
    # create addition function
    def math_sign(self, sign):
        # create a variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text
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
            self.ids.calc_input.text = str(round(answer, 11))
            # Change operation state
            self.operation_ended = True
        except:
            self.ids.calc_input.text = "Error"

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()