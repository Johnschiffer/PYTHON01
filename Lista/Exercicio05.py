# Construa um programa onde o usuario digitara 7 numeros e o programa escrevera
# na tela, quantos deles sao pares e impares.

Nums = []
NumsPar = 0
NumsImp = 0
for i in range(7):
    Nums.append(int(input("Digite um numero: ")))

    if Nums[i] %2:
        NumsPar += 1

    else:
        NumsImp += 1

print(f'Numeros pares: {NumsPar}')
print(f'Numeros Impares: {NumsImp}')