
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.core.window import Window
Builder.load_file("tab.kv")
class MyLayout (TabbedPanel):
   pass
class KvApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()

