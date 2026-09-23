#!/usr/bin/env python3

DNA = "COLE_AQUI_A_SEQUENCIA"

DNA = DNA.replace("GAATTC", "G^AATTC")

posicoes = []

for i in range(len(DNA)):
    if DNA[i] == "^":
        posicoes.append(i)

DNA = DNA.replace("^", "")

fragmentos = []
inicio = 0

for posicao in posicoes:
    fragmentos.append((inicio + 1, posicao, DNA[inicio:posicao]))
    inicio = posicao

fragmentos.append((inicio + 1, len(DNA), DNA[inicio:]))

for inicio, fim, fragmento in fragmentos:
    print(inicio, fim, len(fragmento), sep="\t")
