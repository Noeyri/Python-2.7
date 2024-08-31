#

from math import log10

# numeros = [16, 4, 9, 1, 3, 20, 8]
numeros = [12, 15, 20, 35, 10, 25, 12, 19, 18, 21, 24, 15, 12, 16, 15, 33, 22, 30, 10, 18, 14, 41, 17,  25, 14, 15, 48, 24, 15, 28, 20, 14, 15, 19, 23, 32, 11, 52, 18, 16]


# numeros.sort(reverse=True) -> ordenados al reves
numeros.sort()
print("Ordered numbers:")
print(numeros)

print("")

print("n = " + str(numeros.__len__()))
# "n" es el total de numeros.
n = numeros.__len__()
print("")

primerNumero = numeros[0]
ultimoNumero = numeros[len(numeros) - 1]

# "R" es el rango.
R = ultimoNumero - primerNumero
print("R = " + str(R))


# "K" es son los intervalos o las clases.
K = 1 + 3.322*log10(n)

# print("K = " + str(K))
print("Rounded:")
print("K = " + (str(int(round(K)))))

# "A" es la Amplitud.
A = R/K
print("Rounded:")
print("A = " + str(int(round(A))))

def buscar(limiteInferior, limiteSuperior):
    counter = 0
    for i in numeros:
        if(i>=limiteInferior and i<limiteSuperior):
            counter = counter + 1
    return counter

# "Xi" es la marca de clase.
# Xi = Li + Ls/2

limiteInferior = primerNumero
limiteSuperior = primerNumero + int(round(A))

print("")
print("Variable; Edad:" + "  |   fi  |   hi   |  hi%  |   Xi")

contador = 0
while (contador <= K):

    fi_Entre_n = int(buscar(limiteInferior, limiteSuperior))
    hi_Porcentual = int((fi_Entre_n/float(n)*100))
    xi = (limiteInferior + limiteSuperior)/float(2)

    # print("   [" + str(limiteInferior) + ";" + str(limiteSuperior) + "]" + " ----> |   " + str(fi_Entre_n)+ "   |  " + "{:0,.3f}".format(round(fi_Entre_n/float(n), 2)) + "  |  " + str(hi_Porcentual) + "%" + "  |  " + str(round(xi,2)))
    print("   [" + str(limiteInferior) + ";" + str(limiteSuperior) + "]" + " ----> |   " + str(fi_Entre_n)+ "   |  " + str((fi_Entre_n/float(n))) + "  |  " + str(hi_Porcentual) + "%" + "  |  " + str((xi)))

    contador = contador + 1
    limiteInferior = limiteInferior + int(round(A))
    limiteSuperior = limiteSuperior + int(round(A))

print()