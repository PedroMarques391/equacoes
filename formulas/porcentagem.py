from time import sleep

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
                if continua != 'q':
                    sleep(1)
                    valorporcentagem(numero, porcentagem)
                else:
                    sleep(1)
                    porcentagem()

    elif escolha == 2:
        print("Certo, até a próxima!!")
        exit
        
    else:
        print("Escolha uma opção válida..")
        sleep(2)
        porcentagem()

porcentagem()


