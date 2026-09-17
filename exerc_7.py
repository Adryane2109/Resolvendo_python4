#!/usr/bin/env python3
#parte 1 do exercicio
numeros = [101, 2, 15, 22, 95, 33, 2, 27, 72, 15, 52]

numeros_ordenados = sorted(numeros)

for numero in numeros_ordenados:
    print(numero)

#parte 2 e 3 do exercicio
pares = 0
impares = 0

for numero in numeros:
    if numero % 2 == 0:
        pares = pares + numero
    else:
        impares = impares + numero
print("Soma dos numeros pares:", pares)
print("Soma dos numeros impares:", impares)
