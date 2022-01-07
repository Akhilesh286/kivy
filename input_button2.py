import kivy

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class MyGridLayout (GridLayout):
    def __init__ (self , **kwargs):
        
        super (MyGridLayout, self).__init__(**kwargs)
        self.cols=1
        self.top_grid= GridLayout()
        self.top_grid.cols=2
        self.top_grid.add_widget(Label (text="Name: "))
        self.name=TextInput(multiline=False)
        self.top_grid.add_widget(self.name)
        self.top_grid.add_widget(Label (text="Favorite Pizza: "))
        self.pizza=TextInput(multiline=False)
        self.top_grid.add_widget(self.pizza)
        self.add_widget(self.top_grid)
        self.submit=Button (text="submit")
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    def press (self, instance):
      name = self.name.text
      
      '''
      if name == "akhilesh":
          self.add_widget(Label (text="hello"))
          
      '''
      pizza = self.pizza.text
      self.add_widget(Label (text=f"Name : {name} , {pizza} is pizza "))
      self.name.text=""#"No"
      self.pizza.text=""#"No"
      
      
      
class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
