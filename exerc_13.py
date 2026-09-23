#!/usr/bin/env python3

bases_nitrogenadas = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

tuplas = []

for DNA in bases_nitrogenadas:
    tupla = (len(DNA), DNA)
    tuplas.append(tupla)

for numero, (comprimento, DNA) in enumerate(tuplas, start=1):
    print(numero, comprimento, DNA, sep="\t")
