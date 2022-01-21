from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window

import math

Window.size = (500,700)


Builder.load_file('calc.kv')

class MyLayout(Widget):
    # Operation state
    operation_ended = False
    dot_included = False

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
        # Remove sign only operation is not ended
        if self.operation_ended == False:
            prior = self.ids.calc_input.text
            # If there is only one item in the textbox, call clear() function to display '0'
            if len(prior) == 1:
                self.clear()
            else:
                # Remove the last item in the textbox
                prior = prior[:-1]
                # Output back to the textbox
                self.ids.calc_input.text = prior
        else:
            pass

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

        last_sign = prior[-1]

        try:
            last_sign = int(last_sign)
        except ValueError:
            pass
        
        last_num = ''
        for sign in prior[::-1]:
            try:
                sign = int(sign)
            except ValueError:
                pass
    
            if type(sign) == int or sign == '.':
                last_num += str(sign)
            else:
                break

        try:
            if '.' in last_num: 
                last_num = float(last_num[::-1])
            else:
                last_num = int(last_num[::-1])
        except ValueError:
            pass
        
        if type(last_num) is int:
            prior += "."
        else:
            pass

        self.ids.calc_input.text = prior

    # create addition function
    def math_sign(self, sign):
        # create a variable that contains whatever was in the textbox already
        prior = self.ids.calc_input.text

        # if dot is in the end, remove it
        if prior[-1] == '.':
            prior = prior[:-1]

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

    def reciprocal(self):
        prior = self.ids.calc_input.text
        try:
            rec = round(1/float(prior), 6)
            self.ids.calc_input.text = str(rec)
            self.operation_ended = True
        except:
            self.display_error()

    def absolute(self):
        self.equals()
        prior = self.ids.calc_input.text

        if prior[0] == '-':
            prior = prior[1:]

        self.ids.calc_input.text = prior
        
    
    def display_error(self):
        self.ids.calc_input.text = "ERR"
        self.operation_ended = True


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()