""" ARQUIVO PRINCIPAL """
# imports as classes fncionarios para dentro do main.py
from model.funcionarios import Funcionario
import model.funcionario_dao as f_dao
from model.pratos import Pratos
import model.pratos as p_dao

#cria os objetos
f1 = Funcionario(0, 'joão')
f2 = Funcionario(1, 'joaquim')
f3 = Funcionario(2, 'matheus')
f4 = Funcionario(3, 'pedro')

#adiciona na lista
f_dao.adicionar(f1)
f_dao.adicionar(f2)
f_dao.adicionar(f3)
f_dao.adicionar(f4)

#imprime
lista_func = f_dao.getLista()
for func in lista_func:
    func.print()

print('-----')
#busca pelo codigo 
func = f_dao.getFuncionario(3)
if func != None:
    func.print()
else:
    print('Funcionario não encontrado.')

#editar
novoF = Funcionario(None, 'vitoria')
f_dao.editar(2, novoF)

p1 = Pratos(0, 'Hanburg')
p2 = Pratos(1, 'misto')
p3 = Pratos(2, 'x-burg')
p4 = Pratos(3, 'americano')
p5 = Pratos(4, 'big')

f_dao.adicionar(p1)
f_dao.adicionar(p2)
f_dao.adicionar(p3)
f_dao.adicionar(p4)
f_dao.adicionar(p5)

lista_punc = p_dao.get.lista()
for punc in lista_punc:
    punc.print