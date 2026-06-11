import os
from app.crud import (
    validar_senha,
    email_existe,
    salvar_usuario,
    read_cadastro,
    update_cadastro,
    delete_cadastro,
)
from app.sensor import create_sensor_data

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
        try:
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
                usuario = read_cadastro()
                if usuario is not None:
                    menu_logado(usuario)
            elif opcao == "3":
                update_cadastro()
            elif opcao == "4":
                delete_cadastro()
            elif opcao == "0":
                print("Saindo, até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nOperação cancelada. Voltando ao menu principal...")

def menu_logado(usuario):
    print(f"\n=== Bem vindo, {usuario['nome']}! ===")
    while True:
        try:
            print("\n1 - Consultar sensor")
            print("0 - Voltar")
            opcao = input("\nEscolha uma opção: ").strip()
            if opcao == "1":
                create_sensor_data()
            elif opcao == "0":
                print("Voltando ao menu principal...")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except KeyboardInterrupt:
            print("\nVoltando ao menu principal...")
            break

if __name__ == "__main__":
    menu()
