
#função que cria um cadastro de usuario
def create_cadastro():
    print("Create Cadastro")
    nome = input("Digite seu nome completo: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    usuario = {
        "nome": nome,
        "email": email,
        "senha": senha
    }

    return usuario

def read_cadastro():
    print("Read Cadastro")
    pass

def update_cadastro():
    print("Update Cadastro")
    pass

def delete_cadastro():
    print("Delete Cadastro")
    pass
