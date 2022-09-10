
num = input('Digite seu nome inteiro: ')

def Modnum(nome):
    
    Unidade = nome[3]
    
    Dezena = nome[2]
    
    Centena = nome[1]
    
    Milhar = nome[0]
    
    return print(f'Unidade:{Unidade}\nDezena:{Dezena}\nCentena:{Centena}\nMilhar:{Milhar}')
    
    
    

Modnum(num)