
from cgitb import text
from operator import itemgetter
from tkinter import dialog
from turtle import title
from typing import Text
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
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatButton
from kivy.uix.behaviors import ButtonBehavior 
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix import MDAdaptiveWidget 
from kivymd.uix.dialog import MDDialog  
from kivymd.uix.button import MDFlatButton
from kivymd.uix.button import MDFillRoundFlatButton
import googlemaps
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.textfield import MDTextField 
from kivy.uix.textinput import TextInput

# Creating the app and the link to the kivy file. 

Builder.load_file('report.kv')

class MyApplication(Widget):
# In this class or the 'root' is where is possible to add logic and functionality to the App. 
    dialog = None 
# this 2 floating bottoms are not bind to the fucntions I planned, for the moment only can print. 
    def on_press_buttom1(self):
        print('pressed')

    def on_press_buttom2(self):
        print('hello')

    def dialog_popup(self):    
        if not self.dialog :
            self.dialog = MDDialog (
            title = 'User details',
            type="custom",
            size_hint = (.5, .7),
            buttons = [
                MDFlatButton(
                    text = 'Cancel', on_release = self.close_dialog),
                MDRectangleFlatButton( 
                    text = 'Save',on_release = self.save_info ),   
                ],
            # I have trying to add a textinput here but it does not work.
            )

        self.dialog.open() 

    def close_dialog(self,obj):
        self.dialog.dismiss()

    def save_info (self,obj):
        self.dialog.dismiss()
        
    def dialog_draft(self):
        if not self.dialog :
            self.dialog = MDDialog (
            title = 'User details',
            type = 'simple',
            radius=[20, 7, 20, 7],
            size_hint = (.5, .7), 
            buttons = [
                MDFlatButton(
                    text = 'Cancel', on_release = self.close_dialog),
                MDRectangleFlatButton( 
                    text = 'Save',on_release = self.save_info ),   
                ],
            # I have trying to add a textinput here but it does not work.
            )

        self.dialog.open()

        
    def reportar_boton (self):
        pass 
    # As it happend with all the bottons I could not use the bind methods and give them and functionality. 
    # I tried diferent codes but they dont work: 
        #self.bind(on_press= Addphoto)
        # 
        # Addphoto.open () 
        # return Addphoto 
        #self.reporte.bind (on_press =  Addphoto )
        
class ReportApp(MDApp):
	def build(self):
        
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "BlueGray"
        

    
		return MyApplication ()

ReportApp().run()
	
	
