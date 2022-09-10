
city = input('Digite seu nome inteiro: ')

def Modnum(nome):
    
    nome = nome.lower()
    
    if str(nome).find('silva') == 0:
        return print(True)
    return print(False)
    
    

Modnum(city)