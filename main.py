#SISTEMA DO LOOP
while True:
    print("=== MENU ===")
    print("1 - Cadastrar")
    print("2 - Atualizar senha")
    print("3 - Listar usuários")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

#SISTEMA DE FUNÇÕES 

    if opcao == "1":
        print("Cadastrar usuário")

    elif opcao == "2":
        print("Atualizar senha")

    elif opcao == "3":
        print("Listar usuários")

    elif opcao == "4":
        print("Encerrando sistema...")
        break

    else:
        print("Opção inválida!")
      
