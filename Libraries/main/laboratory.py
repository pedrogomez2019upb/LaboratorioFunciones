"""
Solución del laboratorio
"""
#Se utilizan las funciones de la vez pasada y
#se modifican para que tiren solamente resultados
def recolectar_datos(x):
    #Se crea el contador
    i=0
    for i in range(0,12):    
        #Retomamos lo del primer ejercicio        
        a=i+1
        b=int(input("Por favor ingrese la temperatura {}:".format(a)))
        c=x.append(b)
#Creamos la segunda función
def promedio(x):
    sumatoria=sum(x)
    promedio=sumatoria/12
    print(promedio)
#Creamos la tercer función
def mayor(x):
    a=max(x)
    print(a)
#Creamos la cuarta función
def mes(x):
    a=max(x)
    b=x.index(a)
    if b == 0:
        c="Enero"
    else:
        if b == 1:
            c="Febrero"
        else:
            if b == 2:
                c="Marzo"
            else:
                if b == 3:
                    c="Abril"
                else:
                    if b == 4:
                        c="Mayo"
                    else:
                        if b == 5:
                            c="Junio"
                        else:
                            if b == 6:
                                c="Julio"
                            else:
                                if b == 7:
                                    c="Agosto"
                                else:
                                    if b == 8:
                                        c="Septiembre"
                                    else:
                                        if b == 9:
                                            c="Octubre"
                                        else:
                                            if b == 10:
                                                c="Noviembre"
                                            else:
                                                if b == 11:
                                                    c="Diciembre"
    #Se imprime los resultados
    print(c)
def des_estandar(x):
    import statistics
    a=statistics.stdev(x)
    print(a)
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
    recolectar_datos(santander)
    print("El promedio de las temperaturas en Santander fue de:")
    promedio(santander)
    print("La temperatura mayor en Santander fue de: ")
    mayor(santander)
    print("La temperatura donde fue mayor es en: ")
    mes(santander)
    print("La desviación estándar es: ")
    des_estandar(santander)
    print("Departamento de Santander")
else:
    if a==2:
        print("Departamento de La Guajira")
        recolectar_datos(guajira)
        print("El promedio de las temperaturas en La Guajira fue de: ")
        promedio(guajira)
        print("La temperatura mayor en La Guajira fue de: ")
        mayor(guajira)
        print("El mes donde fue mayor es: ")
        mes(guajira)
        print("La desviación estándar es: ")
        des_estandar(guajira)
        print("Departamento de La Guajira")
    else:
        if a == 3:
            print("Departamento de Nariño")
            recolectar_datos(narino)
            print("El promedio de las temperaturas en Nariño fue de: ")
            promedio(narino)
            print("La temperatura mayor en Nariño fue de: ")
            mayor(narino)
            print("El mes donde fue mayor es: ")
            mes(narino)
            print("La desviación estándar es de: ")
            des_estandar(narino)
            print("Departamento de Nariño")
        else:
            if a == 4:
                print("Departamento de Santander")
                recolectar_datos(santander)
                print("El promedio de las temperaturas en Santander fue de:")
                promedio(santander)
                print("La temperatura mayor en Santander fue de: ")
                mayor(santander)
                print("La temperatura donde fue mayor es en: ")
                mes(santander)
                print("La desviacón estándar es: ")
                des_estandar(santander)
                print("Departamento de Santander")
                print("Departamento de La Guajira")
                recolectar_datos(guajira)
                print("El promedio de las temperaturas en La Guajira fue de:")
                promedio(guajira)
                print("La temperatura mayor en La Guajira fue de: ")
                mayor(guajira)
                print("La temperatura donde fue mayor es en: ")
                mes(guajira)
                print("La desviación estándar es: ")
                des_estandar(guajira)
                print("Departamento de La Guajira")
                print("Departamento de Nariño")
                recolectar_datos(narino)
                print("El promedio de las temperaturas en Nariño fue de:")
                promedio(narino)
                print("La temperatura mayor en Nariño fue de: ")
                mayor(narino)
                print("La temperatura donde fue mayor es en: ")
                mes(narino)
                print("La desviación estándar es: ")
                des_estandar(narino)
                print("Departamento de Narino")

#Desarrollado por Pedro Gómez / ID:000396221 / CACE Producciones      