from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivy.uix import widget

class AESDiary(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        test = Builder.load_file("main.kv")
        return test
    def callback(self):
        print("memes")


AESDiary().run()
