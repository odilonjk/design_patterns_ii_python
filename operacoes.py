class Subtracao(object):

    def __init__(self, exp_esquerda, exp_direita):
        self.__exp_esquerda = exp_esquerda
        self.__exp_direita = exp_direita

    def calcula(self):
        return self.__exp_esquerda.calcula() - self.__exp_direita.calcula()

class Soma(object):

    def __init__(self, exp_esquerda, exp_direita):
        self.__exp_esquerda = exp_esquerda
        self.__exp_direita = exp_direita

    def calcula(self):
        return self.__exp_esquerda.calcula() + self.__exp_direita.calcula()


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero

    def calcula(self):
        return self.__numero

if __name__ == '__main__':

    e_dir = Soma(Numero(1), Numero(1))
    e_esq = Subtracao(Numero(9), Numero(8))
    conta = Soma(e_dir, e_esq)
    print(conta.calcula())