from abc import ABCMeta, abstractmethod

class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass

class FinalizaPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()

class PagaPedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()
