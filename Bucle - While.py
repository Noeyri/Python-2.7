# Bucle "while"
#
# Hacer un programa que al ingreasar un salario, diga que "es un numero"; y si no es un numero, que diga "por favor vuelva intentar".
# Mostrar el numero del salario.
# Luego hacer si el salario es <= a pobre:
# pobre = 1000
# Para asi saber si dar bono o no dar bono.
# Por ultimo hacer que si el usuario "desea ingresar otro salario", y que escriba "si" o "no" para continuar.
# Y si el usuario escribe cualquier cosa, repetir hasta que escriba el "si" o "no".


# i = 1
#
# while(i < 6):
#     print(i)
#     # i += 1
#     # i = i + 1

# salario = ""


print("Inicio del programa")

repetir = True
while (repetir):
#Inicio de While - Repetir.

    hacer = True
    while (hacer):
    #Inicio del While - Hacer.

        print("Ingrese salario:")
        salario = str(raw_input())

        if (salario.isdigit()):
            print("El salario ingresado es un numero.")
            hacer = False
        else:
            print("El salario ingresado no es un numero, por favor vuelva a intentar.")
            hacer = True
    #Fin del While - Hacer.


    print("El salario ingresado es : " + salario)

    pobre = 1000

    if (int(salario) <= pobre):
        print("Dar bono.")
        print("")

    else:
        print("No dar bono.")
        print("")

    continuar = True
    while (continuar):
    #Inicio del While - Continuar.

        print("Desea ingresar otro salario:")
        print("Diga : si , o no.")

        ingresar = str(raw_input())

        if(ingresar == "si"):
            continuar = False
            repetir = True

        elif(ingresar == "no"):
            continuar = False
            repetir = False

        else:
            continuar = True
    #Fin del While - Continuar.


#Fin del While - Repetir.

print("Fin del programa")