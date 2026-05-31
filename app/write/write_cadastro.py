import os
import json
from app.validacao.validar_cadastro import email_existe, id_existe

#salva o usuario no arquivo usuarios.txt
def salvar_usuario(usuario: dict, nome_arquivo: str = "usuarios.txt") -> str:
    pasta_data = os.path.join(os.path.dirname(__file__), "..", "..", "data")
    os.makedirs(pasta_data, exist_ok=True)
    caminho_arquivo = os.path.join(pasta_data, nome_arquivo)

    #compara o email com os outros emails para n salvar usuarios com emails duplicados
    if email_existe(usuario["email"], caminho_arquivo):
        print("Erro: email já cadastrado!")
        return None

    novo_id = gerar_id(caminho_arquivo)

    #chama a funçao de comparar o id com os outros ids para n salvar um usuario com id ducplicado
    if id_existe(novo_id, caminho_arquivo):
        print("Erro: ID duplicado!")
        return None

    usuario = {"id": novo_id, **usuario}

    with open(caminho_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write(json.dumps(usuario, ensure_ascii=False) + "\n")

    return os.path.abspath(caminho_arquivo)

#gera um id para cada usuario
def gerar_id(caminho_arquivo: str) -> int:
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return sum(1 for linha in arquivo if linha.strip()) + 1
    return 1

