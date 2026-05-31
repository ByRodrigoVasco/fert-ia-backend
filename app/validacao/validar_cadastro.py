import os
import json

#carrega os usuarios do arquivo usuarios.txt
def carregar_usuarios(caminho_arquivo: str) -> list[dict]:
    if not os.path.exists(caminho_arquivo):
        return []

    usuarios = []
    with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha:
                try:
                    usuarios.append(json.loads(linha))
                except json.JSONDecodeError:
                    print(f"Aviso: linha inválida ignorada: {linha}")
    return usuarios

#compara o email com os outros emails para n salvar usuarios com emails duplicados
def email_existe(email: str, caminho_arquivo: str) -> bool:
    usuarios = carregar_usuarios(caminho_arquivo)
    for usuario in usuarios:
        if usuario.get("email") == email:
            return True
    return False

#compara o id com os outros ids para n salvar usuarios com ids duplicados
def id_existe(id: int, caminho_arquivo: str) -> bool:
    usuarios = carregar_usuarios(caminho_arquivo)
    for usuario in usuarios:
        if usuario.get("id") == id:
            return True
    return False
