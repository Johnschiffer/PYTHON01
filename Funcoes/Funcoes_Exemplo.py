def Medias(n1, n2, n3, n4):
    Media = (n1 + n2 + n3 + n4) / 4

    if Media >= 7:
        return "APROVADO"
    
    elif Media < 7 and Media >4:
        return "RECUPERAÇÃO"
    
    else:
        return "REPROVADO"


aprovados = []  
def DefineMedia(nome):
    notas = []
    

    for i in range(4):
        notas.append(float(input(f"Digite a Nota:{i + 1} ")))

    print(f'O Aluno está {nome}: {Medias(notas[0], notas[1], notas[2], notas[3])}')
    aprovados.append(i)



for i in range(5):
    NomeAluno = input("Digite o nome do Aluno: ")
    DefineMedia(NomeAluno)

print(aprovados)