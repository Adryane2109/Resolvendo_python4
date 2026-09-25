#!/usr/bin/env python3
import sys

inicio = int(sys.argv[1])
fim = int(sys.argv[2])

numeros = [i for i in range(inicio, fim + 1)]

print(numeros)

# parte 2 do exercício:
for numero in numeros:
    if numero % 2 != 0:
        print(numero)
