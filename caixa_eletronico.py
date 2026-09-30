from contaBancaria import ContaBancaria

import errosDeConta

class OpcaoInvalidaError (Exception):
    ...

conta = ContaBancaria()

while True:
    try:
        print("MENU")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")
        opcao = int(input("Escolha uma opção: "))

        if opcao not in [1,2,3,4]:
            raise OpcaoInvalidaError ("Opção inválida, escolha novamente")

        match opcao:

            case 1:
                print("Saldo da conta:" ,conta.saldo)

            case 2:
                valor = float(input('Digite o valor para depositar:'))
                conta.depositar(valor)

            case 3:
                valor = float(input('Digite o valor para sacar:' ))
                conta.sacar(valor)

            case 4:
                print("Fim do programa")
                break

    except OpcaoInvalidaError as erro:
        print(erro)

    except ValueError:
        print('Digite apenas números válidos!')

    except errosDeConta.ValorInvalidoError as erro:
        print(erro)

    except errosDeConta.SaldoInsuficienteError as erro:
        print(erro)

    except errosDeConta.LimiteExcedidoError as erro:
        print(erro)