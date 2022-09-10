
num = int(input('Digite seu nome inteiro: '))

def Modnum(nome):
    
    Unidade = nome // 1 % 10
    
    Dezena = nome // 10 % 10
    
    Centena = nome // 100 % 10
    
    Milhar = nome // 1000 % 10
    
    return print(f'Unidade:{Unidade}\nDezena:{Dezena}\nCentena:{Centena}\nMilhar:{Milhar}')
    
    
    

Modnum(num)