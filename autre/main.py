from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.filemanager import MDFileManager
#import os

Builder.load_file('kivy_f.kv')


class ApplicationMakan(Widget):
    def bonjour(self):
        id_euro = self.ids.euro.text
        id_lbl = self.ids.lbl
        
        try:
            conv = int(id_euro) * 130
        except:
            id_lbl.text = 'Error'
        else:
            id_lbl.text = str(conv)+' Fcfa'
        
    

class TestAppApp(MDApp):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        layout = ApplicationMakan()
        return layout

Insta = TestAppApp()
Insta.run()