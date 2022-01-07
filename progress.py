
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#or
from kivy.core.window import Window
Builder.load_file("progress.kv")
class MyLayout (Widget):
  def press(self):
    count=self.ids.bar.value
    if count==1:
      count=0
    count+=.25
    self.ids.bar.value=count
    self.ids.txt.text=str(count)
class KvApp(App):
    def build(self):
        #Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()

