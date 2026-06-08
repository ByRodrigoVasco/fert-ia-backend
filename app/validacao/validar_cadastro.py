'''carregar_usuarios(caminho_arquivo)
Lê o arquivo usuarios.txt e retorna uma lista com todos os usuários cadastrados.
 Se o arquivo não existir, retorna uma lista vazia.

buscar_usuario(email, senha, caminho_arquivo)
Percorre a lista de usuários e retorna o dicionário do usuário cujo email e 
senha correspondam aos informados. Se não encontrar, retorna None.

validar_senha(senha)
Verifica se a senha possui o tamanho mínimo de 6 caracteres. Retorna True se válida,
False caso contrário.'''

import json
import os

def carregar_usuarios(caminho_arquivo: str) -> list:
    if not os.path.exists(caminho_arquivo):
        return []
    usuarios = []
    with open (caminho_arquivo, "r") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                usuarios.append(json.loads(linha))
    return usuarios

def email_existe(email: str, caminho_arquivo: str) -> bool:
    usuarios = carregar_usuarios(caminho_arquivo)
    for usuario in usuarios:
        if usuario.get("email") == email:
            return True
    return False

def buscar_usuario(email: str, senha: str, caminho_arquivo: str) -> dict | None:
    usuarios = carregar_usuarios(caminho_arquivo)
    for usuario in usuarios:
        if usuario.get("email") == email and usuario.get("senha") == senha:
            return usuario
    return None

def validar_senha(senha: str) -> bool:
    tamanho_minimo = 6
    if len(senha) < tamanho_minimo:
        return False
    return True
