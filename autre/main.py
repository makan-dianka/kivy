from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.layout import Layout 
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        
        self.inside = GridLayout()
        self.inside.cols = 2
        
        self.inside.add_widget(Label(text="Votre nom : "))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)
        
        self.inside.add_widget(Label(text="Votre prènom : "))
        self.prenom = TextInput(multiline=False)
        self.inside.add_widget(self.prenom)
        
        self.inside.add_widget(Label(text="Votre E-mail : "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)
        
        self.add_widget(self.inside)
        
        self.submit = Button(text="Se soumettre", font_size=32)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)
        
    def pressed(self, instance):
        name = self.name.text
        prenom = self.prenom.text
        email = self.email.text
        print("\nNom : ",name, "\nPrènom : ",prenom, "\nEmail : ",email)
        
        self.name.text = ""
        self.prenom.text = ""
        self.email.text = ""

class Dagakane(App):
    def build(self):
        return MyGrid()

Dagakane().run()