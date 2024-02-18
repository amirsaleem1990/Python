import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
	name = ObjectProperty(None) # get <name> from .kv file
	email = ObjectProperty(None) # get <email> from .kv file

	def btn(self):
		print(f"\nFirstName: {self.f_name.text}\nLastName: {self.l_name.text}\nEmail: {self.email.text}\n")
		self.f_name.text = ""
		self.l_name.text = ""
		self.email.text = ""

class MyApp(App):
	def build(self):
		return MyGrid()
MyApp().run()
