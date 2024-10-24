nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media < 4:
    print(f"Aluno reprovado com média: {media}")

elif media > 7:
    print(f"Aluno aprovado direto com média: {media}")

elif media > 4 and media < 7:
    print(f"Aluno em recuperação com média: {media}")

    media_recupera = float(input("Digite a nota de recuração: "))
    if media_recupera < 5:
        print(f"Você foi Reprovado na recuperação com media: {media_recupera}")
    
    else:
        print(f"Você passou na recuperação com média: {media_recupera}")