import math
from time import sleep



def geometria():
    print('Escolha uma das Fórmulas para calcular figuras planas: ')
    print('[1] - Triângulo')
    print('[2] - Quadrado')
    print('[3] - Retângulo')
    print('[4] - Losango')
    print('[5] - Trapézio')
    print('[6] - Circulo')
    print('[7] - sair')
    formula = int(input('--> '))

    if formula == 1:
        def triangulo(b, h):
            a = b*h/2
            print(f"O resultado da questão é {a}")

        if __name__ == '__main__':
            while True:
                print("Calculando a área do triângulo..\n")
                b = int(input("Digite o valor da base: "))
                h = int(input("Digite o valor da altura: "))
                triangulo(b, h)
                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua != 'q':
                    sleep(1)
                    triangulo(b, h)
                else:
                    sleep(1)
                    geometria()

    elif formula == 2:
        def quadrado(i):
            a = i**2
            print(f'O resultado da questão é {a}')
        
        if __name__ == '__main__':
            while True:
                print("Calculando a área do quadrado..\n")
                i = int(input("Digite a medida da base/altura: "))
                quadrado(i)
                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua != 'q':
                    sleep(1)
                    quadrado(i)
                else:
                    sleep(1)
                    geometria()

    elif formula == 3:
        def retangulo(b, h):
            a = b*h
            print(f"O resultado da questão é: {a}")
        
        if __name__ == '__main__':
            while True:
                print("Calculando a área do retângulo.. \n")
                b = int(input("Digite o valor da base: "))
                h = int(input("Digite o valor da altura: "))
                retangulo(b, h)
                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua != 'q':
                    sleep(1)
                    retangulo(b, h)
                else:
                    sleep(1)
                    geometria()

    elif formula == 4:
        def losango(D, d):
            a = D*d/2
            print(f'O resultado da questão é: {a}')

        if __name__ == '__main__':
            while True:
                print("Calculando a área do Losango.. \n")
                D = int(input("Digite o valor da Diagonal Maior: "))
                d = int(input("Digite o valor da Diagonal Menor: "))
                losango(D, d)
                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua != 'q':
                    sleep(1)
                    losango(D, d)
                else:
                    sleep(1)
                    geometria()

    elif formula == 5:
        def trapezio(B, b, h):
            a = (B+b)*h/2
            print(f"o resultado da questão é: {a}")
        
        if __name__ == '__main__':
            while True:
                print("Calculando a área do Trapézio.. \n")
                B = int(input("Digite o valor da Base Maior: "))
                b = int(input("Digite o valor da Base Menor: "))
                h = int(input("Digite o valor da altura: "))
                trapezio(B, b, h)
                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua != 'q':
                    sleep(1)
                    trapezio(B, b, h)
                else:
                    sleep(1)
                    geometria()

    elif formula == 6:
        def circulo(r):
            a = math.pi*(r**2)
            print(f"O resultado da questão é: {a}")
        
        if __name__ == '__main__':
            while True:
                print("Calculando a área do Circulo.. \n")
                r = int(input("Digite o valor do raio: "))
                circulo(r)
                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua != 'q':
                    sleep(1)
                    circulo(r)
                else:
                    sleep(1)
                    geometria()
                    


    
    if formula == 7:
        print('Saindo, espero ter ajudado!!')
        sleep(2)
        exit
        
    else:
        print("Opção Inválida para o usuário, Tente de novo.")
        sleep(2)
        geometria()

geometria()
    











