'''create_cadastro()
Solicita nome, email e senha via input(). Valida a senha com validar_senha() e 
retorna um dicionário com os dados do novo usuário.

menu()
Exibe um menu em loop com as seguintes opções, chamando a função correspondente a 
cada escolha:

1 — Cadastrar: chama create_cadastro() e passa o resultado para salvar_usuario()
2 — Login: chama read_cadastro()
3 — Mudar senha: chama update_cadastro()
4 — Excluir conta: chama delete_cadastro()
0 — Sair: encerra o programa

O menu deve continuar aparecendo até que o usuário escolha a opção 0. Entradas
 inválidas devem exibir uma mensagem de erro e repetir o menu.'''

import os
from app.validacao.validar_cadastro import validar_senha, email_existe
from app.write.write_cadastro import salvar_usuario
from app.cadastro import read_cadastro, update_cadastro, delete_cadastro

def _caminho_arquivo() -> str:
    pasta_data = os.path.join(os.path.dirname(__file__), "data")
    return os.path.join(pasta_data, "usuarios.txt")

def create_cadastro() -> dict:
    print("\n=== Cadastrar ===")
    nome = input("Nome: ").strip()
    while True:
        email = input("Email: ").strip()
        if not email_existe(email, _caminho_arquivo()):
            break
        print("Email já cadastrado. Tente outro.")

    while True:
        senha = input("Senha com 6 caracteres: ").strip()
        if validar_senha(senha):
            break
        print("Senha muito curta. Tente novamente.")
    return {"nome": nome, "email": email, "senha": senha}

def menu():
    print("\n=== Sistema de Cadastro ===")
    while True:
        print("\n1 - Cadastrar")
        print("2 - Login")
        print("3 - Mudar senha")
        print("4 - Excluir conta")
        print("0 - Sair")
        opcao = input("\nEscolha uma opção: ").strip()
        if opcao == "1":
            usuario = create_cadastro()
            ok = salvar_usuario(usuario, _caminho_arquivo())
            if ok:
                print(f"Usuario {usuario['nome']} cadastrado com sucesso!")
        elif opcao == "2":
            read_cadastro()
        elif opcao == "3":
            update_cadastro()
        elif opcao == "4":
            delete_cadastro()
        elif opcao == "0":
            print("Saindo, até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
