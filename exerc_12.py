#/usr/bin/env python3
bases_nitrogenadas = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

tuplas = []

for dna in bases_nitrogenadas:
    tupla = (len(dna), dna)
    tuplas.append(tupla)

for comprimento, dna in tuplas:
    print(comprimento, dna, sep="\t")
