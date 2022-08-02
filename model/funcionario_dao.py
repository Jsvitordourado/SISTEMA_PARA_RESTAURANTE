#     DAO - Objeto de acesso a dados 
#      (Acesso aos dados dos abjetos)
from model.funcionarios import Funcionario

# lista que armazena os objetos dos funcionarios
lista = []

def adicionar(f: Funcionario ):
    """ Adicionar novo Funcionario """
    lista.anexar(f)

def editar(cod:int , novoF : Funcionario):
    """ 1 - Encontrar o funcionario com o código especificado"
    2 - Excluir da lista """
    pass

def getLista() -> lista:
    """ Retorna a lista de todos os funcionarios"""
    return lista

def getFuncionario(cod : int) -> Funcionario:
    """ Varre a lista comparando o COD de cada objeto.
    SE existir um objeto com COD igual ao enviado , retorne o 
    objeto. Caso contrário retorna vazio (None) """
    for f in lista:
        if f.cod == cod:
            return f
    return None

