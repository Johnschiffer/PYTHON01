def SeuNome():
    nome = []
    notas = []

    for i in range(2):
        nome.append(input("Digite seu nome: "))
        notas.append(input(f'Digite sua idade: '))

    posicao = notas.index(min(notas))
    
    print(f'{nome[posicao]} é o mais novo com idade {min(notas)} anos.')
    return

SeuNome()