#!/usr/bin/env python3
bases_nitrogenadas = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
print(bases_nitrogenadas)
for dna in bases_nitrogenadas:
	print(len(dna), dna, sep="\t")
