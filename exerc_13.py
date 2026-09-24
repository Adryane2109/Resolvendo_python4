#!/usr/bin/env python3
bases_nitrogenadas = ['ATGCCCGGCCCGGC', 'GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT', 'ATGGGCCC']

#imprimindo a posição, o comprimento e a sequência:
for posicao, dna in enumerate(bases_nitrogenadas, start=1):
    print(posicao, len(dna), dna, sep="\t")
