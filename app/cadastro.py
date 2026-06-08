'''read_cadastro()
Solicita ao usuário email e senha via input(). Chama buscar_usuario() e 
exibe uma mensagem de boas-vindas se o login for bem-sucedido, ou uma mensagem 
de erro caso contrário.

update_cadastro()
Solicita email e senha atual via input(). Confirma a identidade do usuário com
 buscar_usuario(). Se confirmado, solicita a nova senha, valida com validar_senha()
   e chama atualizar_senha().

delete_cadastro()
Solicita email e senha via input(). Confirma a identidade com buscar_usuario(). 
Se confirmado, chama deletar_usuario() e exibe mensagem de confirmação.'''

import os
from app.validacao.validar_cadastro import buscar_usuario, validar_senha
from app.write.write_cadastro import atualizar_senha, deletar_usuario

def _caminho_arquivo() -> str:
    pasta_data = os.path.join(os.path.dirname(__file__), "..", "data")
    return os.path.join(pasta_data, "usuarios.txt")

def read_cadastro():
    print("\n=== Login ===")
    while True:
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        try:
            usuario = buscar_usuario(email, senha, _caminho_arquivo())
            if usuario is not None:
                print(f"Login OK! Seja bem vindo, {usuario["nome"]}!")
                break
            else:
                print("Email ou senha inválidos.")
        except Exception as e:
            print("Ocorreu um erro!", e)

def update_cadastro():
    print("\n=== Mudar Senha ===")
    while True:
        email = input("Email: ").strip()
        senha_atual = input("Senha atual: ").strip()
        usuario = buscar_usuario(email, senha_atual, _caminho_arquivo())
        if usuario is not None:
            break
        print("Email ou senha inválidos. Tente novamente.")
    while True:
        nova_senha = input("Insira nova senha: ").strip()
        if not validar_senha(nova_senha):
            print("Senha muito curta. Mínimo de 6 caracteres.")
        elif nova_senha == senha_atual:
            print("A nova senha não pode ser igual à senha atual.")
        else:
            break
    try:
        ok = atualizar_senha(email, nova_senha, _caminho_arquivo())
        if ok:
            print("Senha atualizada com sucesso!")
        else:
            print("Não foi possível atualizar a senha.")
    except Exception as e:
        print("Ocorreu um erro!", e)

def delete_cadastro():
    print("\n=== Excluir conta ===")
    while True:
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        caminho_arquivo = _caminho_arquivo()
        usuario = buscar_usuario(email, senha, caminho_arquivo)
        if usuario is not None:
            break
        print("Email ou senha inválidos. Tente novamente.")
    try:
        ok = deletar_usuario(email, caminho_arquivo)
        if ok:
            print("Conta excluída com sucesso!")
        else:
            print("Não foi possível excluir a conta.")
    except Exception as e:
        print("Ocorreu um erro!", e)
