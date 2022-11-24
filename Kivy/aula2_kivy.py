import kivy 
'''kivy.require('2.1.0') # replace with your current kivy version !'''
from kivy.lang import Builder
from kivymd.app import App

from kivy.core.window import Window

Window.size = (380, 670)

abc = '''
FloatLayout:
    canvas.before:
        Color: 
            rgba: .5, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Label:
        id: rotulo
        text: "Ta vendo a caixa abaixo? Escreve algo nela."
        pos_hint: {'center_x':.5, 'center_y': .7}
        color: 5, 2, .9, 1

    TextInput:
        id: caixa
        text: " "
        size_hint: .87, .08
        pos_hint: {'center_x':.5, 'center_y': .6}
        
    Button:
        id: boton
        text: 'Eu sou um botão me pressione!'
        size_hint: .65, .08
        pos_hint: {'center_x':.5, 'center_y': .4}
        on_press: app.muda_texto()
'''


class MainApp(App):
    def build(self):
        return Builder.load_string(abc)

    def muda_texto(self):
        if self.root.ids.caixa.text == " ":
            self.root.ids.rotulo.text = "Ta vendo a caixa abaixo? Escreve algo nela."
        else:
            self.root.ids.rotulo.text = self.root.ids.caixa.text
            self.root.ids.caixa.text = " "


'''          
 if self.root.ids.caixa.text != " ":
            self.root.ids.rotulo.text = self.root.ids.caixa.text
            self.root.ids.caixa.text = " "
        else:
            self.root.ids.rotulo.text = "Escreva algo na caixa abaixo !"
'''

MainApp().run()
