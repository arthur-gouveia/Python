# Exercício 6.2


def ex6_2():
    """ Exercício 6.2

    Reúne duas listas e imprime a junção de ambas
    """
    key = ''
    index = 1
    list1 = []
    list2 = []

    print('Entre com os valores da primeira lista. Digite "p" para parar.')
    while key != 'p':
        key = input('Entre com o %d° item da lista: ' % index)
        try:
            list1.append(int(key))
            index += 1
        except ValueError:
            if key != 'p':
                print('Valor inválido. Tente novamente')

    key = ''
    index = 1
    print('Entre com os valores da segunda lista. Digite "p" para parar.')
    while key != 'p':
        key = input('Entre com o %d° item da lista: ' % index)
        try:
            list2.append(int(key))
            index += 1
        except ValueError:
            if key != 'p':
                print('Valor inválido. Tente novamente')

    print('União das duas listas\n', list1+list2)

# Exercício 6.3


def ex6_3():
    """
    Exercício 6.3

    Lê duas listas e reúne ambas removendo elementos duplicados
    """
    key = ''
    index = 1
    list1 = []
    list2 = []

    print('Entre com os valores da primeira lista. Digite "p" para parar.')
    while key != 'p':
        key = input('Entre com o %d° item da lista: ' % index)
        try:
            list1.append(int(key))
            index += 1
        except ValueError:
            if key != 'p':
                print('Valor inválido. Tente novamente')

    key = ''
    index = 1
    print('Entre com os valores da segunda lista. Digite "p" para parar.')
    while key != 'p':
        key = input('Entre com o %d° item da lista: ' % index)
        try:
            list2.append(int(key))
            index += 1
        except ValueError:
            if key != 'p':
                print('Valor inválido. Tente novamente')

    list1 += list2
    list2 = []

    for item in list1:
        if item not in list2:
            list2.append(item)

    print('União das listas removendo duplicados\n', list2)


def ex6_5():
    último = 10
    fila = list(range(1, último + 1))
    print("\nExistem %d clientes na fila" % len(fila))
    print("Fila atual:", fila)
    print("Digite uma sequência de movimentos na fila.")
    print("F adiciona um cliente ao fim da fila e A realiza o atendimento.")
    operação = input("Operações: ")
    i = 0
    while i < len(operação):
        if operação[i].upper() == "A":
            if(len(fila)) > 0:
                atendido = fila.pop(0)
                print("Cliente %d atendido" % atendido)
                print("Fila: ", fila)
            else:
                print("Fila vazia! Ninguém para atender...")
                # break
        elif operação[i].upper() == "F":
            último += 1  # Incrementa o ticket do novo cliente
            fila.append(último)
        elif operação.upper() == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A ou S!")
        i += 1
    print(fila)


def ex6_6():
    último1 = 10
    último2 = 7
    fila1 = list(range(1, último1 + 1))
    fila2 = list(range(1, último2 + 1))
    print("\nExistem %d clientes na fila 1" % len(fila1))
    print("Fila 1 atual:", fila1)
    print("\nExistem %d clientes na fila 2" % len(fila2))
    print("Fila 2 atual:", fila2)
    print("Digite uma sequência de movimentos nas filas.")
    print("F adiciona um cliente ao fim da fila 1 e A realiza o atendimento.")
    print("G adiciona um cliente ao fim da fila 2 e B realiza o atendimento.")
    operação = input("Operações: ")
    i = 0
    while i < len(operação):
        if operação[i].upper() == "A":
            if(len(fila1)) > 0:
                atendido = fila1.pop(0)
                print("Cliente {} atendido na fila 1".format(atendido))
                print("Fila 1: ", fila1)
            else:
                print("Fila 1 vazia! Ninguém para atender...")
                # break
        elif operação[i].upper() == "F":
            último1 += 1  # Incrementa o ticket do novo cliente
            fila1.append(último1)
        elif operação[i].upper() == "B":
            if(len(fila2)) > 0:
                atendido = fila2.pop(0)
                print("Cliente {} atendido na fila 2".format(atendido))
                print("Fil a: ", fila2)
            else:
                print("Fila 2 vazia! Ninguém para atender...")
                # break
        elif operação[i].upper() == "G":
            último2 += 1  # Incrementa o ticket do novo cliente
            fila2.append(último2)
        elif operação.upper() == "S":
            break
        else:
            print("Operação inválida! Digite apenas F, A, G, B ou S!")
        i += 1
    print(fila1)
    print(fila2)


def ex6_7():
    expressão = input('Entre uma expressão com parênteses: ')
    pilha = []
    for char in expressão:
        if char == '(':
            pilha.append(char)
        elif char == ')':
            if len(pilha) > 0:
                pilha.pop(-1)

    result = 'Parênteses preenchidos corretamente' if len(pilha) == 0 \
        else 'Parênteses não preenchidos corretamente'

    print(result)


def printmenu():
    print('{:=^28}\n'.format(' MENU '))
    menu = {1: 'Ex. 6.2: Reunir duas listas',
            2: 'Ex. 6.3: Reunir duas listas removendo duplicados',
            3: 'Ex. 6.5: Atendimento de fila no banco',
            4: 'Ex. 6.6: Atendimento de duas filas no banco',
            5: 'Ex. 6.7: Verificação de parênteses'}

    for item in menu:
        print('{}. {}'.format(item, menu[item]))
    return len(menu)


if __name__ == '__main__':

    opção = 'x'
    while True:
        itens = printmenu()
        opção = input(
                'Entre uma opçao [1 a {}] ou S para sair: '.format(itens))
        if opção == '1':
            ex6_2()
        elif opção == '2':
            ex6_3()
        elif opção == '3':
            ex6_5()
        elif opção == '4':
            ex6_6()
        elif opção == '5':
            ex6_7()
        elif opção.upper() == 'S':
            break
        else:
            print('Opção inválida.\nEscolha um item do menu ou S para sair')
