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
#Se crea la función para hacer desviacón estándar
def des_estandar(x):
    import statistics
    a=statistics.stdev(x)
    print(a)
#Desarrollado por Pedro Gómez / ID:000396221 / CACE Producciones  

