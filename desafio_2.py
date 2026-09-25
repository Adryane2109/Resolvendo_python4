#!/usr/bin/env python3

seq1 = "ATGAACC-GA"
seq2 = "ATGCACT-GA"

identidades = 0

#para comparar os nucleotídeos em cada índice e contar as identidades
for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
        identidades += 1

#para calcular a porcentagem de identidade das duas sequências
identidade = (identidades / len(seq1)) * 100

print(identidade)
