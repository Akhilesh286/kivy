
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#or
from kivy.core.window import Window
Builder.load_file("check.kv")
class MyLayout(Widget):
  check=[]
  def check_click (self,instance,value,pizza):
    
    if value == True:
      MyLayout.check.append(pizza)
      top=""
      for i in MyLayout.check:
        top=f'{top}  {i}'
      self.ids.txt.text=f"You selected {top} !"
    else:
      MyLayout.check.remove(pizza)
      top=""
      for i in MyLayout.check:
        top=f'{top}  {i}'
      self.ids.txt.text=f"You selected {top} !"
class KvApp(App):
    def build(self):
        #Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()

