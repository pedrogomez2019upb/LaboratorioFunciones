#Importamos la libreria unittest
import unittest
#Importamos las funciones de la carpeta
from custom_functions import temperature_methods
#Creamos una clase para empezar a hacer las pruebas unitarias
class TestStringMethods(unittest.TestCase):
    #Definimos las funciones para hacer las pruebas unitarias individuales
    def promedio(self):
        x=[74,56,85,78,96,32,45,14,52,68,78,25]
        promedio = temperature_methods.promedio(x)
        #Decimos que la respuesta sea igual al resultado que yo diga
        self.assertEqual(promedio,58.58)
#Aplicamos esto para los demás casos
    def mayor (self):
        x=[12,23,34,45,56,67]
        mayor=temperature_methods.mayor(x)

        self.assertEqual(mayor,67)

    def promedio1(self):
        x=[56,45,23,67,56,45,34,87,12,34,45,56]
        promedio = temperature_methods.promedio(x)

        self.assertEqual(promedio,58.58)

    def mayor1(self):
        x=[12,23,34,45,56,78,230]
        mayor=temperature_methods.mayor(x)

        self.assertEqual(mayor,230)
#Ejecutamos las pruebas unitarias
if __name__=="_main_":
    unittest.main
#Desarrollado por Pedro Gómez / ID:000396221 / CACE Producciones    