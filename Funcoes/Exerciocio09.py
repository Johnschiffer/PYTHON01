# Usuario digitara o nome e a media de cinco alunos
# O progrma só aceitará a media do aluno caso ela esteja entre zero e dez

lista = []
def Alunos():
    for i in range(2):
        Nome = input("Digite seu nome: ")
        Media = float(input("Digite sua média: "))
        
        while Media <0 or Media > 10:
            Media = float(input("Digite uma média valida: "))
        
        lista.append({"Nome":Nome, "Media":Media})

Alunos()
print(lista)