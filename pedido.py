from datetime import date
from comando import PagaPedido, FinalizaPedido

class Pedido(object):

    def __init__(self, cliente, valor):

        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_finalizacao(self):
        return self.__data_finalizacao

class FilaTrabalho(object):

    def __init__(self):
        self.__comandos = []

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def processa(self):
        for comando in self.__comandos:
            comando.executa()

if __name__ == '__main__':

    pedido1 = Pedido(cliente='Ash', valor=200)
    pedido2 = Pedido(cliente='Brock', valor=340)
    print('Status pedido 1: {}'.format(pedido1.status))

    fila = FilaTrabalho()
    print('Adicionado comandos a fila...')
    fila.adiciona(FinalizaPedido(pedido1))
    fila.adiciona(PagaPedido(pedido1))
    fila.adiciona(FinalizaPedido(pedido2))
    fila.adiciona(PagaPedido(pedido2))
    print('Processando comandos...')
    fila.processa()

    print('Status pedido 1: {}'.format(pedido1.status))