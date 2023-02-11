import math
from time import sleep

print(f'Olá, essa aplicação foi desenvolvida para fins educativos.')
print("Essa aplicação é capaz de resolver cálculos de geometria plana, bhaskara e porcentagem de maneira rápida e assertiva.")
print("Use a vontade!!")

def main():
    menu()

def menu():
    print("ESCOLHA O TIPO DE CÁLCULO QUE VOCÊ DESEJA EFETUAR:")
    print("[1] - BHASKARA")
    print("[2] - GEOMETRIA PLANA")
    print("[3] - PORCENTAGEM")
    print("[4] - SAIR DA APLICAÇÃO")
    escolha = int(input("--> "))

    if escolha == 1:
      
        bhaskara()

    elif escolha == 2:
        
        geometria()

    elif escolha == 3:

        porcentagem()
    
    elif escolha == 4:
        print("Certo, até mais tarde!")
        sleep(1)

    else:
        print("Opção inválida, tente outra vez..")
        sleep(2)
        menu()
    

def porcentagem():
    print("=============== Porcentagem ============")

    print("Escolha um Opção")
    print("[1] - Valor para porcentagem")
    print("[2] - sair")
    escolha = int(input("--> "))

    if escolha == 1:
        def valorporcentagem (numero, porcentagem):
            valor = porcentagem/100
            valor2 = numero
            resultado = valor*valor2
            print(f'{valor*100:,.0f}% de {valor2} é {resultado:,.0f}')

        if __name__ == "__main__":
            while True:
                numero = int(input("Digite o valor para tirar o porcentual: "))
                porcentagem = int(input("Digite o porcentual [sem %]: "))
                valorporcentagem(numero, porcentagem)

                continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
                if continua == 'q':
                    break

    elif escolha == 2:
        print("Certo, até a próxima!!")
        exit
        
    else:
        print("Escolha uma opção válida..")
        sleep(2)
        porcentagem()


def bhaskara():
    def raizes(a, b, c):
        d = (b**2 - 4 * a * c)
        x1 = (-b + d ** (1 / 2)) / (2 * a)
        x2 = (-b - d ** (1 / 2)) / (2 * a)

        print('\nValor de Delta: {0}'.format(d))
        print('Valor de x1: {0}'.format(x1))
        print('Valor de x2: {0}'.format(x2))


    if __name__ == '__main__':
        while True:
            print("Calculando as Raizes de Equação de 2º grau\n")
            a = float(input('Entre com o valor de a: '))
            b = float(input('Entre com o valor de b: '))
            c = float(input('Entre com o valor de c: '))
            raizes(a, b, c)

            continua = input("Deseja sair? Digite 'q' ou 'Enter' para novo cálculo: ")
            if continua == 'q':
                break

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
                if continua == 'q':
                    break

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
                if continua == 'q':
                   break

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
                if continua == 'q':
                    break

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
                if continua == 'q':
                    break

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
                if continua == 'q':
                    break

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
                if continua == 'q':
                    break
                break
                    
    if formula == 7:
        print('Saindo, espero ter ajudado!!')
        sleep(2)
        menu()
        
    else:
        print("OK, retornando ao menu!")
        sleep(2)
        geometria()


































if __name__ == "__main__":
    main()
