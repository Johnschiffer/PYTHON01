# Value = 3

# match Value:
#     case 1:
#         result = 'one'
    
#     case 2:
#         result = 'Two'
    
#     case 3:
#         result = 'Three'

#     case _:
#         result = 'Default'

# print(result)
Total = 0
Escolha = 0
Total_Pizza = 0
while Escolha != 5:
    print('------ Cardápio ------')
    print(f'1. Calabresa com Cebola R$59.90\n'
          f'2. Camarão com Catupity R$87.90\n'
          f'3. Frango com Requeijão R$69.90\n'
          f'4. Banana com Chocolate R$100.00\n'
          f'5. Finalizar Peido')
    print('-----------------------')

    Escolha = int(input("Escolha a pizza desejada: "))
    match Escolha:
        case 1:
            print("Calabresa com Cebola R$59.90")
            Total += 59.90
            Total_Pizza += 1
    
        case 2:
            print("Camarão com Catupity R$87.90")
            Total += 87.90
            Total_Pizza += 1
    
        case 3:
            print("Frango com Requeijão R$69.90")
            Total += 69.90
            Total_Pizza += 1
    
        case 4:
            print(f" Banana com Chocolate R$100.00")
            Total += 100.00
            Total_Pizza += 1
            

        case 5:
            print(f"Pedido com {Total_Pizza} pizzas no Valor: R${Total}")
            

        case _:
            print("Escolha inválida!")