import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder


from kivy.config import Config
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 400)

class Contenedor_01(BoxLayout):
		def mostrarBoton(self,nroBoton):
			if nroBoton == 1:
				self.add_widget(Contenedor_MostrarTexto_Boton_Uno())
			if nroBoton == 2:
				self.add_widget(Contenedor_MostrarTexto_Boton_Dos())
			if nroBoton == 3:
				self.add_widget(Contenedor_MostrarTexto_Boton_Tres())
			if nroBoton == 4:
				self.add_widget(Contenedor_MostrarTexto_Boton_Cuatro())


class Titulo(BoxLayout):
	None

class Contenedor_MostrarTexto_Boton_Uno(GridLayout):
	None

class Contenedor_MostrarTexto_Boton_Dos(BoxLayout):
	None

class Contenedor_MostrarTexto_Boton_Tres(BoxLayout):
	None

class Contenedor_MostrarTexto_Boton_Cuatro(BoxLayout):
	None	
	
class MainApp(App):	
	title = "Hola Mundo"

	def build(self):
		return Contenedor_01()
		
if __name__ == '__main__':
	MainApp().run()
