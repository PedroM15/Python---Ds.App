from kivy.lang import Builder
from kivymd.app import MDApp

from kivy.core.window import Window

Window.size = (380, 670)


class Menu(MDApp):
    def build(self):
        return Builder.load_file('tela.kv')

    def Conta(self):
        imc = float(self.root.ids.peso.text) / (float(self.root.ids.alt.text)) ** 2

        if imc <= 18.5:
            self.root.ids.l1.text = f"Voce esta abaixo do peso: {imc}"
            self.root.ids.peso.text = ""
            self.root.ids.alt.text = ""
        else:
            if (imc >= 18.5) and (imc <= 25):
                self.root.ids.l1.text = f"Seu peso esta normal: {imc}"
                self.root.ids.peso.text = ""
                self.root.ids.alt.text = ""
            else:
                if (imc >= 25) and (imc <= 30):
                    self.root.ids.l1.text = f"Voce esta acima do peso: {imc}"
                    self.root.ids.peso.text = ""
                    self.root.ids.alt.text = ""
                else:
                    if imc > 30:
                        self.root.ids.l1.text = f"Voce esta obeso: {imc}"
                        self.root.ids.peso.text = ""
                        self.root.ids.alt.text = ""

    def fechar(self):
        self.stop()

    def rst(self):
        self.root.ids.l1.text = "IMMC"
        self.root.ids.peso.text = ""
        self.root.ids.alt.text = ""
        self.root.ids.bt1.text = "Calcule seu immc"


Menu().run()
