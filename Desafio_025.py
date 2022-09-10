
city = input('Digite seu nome inteiro: ')

def Modnum(nome):
    
    nome = nome.lower()
    
    quant = str(nome).count('a')
    
    lfind = str(nome).find('a')
    
    rfind = str(nome).rfind('a')
    
    return print(f'QUANTOS A:{quant}, Posi_start:{lfind}, Posi_end:{rfind} {len(nome)}')
    

Modnum(city)