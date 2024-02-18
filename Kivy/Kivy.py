import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# ---------------
# https://www.youtube.com/watch?v=bMHK6NDVlCM&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=1
# 1
# see: 01.png
class MyApp(App):
    def build(self):
        # return Label(text="Tech with Amir")
        return MyGrid() # 2
# MyApp().run()
# ---------------

# ---------------
# https://www.youtube.com/watch?v=QUHnJrFouv8&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=2
# 2
# see: 02.png
class MyGrid(GridLayout):
    def __init__(self, **kwargs):

        super(MyGrid, self).__init__(**kwargs)

        self.inside = GridLayout() # 3

        # self.cols = 2
        self.cols = 1            # 3

        self.inside.cols = 2     # 3
        
        # self.add_widget(Label(text="First_name: "))
        self.inside.add_widget(Label(text="First_name: ")) # 3
        self.first_name = TextInput(multiline=False)
        # self.add_widget(self.first_name)
        self.inside.add_widget(self.first_name)            # 3
        
        # self.add_widget(Label(text="Last_name: "))
        self.inside.add_widget(Label(text="Last_name: "))  # 3
        self.last_name = TextInput(multiline=False)
        # self.add_widget(self.last_name)
        self.inside.add_widget(self.last_name)             # 3
        
        # self.add_widget(Label(text="Email: "))
        self.inside.add_widget(Label(text="Email: "))      # 3
        self.email = TextInput(multiline=False)
        # self.add_widget(self.email)                      #3
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        # ---------------
        # https://www.youtube.com/watch?v=fGWHQA3LhJ8&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=3
        # 3
        # see: 03-1.png
        self.submit = Button(text="Submit", font_size=40)

        self.submit.bind(on_press=self.pressed)
        # see 03-3.png

        self.add_widget(self.submit)        
        # ab yahan 1 masla h k submit ka button 1 side par ho gya h, hame usy beech me lay kar aana h, us k lye ye karen gy k
        # main layout ko 2 rows me devide kar den gy, opar wali row me <first_name>, <last_name> and <email> aa jayen gy, or neechy wali row me srif 
        # beech me <submit> ka button ho ga. is k lye ham <inside> k name sy Gridlayout bana rahy hen.
         
        # see: 03-2.png
    def pressed(self, instance):
        f_name = self.first_name.text # 03-4.png
        l_name = self.last_name.text  # 03-4.png
        email = self.email.text       # 03-4.png
                
        # print("Pressed")
        print(f"\nFirstName: {self.f_name}\nLastName: {self.l_name}\nEmail: {self.email}\n") # see: 03-4.png
        
        # Clear the boxes after print
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""
        
# ---------------
# https://www.youtube.com/watch?v=AS3b70pLYEU&list=PLzMcBGfZo4-kSJVMyYeOQ8CXJ3z1k7gHn&index=4
# 4
# see: 04.png
"""
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        return MyGrid() # 2

class MyGrid(GridLayout):
    def __init__(self, **kwargs):

        super(MyGrid, self).__init__(**kwargs)

        self.inside = GridLayout()

        self.cols = 1

        self.inside.cols = 2
        
        self.inside.add_widget(Label(text="First_name: "))
        self.first_name = TextInput(multiline=False)
        self.inside.add_widget(self.first_name)
        
        self.inside.add_widget(Label(text="Last_name: "))
        self.last_name = TextInput(multiline=False)
        self.inside.add_widget(self.last_name)
        
        self.inside.add_widget(Label(text="Email: "))
        self.email = TextInput(multiline=False)
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)
        self.submit = Button(text="Submit", font_size=40)

        self.add_widget(self.submit)        

    def pressed(self, instance):
        f_name = self.first_name.text
        l_name = self.last_name.text
        email = self.email.text
                
        print(f"\nFirstName: {self.f_name}\nLastName: {self.l_name}\nEmail: {self.email}\n") # see: 03-4.png
        
        self.first_name.text = ""
        self.last_name.text = ""
        self.email.text = ""

MyApp().run()
"""
# ye poora likhny k bajay ham ye bhi kar sakty thy:
"""
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
""" > my_app.py
    

"""
<MyGrid>  # copy your class name

	f_name:name_1
	l_name:name_2
	email:user_email

	GridLayout:
		cols:1
		size: root.width, root.height # taky ye poori screen par aay, warna bohot choti c jaga par aay ga.
		
		GridLayout:  # copy your class name
			cols:2
			
			Label:
				text: "FirstName: "
			TextInput:
				id: name_1
				multiline:False
			
			Label:
				text: "LastName: "		
			TextInput:
				id: name_2
				multiline:False


			Label:
				text: "Email: "		
			TextInput:
				id: user_email
				multiline:False
			
		Button:
			text: "Submit"
			on_press: root.btn()
""" > My.kv  # is file name ka andar zaroori h k:
    # 1- ye lower case ho.
    # 2- main script ki main class ka name ho <App> strip kar k, (eg. agar meri main class ka name <MyApp> h to me is file ka name my.kv rakhun ga, agar <YOUR> h to is file ka name your.kv rakhun ga) 
    
    # is file me koi comment # nahi hona chahye. yahan comment srif samjahny k lye likhy hen. 
    

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------

# ---------------
MyApp().run()

