# -*- coding: utf-8 -*-


"""
Escreva um programa que exiba uma lista de opções (menu): 
adição, subtração, divisão, multiplicação e sair. Imprima
a tabuada da operação escolhida. Repita até que a opção
saida seja escolhida.
"""

print(60 * "=")

while True:
    print("""
Menu
1 - Adição
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair
""")

    opção = int(input("Digite uma opção: "))
    if opção == 5:
        break
    elif opção >= 1 and opção < 5:
        num = int(input("Tabuada de: "))
        x = 1

        while x <= 10:
            if opção == 1:
                print("%d + %d = %d" % (num, x, num + x))
            elif opção == 2:
                print("%d - %d = %d" % (num, x, num - x))
            elif opção == 3:
                print("%d * %d = %d" % (num, x, num * x))
            elif opção == 4:
                print("%d / %d = %d" % (num, x, num / x))
            x += 1
    else:
        print("Opção Inválida!")


print(60 * "=")
