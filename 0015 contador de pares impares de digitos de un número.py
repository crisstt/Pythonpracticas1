# Contador de numeros pares e impares en los digitos de un numero dados
numerosPares = []
numerosImpares = []
nPar = 0
nImpar = 0
num = input("Introduce un numero para validar sus digitos si son pares o impares ")

for n in num:
    if int(n)%2 == 0:
        numerosPares.append(int(n)) 
        print("Numero Par : ",numerosPares[nPar])
        nPar += 1
    elif int(n)%2 != 0:
        numerosImpares.append(int(n))
        print("Numero Impar : ",numerosImpares[nImpar])
        nImpar += 1
print(numerosPares)
print("La cantidad de digitos Pares en el numero es : ", nPar)
print(numerosImpares)
print("La cantidad de digitos Impares en el numero es : ", nImpar)

#Usando bucle While
numerosPares1 = []
numerosImpares1 = []
nPar1 = 0
nImpar1 = 0
num1 = num

while (int(num1) > 0):
    for n in num1:
        if int(n)%2 == 0:
            numerosPares1.append(int(n)) 
            print("Numero Par : ",numerosPares1[nPar1])
            nPar1 += 1
        elif int(n)%2 != 0:
            numerosImpares1.append(int(n))
            print("Numero Impar : ",numerosImpares[nImpar1])
            nImpar1 += 1
        num1 = int(num1)//10
    print(numerosPares)
    print("La cantidad de digitos Pares en el numero es : ", nPar)
    print(numerosImpares)
    print("La cantidad de digitos Impares en el numero es : ", nImpar)
