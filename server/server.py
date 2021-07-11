from kivymd.app import MDApp
from kivy.core.window import Window 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.widget import Widget

import socket

ip, port = socket.gethostbyname(socket.gethostname()), 6919
socket_s = ip, port
conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conn.bind(socket_s)
conn.listen(5)

class ScreenManagement(ScreenManager):
    pass


class Socket(Screen):
    def connexion(self):
        pass
        
class ValidSocket(Screen):
    def client(self):
        demar = self.ids.demar
        demar.text = f"server demarré... est en ecoute  {ip}:{port}"
        return demar.text
        

class NextScreen(Screen):
    def accepter(self):
        pass
        # etabli = self.ids.etabli
        # etabli.text = f"[+] {adrr[0]}:{adrr[1]} est connecté"
        # return etabli.text
        
        
#kv = Builder.load_file('socketapp.kv')

class SocketApp(MDApp):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        layout = Builder.load_file('socketapp.kv')
        return layout

if __name__ == '__main__':
    Inst = SocketApp()
    Inst.run()