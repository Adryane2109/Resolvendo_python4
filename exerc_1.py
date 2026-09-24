#!/usr/bin/env python3
#criando lista no interpretador e imprimindo com a função print:
>>> coisas_que_gosto = ['café','amiga Jesca','ler','piano','dormir']
>>> print(coisas_que_gosto)
['café', 'amiga Jesca', 'ler', 'piano', 'dormir']

#imprimindo elemento do meio da lista
>>> print(coisas_que_gosto[2])
ler

#substituindo elemento do meio por outro:
>>> coisas_que_gosto[2] = 'goodbye song'
>>> print(coisas_que_gosto)
['café', 'amiga Jesca', 'goodbye song', 'piano', 'dormir']

#adicionando elemento no final da lista com o método append:
>>> coisas_que_gosto.append('Deus')
>>> print(coisas_que_gosto)
['café', 'amiga Jesca', 'goodbye song', 'piano', 'dormir', 'Deus']

#adicionando elemento no começo da lista com o método insert:
>>> coisas_que_gosto.insert(0,'viajar')
>>> print(coisas_que_gosto)
['viajar', 'café', 'amiga Jesca', 'goodbye song', 'piano', 'dormir', 'Deus']

#adicionando elementos em qualquer posição da lista:
>>> coisas_que_gosto.insert(4,'sabados')
>>> print(coisas_que_gosto)
['viajar', 'café', 'amiga Jesca', 'goodbye song', 'sabados', 'piano', 'dormir', 'Deus']

#removendo elemento do final com o método pop:
>>> coisas_que_gosto.pop(-1)
'Deus'
>>> print(coisas_que_gosto)
['viajar', 'café', 'amiga Jesca', 'goodbye song', 'sabados', 'piano', 'dormir']

#removendo elemento do começo da lista:
>>> coisas_que_gosto.pop(0)
'viajar'
>>> print(coisas_que_gosto)
['café', 'amiga Jesca', 'goodbye song', 'sabados', 'piano', 'dormir']

#removendo elemento de qualquer posição (que não seja no início ou no final):
>>> coisas_que_gosto.pop(1)
'amiga Jesca'
>>> coisas_que_gosto.pop(2)
'sabados'
>>> print(coisas_que_gosto)
['café', 'goodbye song', 'piano', 'dormir']

#criando uma string com o método join e juntando os elementos com vírgula:
>>> ",".join(coisas_que_gosto)
'café,goodbye song,piano,dormir'
