import os
import random


def gerar_numeros(ini, fim, qtd):
    lst_num = [random.randint(ini, fim) for i in range (qtd)]
    return lst_num

def somar_numeros(num1, num2):
    sum = num1 + num2
    return sum
def sub_numeros(num1, num2):
    sub = num1 - num2
    return sub
def mult_numeros(num1, num2):
    mult = num1 * num2
    return mult
def div_numeros(num1, num2):
    div = num1 / num2
    return div

# inicio do algoritmo
inicio = 1
final = 10
quantidade = 2
lst_numeros = gerar_numeros (inicio, final, quantidade)
soma_numeros = sum 

# lst_numeros = gerar_numeros(inicio, final, quantidade)

print(lst_numeros[0])
print(lst_numeros[1])

some = somar_numeros(lst_numeros[0], lst_numeros[1])
print(some)
sub = sub_numeros(lst_numeros[0], lst_numeros[1])
print(sub)
mult = mult_numeros(lst_numeros[0], lst_numeros[1])
print(mult)
div = div_numeros(lst_numeros[0], lst_numeros[1])
print(div)
