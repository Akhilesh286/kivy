import kivy
from kivy.app import App
from kivy.uix.button import *
from kivy import *
from kivy.uix.label import *
from kivy import uix as uix
but = uix.button.Button
p = uix.label.Label
class MyApp(App):
    def build(self):
        return p(text='Hello World')


if __name__ == '__main__':
    MyApp().run()
