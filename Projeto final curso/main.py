from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.bottomsheet import MDGridBottomSheet

from kivy.core.window import Window

Window.size = (380, 670)


class Loader(ScreenManager):
    pass


class Home(Screen):
    pass


class Screen1(Screen):
    pass


class Screen2(Screen):
    def sintomas(self):
        menu_inferior = MDGridBottomSheet()
        menu_inferior.add_item(
            text="Inflamações",
            callback=lambda x: self.infla(),
            icon_src="image/inflamacao.png"
        )
        menu_inferior.add_item(
            text="Insônia",
            callback=lambda x: self.insonia(),
            icon_src="image/insonia.png"
        )
        menu_inferior.add_item(
            text="Dor de cabeça",
            callback=lambda x: self.dor_cabeca(),
            icon_src="image/dor-de-cabeca.png"
        )

        menu_inferior.open()

    def infla(self):
        self.ids.title1.text = "Chá recomendado:1 - Camomila"
        self.ids.title2.text = "Chá recomendado:2 - Erva Doce"
        self.ids.title3.text = "Chá recomendado:3 - Chá Verde"

        self.ids.desc1.text = "Contém compostos fenólicos além de óleos essenciais. Tem funções ansiolíticas " \
                              "indutoras do sono, anti-inflamatórias e antioxidantes. "
        self.ids.desc2.text = "Contém ácido málico, ácido fólico, niacina, riboflavina, tiamina, entre outros. Ação " \
                              "na redução de inchaços e gases e melhora a digestão. "
        self.ids.desc3.text = "Contém flavonoides e minerais como manganês, potássio, ácido fólico e as vitaminas C, " \
                              "K, B1 e B2. Possui ação anti-envelhecimento e é um coadjuvante insulínico. "

        self.ids.cha1.source = 'tea/CAMOMILA.png'
        self.ids.cha2.source = 'tea/ERVA_DOCE.png'
        self.ids.cha3.source = 'tea/CHA_VERDE.png'

    def dor_cabeca(self):
        self.ids.title1.text = "Chá recomendado:1 - Camomila"
        self.ids.title2.text = "Chá recomendado:2 - Erva Cidreira"
        self.ids.title3.text = "Chá recomendado:3 - Limão"

        self.ids.desc1.text = "Contém compostos fenólicos além de óleos essenciais. Tem funções ansiolíticas " \
                              "indutoras do sono, anti-inflamatórias e antioxidantes. "
        self.ids.desc2.text = "Contém tanino, resina, citral, terpenos. Ação contra asma, " \
                              "excesso de gases, náuseas e tem efeito analgésico."
        self.ids.desc3.text = "Contém ácido fólico, fósforo, potássio, hesperidina e ácido cítrico." \
                              " Tem ação diurética, coadjuvante insulínico e antiinflamatório."

        self.ids.cha1.source = 'tea/CAMOMILA.png'
        self.ids.cha2.source = 'tea/ERVA_CIDREIRA.png'
        self.ids.cha3.source = 'tea/LIMAO.png'

    def insonia(self):
        self.ids.title1.text = "Chá recomendado:1 - Camomila"
        self.ids.title2.text = "Chá recomendado:2 - Erva Cidreira"
        self.ids.title3.text = "Chá recomendado:3 - Limão"

        self.ids.desc1.text = "Contém compostos fenólicos além de óleos essenciais. Tem funções ansiolíticas " \
                              "indutoras do sono, anti-inflamatórias e antioxidantes. "
        self.ids.desc2.text = "Contém tanino, resina, citral, terpenos. Ação contra asma, " \
                              "excesso de gases, náuseas e tem efeito analgésico."
        self.ids.desc3.text = "Contém antioxidantes como vitamina C, betacarotenos, flavonoides. " \
                              "Possui ação sedativa, antiinflamatória, depurativa, vermífuga, analgésica " \
                              "e coadjuvante insulínico."

        self.ids.cha1.source = 'tea/CAMOMILA.png'
        self.ids.cha2.source = 'tea/ERVA_CIDREIRA.png'
        self.ids.cha3.source = 'tea/FOLHA_DE_MARACUJA.png'


class MeuApp(MDApp):
    def build(self):
        self.root = Loader()
        self.theme_cls.primary_palette = 'Gray'
        return Builder.load_file('style.kv')

    def fechar(self):
        self.stop()


MeuApp().run()
