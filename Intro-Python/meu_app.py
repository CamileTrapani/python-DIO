print('Python DIO')
a = 2
b = 3
soma = a + b
print(soma)

c = float(input('Fala um número: '))
d = float(input('Manda outro: '))
soma2 = c + d
print('Soma = {}'.format(soma2))

a = 10
b = 10
c = 10
if a > b or a >= c:
    print('Primeiro afirmação é verdadeira')
elif a == b:
    print('Segunda afirmação é verdadeira')
else:
    print('Nenhuma afirmação é verdadeira')

a = input('Digite o primeito valor: ')
b = input('Digite o primeito valor: ')
soma = a + b
# print('O valor da soma é: {soma}'.format(soma=soma))
tot = 0
for num in range(101):
    div = 0
    for x in range(1, num+1):
        resto = num % x
        if resto == 0:
            div += 1
    if div == 2:
        print('{} é primo'.format(num))
        tot +=1
print(tot)