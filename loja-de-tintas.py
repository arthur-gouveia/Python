# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:10:44 2016

@author: arthur-gouveia

Faça um programa para uma loja de tintas

O programa deverá pedir o tamanho em metros quadrados da áera a ser pintada.
Considere que a cobertura de tinta é um litro para cada 6 metros quadrados e
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
de 4 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos
preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 4 litros;
    misturar latas e galões, de forma que o preço seja o menor

Acrescente 10% de folga e sempre arredonde para cima, isto é, considere latas
cheias
"""
import math


def loja_tintas():
    volume_lata = 18
    volume_galão = 4
    preço_lata = 80
    preço_galão = 25
    rendimento = 6

    área = int(input("Informe a área a ser pintada em m²: "))
    área *= 1.1

    litros_necessários = área / rendimento

    latas = math.ceil(litros_necessários / volume_lata)
    galões = math.ceil(litros_necessários / volume_galão)
    preço_latas = latas * preço_lata
    preço_galões = galões * preço_galão

    str_latas = "latas" if (latas > 1) else "lata"
    str_galões = "galões" if (galões > 1) else "galão"

    print("Para pintar uma área total (+10%) de {:5.2f}m² são necessários \
    {:5.3f} litros de tinta.".format(área, litros_necessários))
    print("Para isso você pode comprar {} {} a R${:5.2f}".format(latas,
          str_latas, preço_latas), end=' ')
    print("ou então {} {} a R${:5.2f}".format(galões, str_galões,
          preço_galões))

    if (latas > 1):
        latas_combinadas = math.floor(litros_necessários / volume_lata)
        área_coberta = latas_combinadas * volume_lata * rendimento
        área_restante = área - área_coberta
        litros_necessários = área_restante / rendimento
        galões_combinados = math.ceil(litros_necessários / volume_galão)
        preço_combinado = latas_combinadas * preço_lata
        preço_combinado += galões_combinados * preço_galão
        str_latas = "latas" if (latas_combinadas > 1) else "lata"
        str_galões = "galões" if (galões_combinados > 1) else "galão"
        if (preço_combinado < preço_galões and preço_combinado < preço_latas):
            print("Outra alternativa é a de comprar {} {} e {} {} a um \
preço total de R${:5.2f}".format(latas_combinadas, str_latas,
                                 galões_combinados, str_galões,
                                 preço_combinado))


def loja_tintas2():
    area = int(input("Digite o tamanho da área: "))

    # Acrescentamos os 10% de folga
    area = area*1.1

    # Agora vamos arredondar a área da seguinte maneira
    excesso = area - int(area)  # aqui estamos pegando as casas decim da area
    area = int(area)  # Aqui retiramos a parte inteira da area

    if excesso > 0:
        area = area + 1  # sempre devemos arredondar para cima

    # Vamos calcular o numero de litros necessários para pintar a casa
    litros = area//6
    if area % 6 > 0:
        litros = litros + 1

    print("Litros necessários:", litros, "\n")

    print("1) comprar apenas latas de 18 litros")
    latas = litros//18
    if litros % 18 > 0:
        latas = latas + 1

    print("Serão necessárias", latas, "latas")
    print("Obteremos", latas*18, "litros")
    print("Total: R$", latas*80)

    print("\n2)Comprar apenas galões de 4 litros")
    galoes = litros//4
    if litros % 4 > 0:
        galoes = galoes + 1

    print("Serão necessárias", galoes, "galoes")
    print("Obteremos", galoes*4, "litros")
    print("Total: R$", galoes*25)

    # Vamos pensar, o preço total por litro pago nas latas é 80/18 ~ 4.44 R$/L
    # enquanto que para o gualão é 25/4 ~ 6.25 R$/L
    # portanto é sempre mais vantajoso comprar o máximo de latas possíveis e
    # o mínimo de galões, desde que o preço desses galoes ñ ultrapasse o preço
    # de uma lata, isto é, o numero de galoes seja menor ou igual a 3 (R$ 75)
    print("\n3)Misturar latas e galões, de forma que o preço seja o menor.")
    latas = litros//18
    galoes = 0
    litros_restantes = litros % 18

    if litros_restantes <= 3*4:
        # Ou seja o numero de galoes necessarios seja menor do que três
        galoes = litros_restantes // 4
    if litros_restantes % 4 > 0:
        galoes += 1
    else:
        latas += 1

    print("Serão necessárias", latas, "latas")
    print("Serão necessárias", galoes, "galoes")
    print("Obteremos", latas*18 + galoes*4, "litros")
    print("Total: R$", galoes*25 + latas*80)
