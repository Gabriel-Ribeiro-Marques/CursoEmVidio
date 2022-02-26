#Desafio 004, Curso em Video.

p  = input('Valor: ')

print(f'uppe: {p.isupper()} \nalnum: {p.isalnum()} \nalpha: {p.isalpha()}')
print(f'ascii: {p.isascii()} \ndigit: {p.isdigit()} \ndecimal: {p.isdecimal()}')
print(f'identifier: {p.isidentifier()}\nlower: {p.islower()} \nnumeric: {p.isnumeric()}')
print(f'printable: {p.isprintable()} \nspace: {p.isspace()} \ntitle: {p.istitle()}')
print(f'input = atual == {type(p)}')