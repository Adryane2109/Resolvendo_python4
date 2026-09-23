#!/usr/bin/env python3
import sys

inicio = int(sys.argv[1])
fim = int(sys.argv[2])

numeros = [i for i in range(inicio, fim + 1) if i % 2 != 0]

for numero in numeros:
    print(numero)
