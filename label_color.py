import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
Builder.load_file('lcolor.kv')
class MyLayout (Widget):
   pass
class KvApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()