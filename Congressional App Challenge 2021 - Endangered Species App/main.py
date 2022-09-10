from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager,Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout 
from kivy.config import Config 
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.relativelayout import RelativeLayout

class MainApp(App):
  def build(self):
    return kv
  

    
class WindowManager(ScreenManager):
  pass

class MainWindow(Screen):
  pass

class SecondWindow(Screen):
  pass

class ThirdWindow(Screen):
  pass

class FourthWindow(Screen):
  pass

class TigerWindow(Screen):
  pass

class ParrotWindow(Screen):
  pass

class SharkWindow(Screen):
  pass

class WolfWindow(Screen):
  pass



kv = Builder.load_file("my.kv")

if __name__ == "__main__":
  MainApp().run()


