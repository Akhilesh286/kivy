
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#or
from kivy.core.window import Window
Builder.load_file('slider.kv')
class MyLayout (Widget):
   def slider_it(self ,*args):
     #print (args[1])
     self.label_txt.text=str(int(args[1]))
     self.label_txt.font_size=str(int (args[1] *10))
class KvApp(App):
    def build(self):
        #Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()

