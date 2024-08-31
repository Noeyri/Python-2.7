#

print("Introdusca su genero:")
genero = str(raw_input())


if(genero == "femenino"):
    print("Es mujer")

    print("Introdusca el tiempo de experiencia:")
    experiencia = int(raw_input())

    if(experiencia >= 15):
        print("Nvl. de experiencia")
        print(experiencia)
        print("Aprobado")

    else:
        print("Nvl. de experiencia")
        print(experiencia)
        print("Desaprobado")



elif(genero == "masculino"):
    print("Es hombre")

    print("Introdusca el tiempo de experiencia:")
    experiencia = int(raw_input())

    if(experiencia >= 10):
        print("Nvl. de experiencia:")
        print(experiencia)
        print("Aprobado")

    else:
        print("Nvl. de experiencia:")
        print(experiencia)
        print("Desaprobado")



else:
    print("Genero incorrecto.")