class Impressao(object):

    def visita_soma(self, soma):
        print('(', end='')
        soma.exp_esquerda.aceita(self)
        print('+', end='')
        soma.exp_direita.aceita(self)
        print(')', end='')

    def visita_subtracao(self, subtracao):
        print('(', end='')
        subtracao.exp_esquerda.aceita(self)
        print('-', end='')
        subtracao.exp_direita.aceita(self)
        print(')', end='')

    def visita_numero(self, numero):
        print(numero.calcula(), end='')