num = input('Digite seu nome inteiro: ')

def Modnum(nome):
    
    Unidade = str(nome).upper()
    
    Dezena = str(nome).lower()
    
    quant = len(str(nome).strip())
    
    fi = len(range(0, str(nome).find(' ')))
    
    return print(f'{Unidade}\n{Dezena}\n{quant}\n{fi}')
    

Modnum(num)