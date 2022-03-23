
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy_garden.mapview import MapView, MapMarkerPopup 
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.behaviors import RectangularRippleBehavior, BackgroundColorBehavior
from kivymd.uix.behaviors import CircularRippleBehavior
from kivymd.icon_definitions import md_icons
from kivymd.uix.tab import MDTabsBase 
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.boxlayout import MDBoxLayout, MDAdaptiveWidget    
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.properties import ObjectProperty
from kivymd.uix.tab import MDTabsBase
from kivy.utils import get_color_from_hex
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRoundFlatButton



Builder.load_file('sos.kv')

class MyApplication(Widget):
    def on_press_buttom1(self):
        print('pressed')

    def on_press_buttom2(self):
        print('you are the best')
         

class Floating_Buttoms(MDRoundFlatButton):
    pass 


class Tab(MDFloatLayout, MDTabsBase):
    pass

class Float_lay(MDFloatLayout):
    def press (self):
        pass  



class SosApp(MDApp):
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
        
		return MyApplication ()

SosApp().run()
	
	
