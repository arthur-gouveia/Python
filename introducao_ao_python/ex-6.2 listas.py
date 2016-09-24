key = ''
index = 1
list1 = []
list2 = []

print('Entre com os valores da primeira lista. Digite "p" para parar.')
while key != 'sair':
    key = input('Entre com o %d° item da lista: ' %index)
    try:
        list1.append(int(key))
        index += 1
    except ValueError:
        if key != 'p':
            print('Valor inválido. Tente novamente')


key = ''
index = 1
print('Entre com os valores da segunda lista. Digite "p" para parar.')
while key != 'sair':
    key = input('Entre com o %d° item da lista: ' %index)
    try:
        list2.append(int(key))
        index += 1
    except ValueError:
        if key != 'p':
            print('Valor inválido. Tente novamente')
            
            
print('União das duas listas\n', list1+list2)