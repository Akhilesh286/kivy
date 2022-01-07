import kivy

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
#or 
from kivy.core.window import Window
#Window.size=(500,700)
Builder.load_file('calculator.kv')
class MyLayout (Widget):
  def clear(self):
    self.ids.inp.text=""
  def but_press(self, button):
    prior = self.ids.inp.text
    if "Error" in prior:
      prior=''
    if prior=="0":
      self.ids.inp.text=""
      self.ids.inp.text= f'{button}'
    else:
      self.ids.inp.text=f'{prior}{button}'
  def pos_neg (self):
    prior=self.ids.inp.text
    if prior[0] == "-":
      self.ids.inp.text=f'{prior.replace("-","")}'
    else :
      self.ids.inp.text=f"-{prior}"
      
      
    
  
  def remove (self):
    prior=self.ids.inp.text
    prior=prior[:-1]
    self.ids.inp.text=str(prior)
  def maths_sing (self,sing):
    prior = self.ids.inp.text
    self.ids.inp.text=f"{prior}{sing}"
  def dot (self):
    
    prior = self.ids.inp.text
    num_list = prior.split("+")
    if "+" in prior and "." not in num_list[-1]:
      self.ids.inp.text=f"{prior}."
      
    elif "." in prior:
      pass
    else:
      self.ids.inp.text=f"{prior}."
    
  
  def equals (self):
    prior = self.ids.inp.text
    try :
      answer = eval(prior)
      self.ids.inp.text= str (answer)
    except:
      self.ids.inp.text="Error"
      


class KvApp(App):
    def build(self):
        Window.clearcolor=(1,1,1,1)
        return MyLayout()


if __name__ == '__main__':
    KvApp().run()