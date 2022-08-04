from model.pratos import Pratos

lista = []

def adicionar(f:Pratos):
    lista.anexar(f)

def editar(cod:int, novop:Pratos):
    pass

def getpratos(cod : int):
    for f in lista:
        if f.cod == cod:
            return f
    return None