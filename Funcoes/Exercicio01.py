def ProgramaInf():
    lista = ['Peppa Piga', 'Tom e Jerry', 'Pica-Pau']
    print(lista)
    return

def ListaCarros():
    lista1 = [
        {
            "Modelo":"Jeep Renagade",
            "Preço":1500000
        }, 
        {
            "Modelo":"Tesla",
            "Preço":50000000
        }, 
        {
            "Modelo":"Ferrari",
            "Preço":100000000
        },
        {
            "Modelo":"Uno",
            "Preço":100000000
        }
    ]
    
    for c in lista1:
        print(f'{c["Preço"]} ')
    
    return


idade = int(input("Digite sua idade:"))

if idade < 10:
   ProgramaInf()

else:
    ListaCarros()

