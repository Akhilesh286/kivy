
import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.core.window import Window
Builder.load_file("animation.kv")
class MyLayout (Widget):
  
  def animate_it(self,widget,*args):
    
    animate= Animation(
      
      background_color=(0,0,1,1),
      duration=2,
      #opacity=0,
      
       )
    animate += Animation(
      size_hint=(1,1)
      )
    animate += Animation(
      size_hint=(.5,.5)
      )
    animate += Animation(
      pos_hint={"center_x":.2}
      )
    animate += Animation(
      pos_hint= {"center_x":.7}
      )
    animate += Animation(
      pos_hint= {"center_x":.5}
      )
    animate.bind(on_complete=self.my_txt)
    animate.start(widget)
  def my_txt(self,*args):
    self.ids.txt.text="wow looks like awesome"
class KvApp(App):
    def build(self):
        #Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()

