"""
Solución del laboratorio
"""
#Importamos las funciones de la carpeta custom_functions para utilizarlas en el trabajo
from custom_functions import temperature_methods
#Creamos las listas necesarias
santander=[]
guajira=[]
narino=[]
#Mensaje de Bienvenida
print("Bienveido al OMN")
print("Este programa está diseñado para hacer un análizis de datos de las temperaturas de diferentes departamentos")
#Creamos un integro que reciba la opción del usuario
a=int(input("Escoge las siguientes opciones: \n 1:Departamento de Santander \n 2:Departamento de La Guajira \n 3:Departamento de Nariño \n 4:Todo el país \n Escoge la opción: "))
#Creamos un if y then para la opcion que el usuario vaya a escoger
if a==1:
    #Simplemente se recogen las funciones anteriores y se utilizan en el proyecto
    print("Departamento de Santander")
    temperature_methods.recolectar_datos(santander)
    print("El promedio de las temperaturas en Santander fue de:")
    print (temperature_methods.promedio(santander))
    print("La temperatura mayor en Santander fue de: ")
    print (temperature_methods.mayor(santander))
    print("La temperatura donde fue mayor es en: ")
    temperature_methods.mes(santander)
    print("La desviación estándar es: ")
    print (temperature_methods.des_estandar(santander))
    print("Departamento de Santander")
else:
    if a==2:
        print("Departamento de La Guajira")
        temperature_methods.recolectar_datos(guajira)
        print("El promedio de las temperaturas en La Guajira fue de: ")
        print(temperature_methods.promedio(guajira))
        print("La temperatura mayor en La Guajira fue de: ")
        print (temperature_methods.mayor(guajira))
        print("El mes donde fue mayor es: ")
        temperature_methods.mes(guajira)
        print("La desviación estándar es: ")
        print(temperature_methods.des_estandar(guajira))
        print("Departamento de La Guajira")
    else:
        if a == 3:
            print("Departamento de Nariño")
            recolectar_datos(narino)
            print("El promedio de las temperaturas en Nariño fue de: ")
            print(promedio(narino))
            print("La temperatura mayor en Nariño fue de: ")
            print(mayor(narino))
            print("El mes donde fue mayor es: ")
            mes(narino)
            print("La desviación estándar es de: ")
            print(des_estandar(narino))
            print("Departamento de Nariño")
        else:
            if a == 4:
                print("Departamento de Santander")
                recolectar_datos(santander)
                print("El promedio de las temperaturas en Santander fue de:")
                print(promedio(santander))
                print("La temperatura mayor en Santander fue de: ")
                print(mayor(santander))
                print("La temperatura donde fue mayor es en: ")
                mes(santander)
                print("La desviacón estándar es: ")
                print(des_estandar(santander))
                print("Departamento de Santander")
                print("Departamento de La Guajira")
                recolectar_datos(guajira)
                print("El promedio de las temperaturas en La Guajira fue de:")
                print(promedio(guajira))
                print("La temperatura mayor en La Guajira fue de: ")
                print(mayor(guajira))
                print("La temperatura donde fue mayor es en: ")
                mes(guajira)
                print("La desviación estándar es: ")
                print(des_estandar(guajira))
                print("Departamento de La Guajira")
                print("Departamento de Nariño")
                recolectar_datos(narino)
                print("El promedio de las temperaturas en Nariño fue de:")
                print(promedio(narino))
                print("La temperatura mayor en Nariño fue de: ")
                print (mayor(narino))
                print("La temperatura donde fue mayor es en: ")
                mes(narino)
                print("La desviación estándar es: ")
                print(des_estandar(narino))
                print("Departamento de Narino")
                prom_pais=((mayor(santander)+mayor(guajira)+mayor(guajira))/3)
                print("El promedio del país fue de: ")
                print(prom_pais)
                if (mayor(santander)>mayor(narino)>mayor(guajira)):
                    print("La temperatura mayor fue en Santander con: ")
                    print(mayor(santander))
                    print("En el mes de: ")
                    mes(santander)
                else:
                    if(mayor(santander)>mayor(guajira)>mayor(narino)):
                        print("La temperatura mayor fue en Santander con: ")
                        print(mayor(santander))
                        print("En el mes de: ")
                        mes(santander)
                    else:
                        if(mayor(guajira)>mayor(santander)>mayor(narino)):
                            print("La temperatura mayor fue en La Guajira con: ")
                            print(mayor(guajira))
                            print("En el mes de: ")
                            mes(guajira)
                        else:
                            if (mayor(guajira)>mayor(narino)>mayor(santander)):
                                print("La temperatura mayor fue en La Guajira con : ")
                                print(mayor(guajira))
                                print("En el mes de: ")
                                mes(guajira)
                            else:
                                if (mayor(narino)>mayor(santander)>mayor(guajira)):
                                    print("La temperatura mayor fue en Nariño con: ")
                                    print(mayor(narino))
                                    print("En el mes de: ")
                                    mes(narino)
                                else:
                                    if (mayor(narino)>mayor(guajira)>mayor(santander)):
                                        print("La temperatura mayor fue en Nariño con: ")
                                        print(mayor(narino))
                                        print("En el mes de: ")
                                        mes(narino)
#Desarrollado por Pedro Gómez / ID:000396221 / CACE Producciones      
