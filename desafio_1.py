#!/usr/bin/env python3

from random import randrange

sequencia = list("ATGCCCGG")

for i in range(len(sequencia)):
    A = randrange(len(sequencia))
    B = randrange(len(sequencia))
    sequencia[A], sequencia[B] = sequencia[B], sequencia[A]

print(sequencia)
