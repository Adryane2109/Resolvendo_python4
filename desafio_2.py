#!/usr/bin/env python3

seq1 = "ATGAACC-GA"
seq2 = "ATGCACT-GA"

identicas = 0

for i in range(len(seq1)):
    if seq1[i] == seq2[i]:
        identicas += 1

identidade = (identicas / len(seq1)) * 100

print("Identidade:", identidade, "%")
