#COM WHILE

num = int(input("Digite um numero: "))
contagem = 1

while contagem <= 10:
    print(f'{num} x {contagem} = {num * contagem}')
    contagem += 1

else:
    print("FIM DO WHILE!")




#COM FOR
num_for = int(input("Digite um número: "))

for i in range(1, 11):
    print(f'{num_for} x {i} = {num_for * i}')

else:
    print("FIM DO FOR")