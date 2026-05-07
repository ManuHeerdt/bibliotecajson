#Arquivo principal sistema
from models.livro import Livro
from services.biblioteca_service import carregar_livro, salvar_livros

livros = carregar_livro()

print("===============================")
print("=====SISTEMA DE BIBLIOTECA=====")
print("===============================")

print("Categoria padrão: ",Livro.catergotia_padrao())

while True:
    print("\nMENU")
    print("1- Cadastrar livros")
    print("2- Listar livros")
    print("3- Alterar livros")
    print("4- Sair")

    opcao = input("Escolha uma opção: ")

    #cadastrar livro

    if opcao == "1":
        print("\nCadastro de Livro")

        titulo = input("Titulo: ")
        autor = input("Autor: ")
        ano = input("Ano: ")

        livro = Livro(titulo, autor, ano)
        livros.append(livro)
        salvar_livros(livros)
        print("Livro Cadastrado!")

    elif opcao == "2":
        print("\n Lista de Livros")
        if len(livros) == 0:
            print("Nenhum livro cadastrado")
        else:
            for i , livro in enumerate(livros):
                print("Livro",i)
                livro.exibir()



    elif opcao == "3":
        for i, livro in enumerate(livros):
            print(i,'-', livro.titulo)
        pos = int(input(" Escolha o número do livro"))
        novo = input("Novo Título: ")
        livros[pos].titulo = novo
        salvar_livros(livros)

    elif opcao == "4":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida.")