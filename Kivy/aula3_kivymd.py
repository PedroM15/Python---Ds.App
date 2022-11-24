from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.core.window import Window
Window.size = (380, 670)

kvy = '''
MDFloatLayout:
    
    MDLabel:
        id: rotulo
        text: "Ta vendo a caixa abaixo? Escreve algo nela."
        pos_hint: {'center_x':.6, 'center_y': .7}
        theme_text_color: "Custom"
        text_color: "blue"
        font_style: "Subtitle1"
        
    MDTextField:
        id: caixa
        text: 
        hint_text: "Escreva algo."
        mode: "rectangle"
        pos_hint: {'center_x':.5, 'center_y': .6}
        size_hint: .75, .09
        hint_text_color_focus: "blue"
        
    MDRaisedButton:
        id: boton
        text: "Eu sou um botão me pressione!"
        md_bg_color: "blue"
        size_hint: .65, .08
        pos_hint: {'center_x':.5, 'center_y': .4}
        on_press: app.muda_texto()
'''


class Example(MDApp):
    def build(self):
        return Builder.load_string(kvy)

    def muda_texto(self):
        if self.root.ids.caixa.text != " ":
            self.root.ids.rotulo.text = self.root.ids.caixa.text
            self.root.ids.caixa.text = " "
        else:
            self.root.ids.rotulo.text = "Ta vendo a caixa abaixo? Escreve algo nela."


Example().run()
