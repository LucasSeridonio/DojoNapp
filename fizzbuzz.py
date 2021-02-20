# -*- coding: utf-8 -*-

def fizzbuzz(numero):
    if numero == 0:
        return 0
    if numero % 15 == 0:
        return 'fizzbuzz'
    if numero % 5 == 0:
        return 'buzz'
    if numero % 3 == 0:
        return 'fizz'
    else:
        return numero


lista_elementos = list()

for i in range(0, 101):
    print(fizzbuzz(i), end=', ')

# Realizando os testes
assert fizzbuzz(0) == 0
assert fizzbuzz(1) == 1
assert fizzbuzz(2) == 2
assert fizzbuzz(6) == 'fizz'
assert fizzbuzz(3) == 'fizz'
assert fizzbuzz(5) == 'buzz'
assert fizzbuzz(15) == 'fizzbuzz'
assert fizzbuzz(30) == 'fizzbuzz'
assert fizzbuzz(31) == 31
assert fizzbuzz(100) == 'buzz'
