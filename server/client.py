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

class ScreenManagement(ScreenManager):
    pass


class SocketClient(Screen):
    def connexion(self):
        ip, port = socket.gethostbyname(socket.gethostname()), 6919
        socket_s = ip, port
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect(socket_s)
        
        demar = self.ids.demar
        demar.text = "Connexion établi avec le server"
        
class ValidSocket(Screen):
    def client(self):
        pass
        # mdp = self.ids.mdp.text
        # mdp_enc = mdp.encode("utf-8")
        # self.server_sock.sendall(mdp_enc)
        # 
        # receve = self.server_sock.recv(1024)
        # data = receve.decode("utf-8")
        # dossiers = self.ids.dossiers
        # dossiers.text = data

#kv = Builder.load_file('socketapp.kv')

class SocketClientApp(MDApp):
    def build(self):
        Window.clearcolor = (0,0,0,0)
        layout = Builder.load_file('socketclient.kv')
        return layout

if __name__ == '__main__':
    Inst = SocketClientApp()
    Inst.run()