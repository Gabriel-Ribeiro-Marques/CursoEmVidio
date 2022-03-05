#Desafio 018, Curso em Video.
import random
a = str(input('aluno1: '))
b = str(input('aluno2: '))
c = str(input('aluno3: '))
d = str(input('aluno4: '))

list = [a, b, c, d]

print(f'O escohido foi: {random.choice(list)}')