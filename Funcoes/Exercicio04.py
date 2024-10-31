def NomeCidade(Cidade):
    if Cidade == 'Rio de Janeiro':
        return f'Seja Bem-Vindo à Cidade Maravilhosa!'
    
    else:
        return f'Seja Bem-Vindo à {Cidade}!'
    

Nome = input("Digite seu nome: ")
SuaCidade = input("Digite sua cidade:")
print(f'{Nome}, {NomeCidade(SuaCidade)}')

