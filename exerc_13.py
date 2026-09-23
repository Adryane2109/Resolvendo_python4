#!/usr/bin/env python3
bases_nitrogenadas = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

tuplas = [(i, len(DNA), DNA) for i, DNA in enumerate(bases_nitrogenadas, start=1)]

for numero, comprimento, DNA in tuplas:
    print(numero, comprimento, DNA, sep="\t")
