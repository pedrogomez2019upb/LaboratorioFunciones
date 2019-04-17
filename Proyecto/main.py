#Desarrollo para un departamento
#Se crea una lista con un contador
santander = []
i = 0
#Creamos un mensaje de bienvenida
print("Bienvenido al ONM")
#Ponemos un rango de 0 a 12 para que ingrese los datos de las temperaturas
for i in range (0,12):
    x=int(input("Por favor ingresa la temperatura: "))
    #.append nos permite añadir un elemento a la lista
    santander.append(x)
#Imprimimos los resultados 
print("Los datos ingresados son : {}".format(santander))
#Utilizamos la funcion sum() que nos permite hacer una sumatoria 
sum_santander = sum(santander)
print("La sumatoria es: {}".format(sum_santander))
prom_santander=sum_santander/12
int_prom_santander=int(prom_santander)
print("El promedio es: {}".format(int_prom_santander))
#Utilizamos la función max() para buscar el número mayor
#y lo guardamos en una variable
max_santander = max(santander)
print("El número mayor de la lista es: {}".format(max_santander))
#Utilizamos la función index() para buscar la posición de
#un dato en una lista
pos_max_santander= santander.index(max_santander)
print("La posición de la temperatura mayor es: {}".format(pos_max_santander))
#Hacemos una condicional if y then para saber el mes adentro
#de la lista
if pos_max_santander == 0:
    pos_max_santander_mes = "Enero"
else:
    if pos_max_santander == 1 :
        pos_max_santander_mes = "Febrero"
    else:
        if pos_max_santander == 2:
            pos_max_santander_mes = "Marzo"
        else:
            if pos_max_santander == 3:
                pos_max_santander_mes = "Abril"
            else:
                if pos_max_santander == 4:
                    pos_max_santander_mes = "Mayo"
                else:
                    if pos_max_santander == 5:
                        pos_max_santander_mes = "Junio"
                    else:
                        if pos_max_santander == 6:
                            pos_max_santander_mes = "Julio"
                        else:
                            if pos_max_santander == 7:
                                pos_max_santander_mes = "Agosto"
                            else:
                                if pos_max_santander == 8:
                                    pos_max_santander_mes = "Septiembre"
                                else:
                                    if pos_max_santander == 9:
                                        pos_max_santander_mes = "Octubre"
                                    else:
                                        if pos_max_santander == 10:
                                            pos_max_santander_mes = "Noviembre"
                                        else:
                                            if pos_max_santander == 11:
                                                pos_max_santander_mes = "Diciembre"
#Se imprime el resultado
print("El mes donde fue mayor es: {}".format(pos_max_santander_mes))
#Desarrollado por Pedro Gómez / ID:000396221 / CACE


