'''salvar_usuario(usuario, caminho_arquivo)
Recebe um dicionário com os dados do usuário, carrega a lista atual, adiciona o
 novo usuário e salva tudo de volta no arquivo.

atualizar_senha(email, nova_senha, caminho_arquivo)
Percorre a lista de usuários e atualiza a senha do usuário com o email informado. 
Salva a lista atualizada no arquivo e retorna True se encontrou o usuário, False 
caso contrário.

deletar_usuario(email, caminho_arquivo)
Remove da lista o usuário com o email informado e salva a lista atualizada no arquivo. 
Retorna True se removeu alguém, False se o email não foi encontrado.'''

import json
import os
from app.validacao.validar_cadastro import carregar_usuarios, email_existe

def salvar_usuario(usuario: dict, caminho_arquivo: str) -> bool:
    os.makedirs(os.path.dirname(caminho_arquivo), exist_ok = True)
    if email_existe(usuario["email"], caminho_arquivo):
        print("Email já cadastrado!")
        return False
    with open(caminho_arquivo, "a") as arquivo:
        arquivo.write(json.dumps(usuario) + "\n")
    return True

def atualizar_senha(email: str, nova_senha: str, caminho_arquivo: str) -> bool:
    usuarios = carregar_usuarios(caminho_arquivo)
    encontrou = False
    for usuario in usuarios:
        if usuario.get("email") == email:
            usuario["senha"] = nova_senha
            encontrou = True
            break
    if not encontrou:
        return False
    with open(caminho_arquivo, "w") as arquivo:
        for u in usuarios:
            arquivo.write(json.dumps(u) + "\n")
    return True

def deletar_usuario(email: str, caminho_arquivo: str) -> bool:
    usuarios = carregar_usuarios(caminho_arquivo)
    usuarios_restantes = [u for u in usuarios if u.get("email") != email]
    if len(usuarios) == len(usuarios_restantes):
        return False
    with open(caminho_arquivo, "w") as arquivo:
        for usuario in usuarios_restantes:
            arquivo.write(json.dumps(usuario) + "\n")
    return True
