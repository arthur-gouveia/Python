import os 

def print_menu(message=''):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('############################## MENU ##############################')
    print('0: Sair')
    print('1: Soma de dois números')
    print('2: Converter metros em milímetros')
    print('3: Converter tempo em segundos')
    print('4: Calcular o reajuste do salário')
    print('5: Calcular o preço com desconto de um produto')
    print('6: Calcular o tempo de viagem')
    print('7: Converter Celsius em Farenheit')
    print('8: Calcular o valor do alguel do veículo')
    print('9: Calcular a redução da expectativa de vida de um fumante')
    if len(message) > 0:
        print(message + '\n')
    return(input('Entre a opção desejada: '))
   
def menu():
    
    opção = print_menu()
    
    while True:
        if opção == '0':
            break
        elif opção == '1':
            soma()
            opção = print_menu()
        elif opção == '2':
            m2mm()
            opção = print_menu()
        elif opção == '3':
            t2s()
            opção = print_menu()
        elif opção == '4':
            aumento()
            opção = print_menu()
        elif opção == '5':
            desconto()
            opção = print_menu()
        elif opção == '6':
            viagem()
            opção = print_menu()
        elif opção == '7':
            c2f()
            opção = print_menu()
        elif opção == '8':
            preço_aluguel()
            opção = print_menu()
        elif opção == '9':
            fumante()
            opção = print_menu()
        else:
            opção = print_menu('Opção inválida.\nTente novamente')

def soma():
    n1 = int(input('Entre o 1º número: '))
    n2 = int(input('Entre o 2º número: '))
    print('A soma dos dois números é %d' %(n1+n2))
    input('Pressione Enter para continuar')
    
def m2mm():
    m = float(input('Entre com uma distância em metros: '))
    print('Distância convertida em mm: %d' %(m*1000))
    input('Pressione Enter para continuar')
    
    
def t2s():
    dias = int(input('Entre com o número de dias: '))
    horas = int(input('Entre com o numero de horas: '))
    minutos = int(input('Entre com o número de minutos: '))
    segundos = int(input('Entre com o número de segundos: '))
    
    t = ((((dias*24 + horas)*60) + minutos)*60 + segundos)
    
    print('O tempo é de %d segundos' %t)
    input('Pressione Enter para continuar')
    
def aumento():
    salário = float(input('Entre com o salário: R$'))
    reajuste = float(input('Entre com o percentual de reajuste: '))
    print('O salário reajustado é R$%5.2f' %(salário*(1+reajuste/100)))
    input('Pressione Enter para continuar')

def desconto():
    preço_original = float(input('Entre com o preço da mercadoria: R$'))
    desc = float(input('Entre com o percentual de desconto: '))
    
    vlr_desc = preço_original * (desc/100)
    preço_final = preço_original - vlr_desc
    
    print('O valor do desconto é R$%5.2f\nO preço após o desconto é R$%5.2f'
          %(vlr_desc, preço_final))
    input('Pressione Enter para continuar')
    

def viagem():
    distância = float(input('Entre com a distância em km: '))
    velocidade = float(input('Entre com a velocidade média prevista (km/h): '))
    
    print('O tempo de viagem é de %5.2f horas' %(distância / velocidade))
    input('Pressione Enter para continuar')


def c2f():
    celsius = float(input('Entre com a temperatura em °C:' ))
    print('A temperatura convertida é de %5.2f°F' %(9*celsius/5+32))
    input('Pressione Enter para continuar')


def preço_aluguel():
    km = float(input('Quantos km rodados: '))
    dias = int(input('Número de dias do aluguel: '))
    
    preço_dia = 60.0
    preço_km = 0.15
    
    print('O valor do alguel é R$%5.2f' %(km*preço_km + dias*preço_dia))
    input('Pressione Enter para continuar')

def fumante():
    cigarros = int(input('Quantos cigarros você fuma por dia? '))
    tempo = int(input('Há quantos anos você fuma? '))
    
    min_por_cigarro = 10
    
    num_cigarros = cigarros*tempo*365
    
    dias_perdidos = num_cigarros*min_por_cigarro/60/24
    
    print('Sua expecativa de vida é de %5.3f dias a menos' %dias_perdidos)
    input('Pressione Enter para continuar')

    
if __name__ == "__main__":
    menu()