import kivy

from kivy.app import App
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        data = Button(text='Hello World',color="white")
        help (data)
        return data


if __name__ == '__main__':
    MyApp().run()
