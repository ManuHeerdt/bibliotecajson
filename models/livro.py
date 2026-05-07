#Classe livro
#Esta clsse representa um livro dentro
#do sistema

class Livro:
#construtor
    def __init__(self, titulo, autor, ano):
#atributos privados
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano

#Propriedade (GETTER)
#Permite acessar o titulo mesmo sendo privado
    @property
    def titulo (self):
        return self.__titulo
    
#SETTER
#Permite alterar o titulo com validação
    @titulo.setter
    def titulo(self, novo_titulo):
        if len(novo_titulo) < 2:
            print("Titulo Inválido!")
        else:
            self.__titulo = novo_titulo

#Metodo para mostrar dados

    def exibir(self):
        self.__log()
        print("Titulo: ",self.__titulo)
        print("Autor: ",self.__autor)
        print("Ano: ",self.__ano)
#Metodo privado
    def __log(self):
        print("(LOG) Livro Acessado")

#Converter para dicionario
#necessario para salvar em json

    def para_dict(self):
        return {
            "titulo":self.__titulo,
            "autor":self.__autor,
            "ano":self.__ano,
        }

#metodo estatico
    @staticmethod
    def catergotia_padrao():
        return "Literatura"

