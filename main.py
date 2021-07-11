from kivy.app import App
from kivy.core.window import Window 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.widget import Widget
# from kivy.properties import ObjectProperty
# import sqlite3
                  
class ScreenManagement(ScreenManager):
    pass

class HomeScreen(Screen):
    pass
    
class EuroScreen(Screen):
    def get_f(self):
        try:
            my_textinput = self.ids.entry.text
            my_label = self.ids.lbl
            conv = int(my_textinput) * 650
            my_label.text = str(conv) + " Fcfa"
        except ValueError:
            my_label = self.ids.lbl
            my_label.text = "Error"

class FcfaScreen(Screen):
    def get_e(self):
        try:
            my_textinput = self.ids.fcfa.text
            my_label = self.ids.fcfalbl
            conv = int(my_textinput) / 650
            integer = int(conv)
            my_label.text = str(integer) + " Euro"
        except ValueError:
            my_label = self.ids.fcfalbl
            my_label.text = "Error"

class FcfaxoaScreen(Screen):
    def get_xoa(self):
        try:
            my_textinput = self.ids.xoainput.text
            my_label = self.ids.xoalbl
            conv = int(my_textinput) / 5
            integer = int(conv)
            my_label.text = str(integer) + " Entier"
        except ValueError:
            my_label = self.ids.xoalbl
            my_label.text = "Error"

class FcfaentierScreen(Screen):
    def get_entier(self):
        try:
            my_textinput = self.ids.entierinput.text
            my_label = self.ids.entierlbl
            conv = int(my_textinput) / 130
            integer = int(conv)
            my_label.text = str(integer) + " Euro"
        except ValueError:
            my_label = self.ids.entierlbl
            my_label.text = "Error"

kv = Builder.load_file('mdapp.kv')
    
class MDApp(App):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        layout = kv
        return layout
    
if __name__ == '__main__':
    Inst = MDApp()
    Inst.run()