from app.crud_cadastro.cadastro import create_cadastro
from app.write.write_cadastro import salvar_usuario

def main():
    #testando funcao de salvar/cadastrar usuario
    salvar_usuario(create_cadastro())

try:
    main()
except Exception as e:
    print("Deu ruim!")
    print(f"Error: {e}")
