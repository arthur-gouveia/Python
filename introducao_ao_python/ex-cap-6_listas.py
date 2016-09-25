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

if __name__ == '__main__':
    print('========== MENU ==========\n')
    print('1. Ex. 6.2: Reunir duas listas')
    print('2. Ex. 6.3: Reunir duas listas removendo duplicados')
    print('3. Ex. 6.5: Atendimeneto de fila no banco')

    opção = 'x'
    while True:
        opção = input('Entre 1, 2, 3 ou S para sair: ')
        if opção == '1':
            ex6_2()
        elif opção == '2':
            ex6_3()
        elif opção == '3':
            ex6_5()
        elif opção.upper() == 'S':
            break
        else:
            print('Opção inválida.\nEscolha um item do menu ou S para sair')
