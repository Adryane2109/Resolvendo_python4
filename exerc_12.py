#/usr/bin/env python3
bases_nitrogenadas = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

tuplas = [(len(dna), dna) for dna in bases_nitrogenadas]

for comprimento, dna in tuplas:
    print(comprimento, dna, sep="\t")
