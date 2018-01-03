from abc import ABCMeta, abstractmethod

class Expressao(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def calcula(self):
        pass

class Subtracao(Expressao):

    def __init__(self, exp_esquerda, exp_direita):
        self.__exp_esquerda = exp_esquerda
        self.__exp_direita = exp_direita

    @property
    def exp_esquerda(self):
        return self.__exp_esquerda

    @property
    def exp_direita(self):
        return self.__exp_direita

    def calcula(self):
        return self.__exp_esquerda.calcula() - self.__exp_direita.calcula()

    def aceita(self, visitor):
        visitor.visita_subtracao(self)

class Soma(Expressao):

    def __init__(self, exp_esquerda, exp_direita):
        self.__exp_esquerda = exp_esquerda
        self.__exp_direita = exp_direita

    @property
    def exp_esquerda(self):
        return self.__exp_esquerda

    @property
    def exp_direita(self):
        return self.__exp_direita

    def calcula(self):
        return self.__exp_esquerda.calcula() + self.__exp_direita.calcula()

    def aceita(self, visitor):
        visitor.visita_soma(self)

class Numero(Expressao):

    def __init__(self, numero):
        self.__numero = numero

    def calcula(self):
        return self.__numero

    def aceita(self, visitor):
        visitor.visita_numero(self)

if __name__ == '__main__':

    from impressao import Impressao

    e_dir = Soma(Numero(1), Numero(1))
    e_esq = Subtracao(Numero(9), Numero(8))
    conta = Soma(e_dir, e_esq)
    
    # print(conta.calcula())

    e_dir2 = Soma(Numero(2), Numero(2))
    e_esq2 = Subtracao(Numero(12), Numero(7))
    conta2 = Soma(e_dir2, e_esq2)

    impressao = Impressao()

    total = Soma(conta, conta2)
    total.aceita(impressao)
    