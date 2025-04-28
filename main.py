from kivymd.app import MDApp
from kivymd.uix.label import *
from kivymd.uix.screen import Screen
from kivymd.uix.button import *
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.textfield import MDTextField
from kivy.uix.image import Image
import sys

class FirstScreen(Screen):
    
    def __init__(self, **kwargs):
        
        super().__init__(**kwargs) 
           
        
        layout1 = FloatLayout()
        lab1 = MDLabel(text="Welcome To Tabel\nApp",
            font_style = "H4",
            halign = "center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),
            pos_hint={"top": 1},
            size_hint_y=None)
        layout1.add_widget(lab1)
        lab2 = MDLabel(text="Which Tabel You Want",
            font_style = "H5",
            halign = "center",
            theme_text_color="Custom",
            text_color=(1, 0, 0, 1),
            pos_hint={"top": 0.8},
            size_hint_y=None)
        self.texti = MDTextField(hint_text="Enter Which Tabel",
                            pos_hint={"top": 0.7, "x": 0.3},
                            size_hint=(None, None),
                            size=(350,50),
                            icon_left="numeric")
        but1 = MDRectangleFlatButton(text="OK",
                                     halign = "center",
                                     pos_hint = {"top": 0.6, "x": 0.4},
                                     size_hint=(None, None))
        but1.bind(on_release=self.change_screen)
        self.value = self.texti.text
        layout1.add_widget(self.texti)
        layout1.add_widget(lab2)
        layout1.add_widget(but1)
        self.add_widget(layout1)
        
    def change_screen(self, instance):
        second_screen = self.manager.get_screen('second')
        
        second_screen.set_value(self.texti.text)
        self.manager.current = 'second' 
        
class SecondScreen(Screen, ):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        
        
        self.lab3 = MDLabel(
            text="", 
            font_style="H4",
            halign="center",
            size_hint=(None, None),
            size=(400, 500),  
            pos_hint={"center_x": 0.5, "center_y": 0.5} 
        )
        but2 = MDRectangleFlatButton(text="back",
                                     halign = "center",
                                     pos_hint={"center_x": 0.5, "center_y": 0.9},
                                     size_hint=(None, None))
        but2.bind(on_release=self.change_scr)
        self.add_widget(but2)    
        self.add_widget(self.lab3)
    def set_value(self, value):
        
        try:
            itex = int(value)
            tabeltxt = ""
            for i in range(1, 11):
                tabeltxt += f"{itex} X {i} = {itex*i}\n"
                self.lab3.text = tabeltxt
        except ValueError:
            self.lab3.text = "Invalid Input"
    
    def change_scr(self, instance):
        self.manager.current = 'first'


class MathsTabel(MDApp):
    

    def build(self):
        self.screen = ScreenManager()
        self.screen.add_widget(FirstScreen(name='first'))
        self.screen.add_widget(SecondScreen(name='second'))
        if getattr(sys, 'frozen', False):
            # If frozen (running as .exe), use the path in the temporary folder
            self.icon = sys._MEIPASS + '/tabel.png'
        else:
            # If not frozen (running from source), use the direct path
            self.icon = 'tabel.png'
        return self.screen 

if __name__ == '__main__':
    MathsTabel().run()