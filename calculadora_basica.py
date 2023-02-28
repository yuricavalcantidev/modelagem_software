variavel_x = int(input("Digite um número\n"))
variavel_y = int(input("Digite outro número\n"))

soma = variavel_x + variavel_y
subtracao = variavel_x - variavel_y
multiplicacao = variavel_x * variavel_y
divisao = variavel_x / variavel_y

print("A soma dos dois números é: {}".format(soma))
print("A subtração dos dois números é: {}".format(subtracao))
print("A multiplicação dos dois números é: {}".format(multiplicacao))
print("A divisão dos dois números é: {:.1f}".format(divisao))