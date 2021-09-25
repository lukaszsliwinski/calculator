from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)


Builder.load_file('calc.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    # Create a button pressing function
    def button_press(self, button):
        # create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text

        # determine if 0 is sitting there
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'
            
    # create addition function
    def math_sign(self, sign):
        # create a variable that contains whatever was in the text box already
        prior = self.ids.calc_input.text
        # slap a plus sign to the text box
        self.ids.calc_input.text = f'{prior}{sign}'

    # create equals to function
    def equals(self):
        prior = self.ids.calc_input.text

        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            # loop thre our list
            for number in num_list:
                answer = answer + int(number)

            # print the answer in the text box
            self.ids.calc_input.text = str(answer)

    

class CalculatorApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    CalculatorApp().run()