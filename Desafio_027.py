
city = input('Digite seu nome inteiro: ')

def Modnum(nome):
    
    nome = nome.lower()
    
    return print(f'Nome inteiro: {nome.title()}\nPrimeiro nome: {nome[:str(nome).find(" ")]}\nÚtimo nome: {nome[str(nome).rfind(" "):]}')
    

Modnum(city)