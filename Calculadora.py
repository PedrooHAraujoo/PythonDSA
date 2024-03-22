import math


def soma(nu1, nu2):
    resultado = nu1 + nu2
    return f'{nu1} + {nu2} = {resultado}'


def sub(nu1, nu2):
    resultado = nu1 - nu2
    return f'{nu1} - {nu2} = {resultado}'


def mult(nu1, nu2):
    resultado = nu1 * nu2
    return f'{nu1} x {nu2} = {resultado}'


def div(nu1, nu2):
    if nu2 == 0:
        return 'Não é possíel fazer divisão por zero.'
    else:
        resultado = nu1 / nu2
        resto = nu1 % nu2
        print(f'{nu1} / {nu2} = {resultado} e o resto da divisão é {resto}')


def pot(nu1, nu2):
    resultado = math.pow(nu1, nu2)
    return f'{nu1} elevado a {nu2} = {resultado}'


def raiz(nu1):
    resultado = math.sqrt(nu1)
    return f'A raiz de {nu1} = {resultado}'


def main():
    while True:
        print('Bem Vindo a sua Calculadora! \n Digite a Opção desejada: \n 1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Potenciação \n 6 - Radiciação')
        opcao = int(input('1/2/3/4/5/6 '))
        if opcao in [1, 2, 3, 4, 5]:
            n1 = float(input('Digite o seu primeiro número: '))
            n2 = float(input('Digite o seu segundo número: '))
            if opcao == 1:
                print(soma(n1, n2))
            elif opcao == 2:
                print(sub(n1, n2))
            if opcao == 3:
                print(mult(n1, n2))
            elif opcao == 4:
                print(div(n1, n2))
            if opcao == 5:
                print(pot(n1, n2))
        elif opcao == 6:
            n1 = float(
                input('Digite um número para saber a raiz quadrada dele: '))
            print(raiz(n1,))
        else:
            print("Essa opção não é válida")
        continuar = input('Deseja fazer alguma outra operação? (sim/não)')
        if continuar.upper() != 'SIM':
            break
if __name__ == '__main__':
    main()