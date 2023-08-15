from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MyApp(MDApp):
    def build(self):

         label = MDLabel(text = "Welcome to MyApp",halign="center")
         return label

MyApp().run()