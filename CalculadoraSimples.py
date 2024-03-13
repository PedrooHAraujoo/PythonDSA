metodo = input('Qual o método que deseja utilizar? (soma, sub, mult, div)')
if metodo in ['soma', 'sub', 'mult', 'div']:
    num1 = float(input('Qual o seu primeiro número? '))
    num2 = float(input('Qual o seu segundo número?'))
    if metodo == 'soma':
        resultado = num1 + num2
        print('A soma dos numeros escolhidos são:', resultado)
    elif metodo == 'sub':
        resultado = num1 - num2
        print('A subtracao dos numeros escolhidos são:', resultado)
    elif metodo == 'mult':
        resultado =num1 * num2
        print('A multiplicacao dos numeros escolhidos são:', resultado)
    elif metodo == 'div':
        if num2 != 0:
            resultado = num1 / num2
            print('A divisao dos numeros escolhidos são:', resultado)
        else:
            print('Essa divisao nao pode ser feita, pois nenhum numero pode ser divisivel por zero!')    
else:
    print('Esse metodo nao é valido!')