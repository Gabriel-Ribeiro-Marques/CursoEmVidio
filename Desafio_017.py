#Desafio 017, Curso em Video.
import math 

print('Descubra a hipotenusa')

a = float(input('CA: '))
b = float(input('CO: '))

print(f'A hipotenusa é igual a: {math.sqrt((math.pow(a, 2)) + (math.pow(b, 2))):.2f}')

#usando o MODULO math, o print é simplificado 

print(f'A hipotenusa é igual a: {math.hypot(a, b):.2f}')
