#Desafio 012, Curso em Video.

print('aplicando 5% Desconto')

x = float(input('Preço Atual: '))

print(f'Preço com desconto R${x-(x*(5/100)):.2f}', end=' ')
print(f'você economizou R${x*(5/100):.2f}')
