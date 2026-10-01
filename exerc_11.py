#!/usr/bin/env python3
bases_nitrogenadas = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#print de cada elemento:
for dna in bases_nitrogenadas:
	print(dna)

#imprimindo o comprimento e a sequência (separados por uma guia):
for dna in bases_nitrogenadas:
	print(len(dna), dna, sep="\t")
