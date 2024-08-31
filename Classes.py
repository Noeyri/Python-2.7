class Humano:
    def __init__(self, edad):
        # self.edad = 25
        self.edad = edad
        # print "Hola chamo."

    def hablar(self, mensaje):
        print(mensaje)

objeto = Humano(26)

print "Hola soy una variable y tengo", objeto.edad

objeto.hablar ("Hola a todos.")