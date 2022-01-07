import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
class MyGridLayout (Widget):
    name=ObjectProperty(None)
    color=ObjectProperty(None)
    def press (self):
      name = self.name.text
      color = self.color.text
      #self.add_widget(Label (text=f"Name : {name} , {pizza} is pizza "))
      print (f"name :{name} color: {color}")
      self.name.text=""#"No"
      self.color.text=""#"No"
      
      
      
class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
