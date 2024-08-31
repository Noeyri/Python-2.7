# Dado el enunciado para calcular dos numeros en: las operaciones de suma, resta, multipicar y dividir, y dando como resultado la resolucion de la operacion dada.

print ("Inicio del programa:")

repetir = True
while (repetir):
# Inicio del while - repetir.

    hacer = True
    while (hacer):
    # Inicio del while - hacer.

        print("Ingrese el N1:")
        N1 = str(raw_input())
        # if(N1.is_integer()):
        #     print("Ingrese el N1:")
        if (N1.isdigit()):
            print ("El dato ingrasado es un numero.")
            hacer = False
        else:
            print ("El dato ingresado no es un numero, vuelva a intentar:")
            hacer = True
    # Fin del while - hacer.


    otro = True
    while (otro):

        print("Ingrese el N2:")
        N2 = str(raw_input())

        if (isinstance(N2, int) or isinstance(N2, float)):
            print ("El dato ingrasado es un numero.")
            otro = False

        else:
            print ("El dato ingresado no es un numero, vuelva a intentar:")
            otro = True


    signo = True
    while (signo):

        print("Ingrese que operacion quiere usar:")
        print("suma," + " resta," + " multiplicar" " o" + " dividir;")
        operacion = str(raw_input())
        # signo = False

        suma = int(N1) + int(N2)

        resta = int(N1) - int(N2)

        multiplicar = int(N1) * int(N2)

        dividir = int(N1) / int(N2)


        if ("suma" == operacion):
            signo = False
            print("Resultado:")
            print(suma)

        elif("resta" == operacion):
            signo = False
            print("Resultado:")
            print(resta)

        elif("multiplicar" == operacion):
            signo = False
            print("Resultado:")
            print(multiplicar)

        elif("dividir" == operacion):
            signo = False
            print("Resultado:")
            print(dividir)

        else:
            print("La operacion ingresada es invalida")
            signo = True

    continuar = True
    while (continuar):
    # Inicio del While - Continuar.

        print("Desea ingresar otro Numero:")
        print("Diga : si , o no.")

        ingresar = str(raw_input())

        if (ingresar == "si"):
            continuar = False
            repetir = True

        elif (ingresar == "no"):
            continuar = False
            repetir = False

        else:
            continuar = True
# Fin del While - Continuar.