metodo = input('Qual o método que deseja utilizar? (soma, sub, mult, div)')
if metodo == 'soma':
    resultado = float(input('Qual o seu primeiro número? ')) + float(input('Qual o seu segundo número?'))
    print('A soma dos numeros escolhidos são:', resultado)
elif metodo == 'sub':
    resultado = float(input('Qual o seu primeiro número? ')) - float(input('Qual o seu segundo número?'))
    print('A subtracao dos numeros escolhidos são:', resultado)
if metodo == 'mult':
    resultado = float(input('Qual o seu primeiro número? ')) * float(input('Qual o seu segundo número?'))
    print('A multiplicacao dos numeros escolhidos são:', resultado)
elif metodo == 'div':
    resultado = float(input('Qual o seu primeiro número? ')) / float(input('Qual o seu segundo número?'))
    print('A divisao dos numeros escolhidos são:', resultado)
else:
    print('Esse metodo nao é valido!')