
import random

lista = ["Pedra", "Papel", "Tesoura"]




Player1 = input("Jogador 1 digite sua jogada: ")
Player2 = random.choice(lista)

if Player1 == Player2:
    print(f"Empate!")

elif ((Player1 == 'Pedra' and Player2 == 'Tesoura') or (Player1 == 'Papel' and Player2 =='Pedra') or (Player1 == 'Tesoura' and Player2 == 'Papel')):
    print(f"Player 1 Venceu! {Player1} vence de {Player2}")


else:
    print(f"Player2 Venceu! {Player2} vence de {Player1}")





