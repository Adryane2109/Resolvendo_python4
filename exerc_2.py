#!/usr/bin/env python3
#criando/salvando a string na variavel taxa:
>>> taxa = "sapiens, erectus, neanderthalensis"
>>> print(taxa)
sapiens, erectus, neanderthalensis

#usando o comando print(taxa[1]):
>>> print(taxa[1])
a
>>> print(taxa[0])
s
>>> print(taxa[3])
i
>>> print(taxa[2])
p

#imprimindo a classificação da variável:
>>> print(type(taxa))
<class 'str'>

#dividir taxa em palavras individuais utilizando o separador ',':
>>> print(taxa.split(","))
['sapiens', ' erectus', ' neanderthalensis']

#salvando o resultado em uma nova variável denominada species:
>>> species = taxa.split(",")
>>> print(species)
['sapiens', 'erectus', 'neanderthalensis']

#comparando o print(species[1]), agora com uma lista:
>>> print(species[1])
erectus 

#imprimindo a classificação da variável com a função type:
>>> print(type(species))
<class 'list'>

#organizando em ordem alfabética:
>>> print(sorted(species))
['erectus', 'neanderthalensis', 'sapiens']

#organizando pelo comprimento da palavra com o argumento key:
>>> print(sorted(species, key=len))
['sapiens', 'erectus', 'neanderthalensis']

