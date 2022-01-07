import kivy
from kivy.app import App
from kivy.uix.button import Button
#from kivy.uix import *
from kivy.uix.label import Label





class MyApp(App):
    def build(self):
        data = Label (
        text='Hello World'
)

        return data


if __name__ == '__main__':
    MyApp().run()
