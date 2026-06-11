import json
import os


# === Helper de caminho ===

def _caminho_arquivo() -> str:
    pasta_data = os.path.join(os.path.dirname(__file__), "..", "data")
    return os.path.join(pasta_data, "usuarios.txt")


# === Carregamento de dados ===

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


# === Validação ===

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


# === Persistência (escrita em arquivo) ===

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


# === Fluxos CRUD (interação com usuário) ===

def read_cadastro():
    print("\n=== Login ===")
    while True:
        email = input("Email: ").strip()
        senha = input("Senha: ").strip()
        try:
            usuario = buscar_usuario(email, senha, _caminho_arquivo())
            if usuario is not None:
                print(f"Login OK! Seja bem vindo, {usuario['nome']}!")
                return usuario
            else:
                print("Email ou senha inválidos.")
        except Exception as e:
            print("Ocorreu um erro!", e)
    return None

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
