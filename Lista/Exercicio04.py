# Construa um programa onde usuario digitara dez numeros.
# O programa deve calcular quantos deles sao maiores que dez.

Nums = []
Cont = 0
for i in range(8):
    Nums.append(int(input("Digite um numero: ")))

    if Nums[i] > 10:
        Cont += 1
        print(Nums[i])
print(Cont)
