# Construa um programa onde o usuario diitara dez numeros
# e o programa somara e calculara a media dos numeros digitados.

Nums = []
Soma = 0
for i in range(10):
    Nums.append(int(input("Digite um numero: ")))
    Soma += Nums[i]
    
print(f'Soma: {Soma} \nMédia: {Soma / len(Nums)}')
    