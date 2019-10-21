import kivy
import sqlalchemy as db
import json
engine = db.create_engine('mysql+mysqlconnector://root:asdasdasdasd@localhost:3306/uejn_afigestion')

kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from kivy.config import Config
Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 400)

class Contenedor_01(BoxLayout):
    def __init__(self, **kwargs):
        super(Contenedor_01, self).__init__(**kwargs)
        connection = engine.connect()
        metadata = db.MetaData()
        beneficios = db.Table('afiliacion_estados', metadata, autoload=True, autoload_with=engine)
        #print(beneficios.columns.keys())
        query = db.select([beneficios])
        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()
        def recorrerArray( ResultSet ):
            for x in ResultSet[:5]:
                if(x[2]):
                    self.add_widget(Label(text=x[1]))
                    print(x[2])


        print(recorrerArray( ResultSet ))


    
class MainApp(App): 
    title = "Hola Mundo"

    def build(self):
        return Contenedor_01()
        
if __name__ == '__main__':
    MainApp().run()
