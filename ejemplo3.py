# Dado el enunciado del genero de una persona. Evaluar si es mujer, o es hombre.

print("Inrtoducir genero:")
genero = str(raw_input())
# print(genero)


if(genero == "femenino"):
    print("Es mujer")

elif(genero == "masculino"):
    print("Es hombre")

else:
    print("No ingreses huevadas")