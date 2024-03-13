metodo = input('Qual o método que deseja utilizar? (soma, sub, mult, div)')
if metodo == 'soma':
    soma = float(input('Qual o seu primeiro número? ')) + float(input('Qual o seu segundo número?'))
    print('A soma dos numeros escolhidos são:', soma)
elif metodo == 'sub':
    sub = float(input('Qual o seu primeiro número? ')) - float(input('Qual o seu segundo número?'))
    print('A subtracao dos numeros escolhidos são:', sub)
if metodo == 'mult':
    mult = float(input('Qual o seu primeiro número? ')) * float(input('Qual o seu segundo número?'))
    print('A multiplicacao dos numeros escolhidos são:', mult)
elif metodo == 'div':
    div = float(input('Qual o seu primeiro número? ')) / float(input('Qual o seu segundo número?'))
    print('A divisao dos numeros escolhidos são:', div)
    