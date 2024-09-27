print ("Lazo Jimenez Angel Jesus 3W")
Num = int(input("ingresar un numero para calcular su factorial: ")) #Pide al usuario ingresar un numero
factorial = 1 
if Num < 0:
    print("El factorial no está definido para números negativos.") #Verifica si el numero ingresado es menor a 0, si es el caso aparece ese mensaje
elif Num == 0:
    print("El factorial de 0 es 1.") #Si el usuario llegara ingresar el numero (0) le aparece que es igual a (1)
else:
    for i in range(1, Num + 1): 
        factorial *= i  
    print(f"El factorial de {Num} es {factorial} ") #En esta linea se muestra en pantalla el numero ingresado junto a su factorial