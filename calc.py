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


    # Clear input and display '0'
    def clear(self):
        self.ids.calc_input.text = '0'


    # Create a button pressing function
    def button_press(self, button):
        # Create a variable that contains expression in the textbox already
        exp = self.ids.calc_input.text
        # Check if operation is ended
        if self.operation_ended == True:
            exp = ''

        # determine if 0 is sitting there
        if exp == '0':
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
            # Change operation state
            self.operation_ended = False
        else:
            self.ids.calc_input.text = f'{exp}{button}'
            # Change the operation state
            self.operation_ended = False


    # Create function to remove last character in textbox
    def remove(self):
        # Remove sign only if operation is not ended
        if self.operation_ended == False:
            exp = self.ids.calc_input.text
            # If there is only one item in the textbox, call clear() function to display '0'
            if len(exp) == 1:
                self.clear()
            else:
                # Remove the last item in the textbox
                exp = exp[:-1]
                # Output back to the textbox
                self.ids.calc_input.text = exp
        else:
            pass


    # Create function to make number positive or negative
    def pos_neg(self):
        exp = ''
        exp = self.ids.calc_input.text

        # Test to see if there's a '-' sign already at the beginning
        if exp[0] == '-':
            exp = exp[1:]
            self.ids.calc_input.text = f'{exp}'
        else:
            self.ids.calc_input.text = f'-{exp}'


    # Create decimal function
    def dot(self):
        exp = self.ids.calc_input.text

        # Get last sign from the operation
        last_sign = exp[-1]

        # Check if last sign is an integer
        try:
            last_sign = int(last_sign)
        except ValueError:
            pass
        
        # Get last number from the operation
        last_num = ''
        for sign in exp[::-1]:
            try:
                sign = int(sign)
            except ValueError:
                pass
    
            if type(sign) == int or sign == '.':
                last_num += str(sign)
            else:
                break

        # Convert from str to correct type
        try:
            if '.' in last_num: 
                last_num = float(last_num[::-1])
            else:
                last_num = int(last_num[::-1])
        except ValueError:
            pass
        
        # If last number is not decimal, allow to add dot
        if type(last_num) is int:
            exp += '.'
        else:
            pass

        self.ids.calc_input.text = exp


    # Create math function
    def math_sign(self, sign):
        exp = self.ids.calc_input.text

        # If dot is in the end, remove it
        if exp[-1] == '.':
            exp = exp[:-1]
        
        # Check if there is a math sign in the end, don't let put another
        if exp[-1] in ['+', '-', '*', '/']:
            pass
        else:
            # Put a math sign to the textbox
            self.ids.calc_input.text = f'{exp}{sign}'


    # Create equals function
    def equals(self):
        exp = self.ids.calc_input.text

        # Error handling
        try:
            # Evaluate the math from the textbox
            answer = eval(exp)
            # Output the answer
            self.ids.calc_input.text = str(round(answer, 6))

            self.operation_ended = True
        except:
            self.display_error()

    # Create power function
    def power(self):
        exp = self.ids.calc_input.text

        # Evaluate power and handle an error
        try:
            power = float(exp)**2
            self.ids.calc_input.text = str(power)
            self.operation_ended = True
        except:
            self.display_error()


    # Create square root function
    def square_root(self):
        exp = self.ids.calc_input.text

        # Evaluate square root and handle an error
        try:
            square = round(math.sqrt(float(exp)), 6)
            self.ids.calc_input.text = str(square)
            self.operation_ended = True
        except:
            self.display_error()


    # Create reciprocal function
    def reciprocal(self):
        exp = self.ids.calc_input.text

        # Evaluate reciprocal and handle an error
        try:
            rec = round(1/float(exp), 6)
            self.ids.calc_input.text = str(rec)
            self.operation_ended = True
        except:
            self.display_error()


    # Create absolute function
    def absolute(self):
        # Evaluate operation
        self.equals()
        exp = self.ids.calc_input.text

        # Check if number is negative and make an absolute
        if exp[0] == '-':
            exp = exp[1:]

        self.ids.calc_input.text = exp


    # Create factorial function
    def factorial(self):
        exp = self.ids.calc_input.text

        # Convert from str to correct type and handle an error
        try:
            exp = int(exp)
        except ValueError:
            try:
                exp = float(exp)
            except ValueError:
                self.display_error()
        
        # Evaluate factorial and handle an error
        fact = 1
        if (type(exp) == int or (type(exp) == float and exp.is_integer())) and exp < 16:
            for i in range(1, int(exp + 1)):
                fact *= i

            self.ids.calc_input.text = str(fact)
            self.operation_ended = True

        else:
            self.display_error()

    # Create function that displays an error
    def display_error(self):
        self.ids.calc_input.text = 'ERR'
        self.operation_ended = True


class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()