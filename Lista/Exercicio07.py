# Usuario digitara o nome e a media de dez alunos
# Mostrar na tela o nome e a media de todos acima de 6.

# Nomes = []
# Nums = []

# NomesAprovados = []
# NumsAcima = []
# for i in range(3):
#     Nomes.append(input("Digite o nome do Aluno: "))
#     Nums.append(int(input("Digite a nota do Aluno: ")))

#     if Nums[i] >= 6:
#         NomesAprovados.append(Nomes[i])
#         NumsAcima.append(Nums[i])

# print(NomesAprovados)
# print(NumsAcima)

Nomes = []
Nums = []

# NomesAprovados = []
# NumsAcima = []
for i in range(3):
    Nomes.append(input("Digite o nome do Aluno: "))
    Nums.append(int(input("Digite a nota do Aluno: ")))

    if Nums[i] < 6:
        Nomes.pop()
        Nums.pop()

    else:
        Nomes.append(i)
        Nums.append(i)

print(Nomes)
print(Nums)

