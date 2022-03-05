#Desafio 020, Curso em Video.
import random

p1 = str(input('aluno 1: '))
p2 = str(input('aluno 2: '))
p3 = str(input('aluno 3: '))
p4 = str(input('aluno 4: '))

list = [p1, p2, p3, p4]

random.shuffle(list)

print(f'A sequencia de apresentação vai ser: {list}')