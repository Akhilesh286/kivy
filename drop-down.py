
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#or
from kivy.core.window import Window
Builder.load_file("drop-down.kv")
class MyLayout (Widget):
   def spinner_click (self , value):
     self.ids.txt.text=f"you selected {value} pizza 🍕🍕"
class KvApp(App):
    def build(self):
       # Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()

