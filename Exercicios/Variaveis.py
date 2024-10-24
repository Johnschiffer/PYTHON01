idade = input("Digite sua idade: ")

altura = input("Digite sua altura: ")

nome = input("Digite seu nome: ")

estudando = input("Está estudando? (S/N)")

if estudando == "S":
    estudando = True
else:
    estudando = False

print(f"Meu nome é {nome} tenho {idade} anos.")