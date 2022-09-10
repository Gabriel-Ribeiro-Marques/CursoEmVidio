
from gettext import find


nomes = input('Digite seu nome inteiro: ')

def ModName(nome):
    
    maxs = str(nome).title()
    
    mins = str(nome).lower()
    
    quant = len(str(nome).strip())
    
    fi = len(range(0, str(nome).find(' ')))
    
    
    
    return print(f'{maxs}\n{mins}\n{quant}\n{fi}')
    
    
    

ModName(nomes)