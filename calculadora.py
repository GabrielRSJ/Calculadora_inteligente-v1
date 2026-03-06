from time import sleep
import math
#menu de opções da calculadora
while True:
    print('-='*35)
    print('''    [  1 ] media escolar
    [  2 ] soma
    [  3 ] subtração
    [  4 ] multiplicação
    [  5 ] divisão
    [  6 ] radiciação/raiz quadrada
    [  7 ] potência
    [  8 ] fatoração
    [  9 ] seno
    [ 10 ] cosseno
    [ 11 ] finalizar''')
    print('-=' * 35)
    menu = int(input('digite sua opcao: '))

    #sistema de media de escolar
    if menu == 1:
        qtd = int(input('quantas notas: '))
        if qtd <= 1:
            print('opcao invalida')
        else:
            cont = 0
            soma = 0
            while cont < qtd:
                nota = float(input('digite a nota: '))
                cont += 1
                soma += nota
            print(f'{cont} notas digitadas, a media foi de {soma/cont:.2f}')
            sleep(2)

    #sistema de soma
    elif menu == 2:
        qtd = int(input('quantos numeros você quer somar: '))
        cont = 0
        soma = 0
        while cont < qtd:
            numero = int(input('digite o numero: '))
            cont += 1
            soma += numero
        print(f'{cont} numeros digitados, a soma dos numeros foi: {soma}')
        sleep(2)

    #sistema de subtração
    elif menu == 3:
        qtd = int(input('Quantos numeros você quer subtrair: '))
        cont = 0
        sub = 0
        while cont < qtd:
            numero = int(input('digite o numero: '))
            cont += 1
            if cont == 1:
                sub = numero
            else:
                sub -= numero
        print(f'{cont} numeros digitados, a subtração dos numeros foi: {sub}')
        sleep(2)

    #Sistema de mutiplicação
    elif menu == 4:
        qtd = int(input('quantos numeros você quer mutiplicar: '))
        cont = 0
        multi = 1
        while cont < qtd:
            numero = int(input('digite o numero que você quer multiplicar: '))
            cont += 1
            multi *= numero
        print(f'{cont} numeros digitados, a mutiplicação dos numeros foi: {multi}')
        sleep(2)

    #Sistema de Divisão
    elif menu == 5:
        qtd = int(input('quantos numeros você quer dividir: '))
        cont = 0
        divi = 0
        while cont < qtd:
            numero = float(input('digite o numero que você quer dividir: '))
            cont += 1
            if cont <= 1 and numero == 0:
                while True:
                    print('erro!!!!')
                    numero = float(input('digite o numero novamente: '))
                    if numero != 0:
                        break
            else:
                if cont == 1:
                    divi = numero
                else:
                    divi /= numero
        print(f'{cont} numeros digitados, a divisão dos numeros foi: {divi}')
        sleep(2)

    #Sistema de radiciação
    elif menu == 6:
        n = float(input('qual numero você quer saber a raiz: '))
        while True:
            if n <= 0:
                n = float(input('qual numero você quer saber a raiz: '))
            else:
                break
        print(f'A raiz de {n} é {math.sqrt(n):.2f}')
        sleep(2)

    #Sistema de Potencia
    elif menu == 7:
        n = float(input('Digite o numero que você quer elevar: '))
        expo = float(input('Digite o expoente: '))
        potencia = n ** expo
        print(f'Você elevou {n} a {expo}, resultado é {potencia:.2f}')
        sleep(2)

    #Sistema de fatorar
    elif menu == 8:
        n = int(input('Digite o numero que você quer fatorar: '))
        while True:
            if n <= 0:
                n = float(input('Digite o numero que você quer fatorar: '))
            else:
                break
        for c in range(n, 0, -1):
            print(f'{c} ', end = '')
            if c == 1:
                print('=', end = ' ')
            else:
                print('x', end = ' ')
        print(math.factorial(n))
        sleep(2)

    #Sistema de seno
    elif menu == 9:
        n = float(input('Qual numero você quer saber o seno: '))
        print(f'O seno de {n} é {math.sin(math.radians(n)):.2f} ')
        sleep(2)

    #Sistema de cosseno
    elif menu == 10:
        n = float(input('Qual numero você quer saber o cosseno: '))
        print(f'O cosseno de {n} é {math.cos(math.radians(n)):.2f} ')
        sleep(2)

    elif menu == 11:
        break

