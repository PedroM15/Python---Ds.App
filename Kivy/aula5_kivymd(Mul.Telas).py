from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen

from kivy.core.window import Window
Window.size = (380, 670)


class Loader(ScreenManager):
    pass


class Home(Screen):
    pass


class Screen1(Screen):
    pass


class Screen2(Screen):
    pass


class MeuApp(MDApp):
    def build(self):
        self.root = Loader()
        return Builder.load_file('tela(exerc5).kv')

    def fechar(self):
        self.stop()


MeuApp().run()
