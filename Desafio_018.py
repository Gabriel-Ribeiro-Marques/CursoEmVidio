#Desafio 018, Curso em Video.
import math as m

x = float(input('qual o angulo: '))

print(f'O Seno é igual a: {m.sin(m.radians(x)):.2f}')
print(f'A cosseno é igual a: {m.cos(m.radians(180 - x)):.2f}')
print(f'A Tangente é igual a: {m.tan(m.radians(180 - x)):.2f}')
