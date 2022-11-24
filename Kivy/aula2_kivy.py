import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.core.window import Window
Window.size = (380, 670)

from kivy.app import App
from kivy.lang import Builder

abc = '''
FloatLayout:
    Label:
        id: rotulo1
        text: "Titulo do futuro projeto: "
        pos_hint: {'center_x':.5, 'center_y': .9}
        color: 5, 2, .9, 1

    Label:
        id: rotulo2
        text: "Insira o seu e-mail: "
        pos_hint: {'center_x':.23, 'center_y': .77}
        color: 5, 2, .9, 1
    Label:
        id: rotulo3
        text: "Insira a sua senha: "
        pos_hint: {'center_x':.23, 'center_y': .6}
        color: 5, 2, .9, 1
        
    TextInput:
        id: caixa1
        text:
        size_hint: .9, .08
        pos_hint: {'center_x':.5, 'center_y': .53}
    
    TextInput:
        id: caixa2
        text:
        size_hint: .9, .08
        pos_hint: {'center_x':.5, 'center_y': .7}
    
    Button:
        id: boton1
        text: 'Olá Mundo!'
        size_hint: .9, .08
        pos_hint: {'center_x':.5, 'center_y': .2}
        on_press: app.muda_texto()
        
    Button:
        id: boton2
        text: 'Limpar as caixas'
        size_hint: .4, .04
        pos_hint: {'center_x':.5, 'center_y': .1}
        on_press: app.limpa_texto()
'''


class MainApp(App):
    def build(self):
        return Builder.load_string(abc)

    def muda_texto(self):
        self.root.ids.caixa1.text = self.root.ids.rotulo1.text

    def limpa_texto(self):
        self.root.ids.caixa1.text = " "
        self.root.ids.rotulo1.tex = " Text clear "

MainApp().run()
