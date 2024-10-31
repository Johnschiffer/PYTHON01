import random

def Game(numero):
    Player2 = random.randint(0, 5)
    print(f'Player 1: {numero} vs Player 2: {Player2}')
    if (numero + Player2) % 2 == 0:
        return 'PAR - Player 1 Venceu!'
    
    else:
        return 'ÍMPAR - Player 2 Venceu!'






print(f'Jogo - Par ou Ímpar\n'
      f'Numeros permiidos - 0, 1, 2, 3, 4 ou 5')
print('-'*40)

Jogadas = int(input('Quantas vezes deseja jogar?'))
for i in range(Jogadas):
    Player1 = int(input("Insira sua jogada: "))
    print(f'{Game(Player1)}')




