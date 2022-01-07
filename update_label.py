import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#or 
from kivy.core.window import Window
Builder.load_file('update_label.kv')
class MyLayout (Widget):
   def press(self):
     name=self.ids.name.text
     self.ids.text.text=f"Name is {name} !"
     self.ids.name.text=""
     
class KvApp(App):
    def build(self):
        #Window.clearcolor=(0,0,0,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()