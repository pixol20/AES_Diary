import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ChildApp(GridLayout):
    def __init__(self,**kwargs):
        super(ChildApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text="Test1"))
        self.s_name = TextInput()
        


class parentApp(App):
    def build(self):
        return ChildApp()


parentApp().run()
