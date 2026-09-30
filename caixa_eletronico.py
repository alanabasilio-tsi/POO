from contaBancaria import ContaBancaria

import errosDeConta

while True:
    try:
        print("MENU")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = input()

        match opcao:

            case 1:
                print("Saldo da conta:" ,contaBancaria.saldo)

            case 2:
                valor = float(input('Digite o valor para depositar:' ,contaBancaria.depositar))

            case 3:
                valor = float(input('Digite o valor para sacar:' ,contaBancaria.sacar))

            case 4:
                print("Fim do programa")
                break

    except OpcaoInvalidaError as erro:
            print(erro)

    except ValorInvalidoError as erro:
        print(erro)

    except SaldoInsuficienteError as erro:
        print(erro)

    except LimiteExcedidoError as erro:
        print(erro)