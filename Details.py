
from turtle import width
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
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix import MDAdaptiveWidget 
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
from kivymd.uix.card import MDCard
import googlemaps
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineIconListItem
from kivy.properties import StringProperty
from kivymd.uix.dropdownitem import MDDropDownItem
from kivy.uix.button import Button
from kivy.uix.slider import Slider
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp


Builder.load_file('details.kv')

class Details_reports (Widget):
	pass


class DetailsApp(MDApp):	
	def build(self):
		
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
    	
		return  Details_reports () 
       
         
DetailsApp().run()