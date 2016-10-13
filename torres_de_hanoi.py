# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 12:15:15 2016

@author: arthur
"""


class Hanoi:
    def __init__(self, blocks):
        self.nblocks = blocks
        self.movimentos = 0
        self.torres = [list(range(blocks+1)),
                       [0],
                       [0]]

    def muda_torre(self, origem, destino):
        if self.movimento_válido(origem, destino):
            self.torres[destino].append(self.torres[origem].pop(-1))
            self.movimentos += 1
        else:
            print('Movimento inválido. Os blocos devem sempre estar em ordem\
            crescente')

    def movimento_válido(self, origem, destino):
        return self.torres[origem][-1] > self.torres[destino][-1]

    def ganhou(self):
        return len(self.torres[2]) == self.nblocks+1

if __name__ == '__main__':
    while True:
        ndiscStr = input('Número de discos ("q" para sair): ')
        if ndiscStr.upper() == "Q":
            break
        elif ndiscStr.isdigit():
            ndisc = int(ndiscStr)
            hanoi = Hanoi(ndisc)
            while not hanoi.ganhou():
                for i in range(3):
                    print('Torre {}: {}'.format(i+1, hanoi.torres[i]))
                print('Entre com o próximo movimento: ')
                origem = int(input('Torre de origem [1-3]: '))
                destino = int(input('Torre de destino [1-3]: '))
                hanoi.muda_torre(origem-1, destino-1)
            print('Ganhou com {} movimentos!!!'.format(hanoi.movimentos))
            if (hanoi.movimentos == ((2**hanoi.nblocks)-1)):
                print('Jogo perfeito!!!!!!!!!!!')
            for i in range(3):
                print('Torre {}: {}'.format(i+1, hanoi.torres[i]))
        else:
            print('Digite um número inteiro ou "Q" para sair.')
            continue
