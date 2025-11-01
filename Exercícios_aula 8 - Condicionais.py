# 1* 
# Peça para o usuário digitar um número, verifique se um número é positivo, 
# negativo ou zero.
numero = int(input('Digite um numero: '))
if numero == 0:
    print('O número é 0')
elif numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
# 2*

# Peça para o usuário digitar a idade, verifique se uma pessoa pode votar com 
# base na idade.
ida = int(input('Digite a sua idade: '))
if ida >= 18:
    print('Você é maior de idade, pode votar')
else:
    print('Você não pode votar ainda')

# 3*

# Declara uma variável com um número qualquer, 
# determine se um número é par ou ímpar.
num = int(input('Digite um número: '))
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')

# 4*

# Usuário vai digitar 3  números, para criar um triângulo, verifique se um triângulo 
# é equilátero, isósceles ou escaleno

# Um triângulo é chamado de equilátero se todos os lados possuem a mesma medida. 
# Um triângulo é chamado de isósceles se dois lados possuem a mesma medida. 
# Um triângulo é chamado de escaleno se todos os lados possuem medidas diferentes.
lado1 = input('Digite as medidas do primeiro lado: ')
lado2 = input('Digite as medidas do segundo lado: ')
lado3 = input('Digite as medidas do terceiro lado: ')

if lado1 == lado2 == lado3:
    print('Esse triângulo é equilátero')
elif lado1 != lado2 != lado3:
    print('Esse triângulo é escaleno')
else:
    print('Esse triângulo é isósceles')

# 5*

# Determine se um número é múltiplo de 5 e 7.
nmro = int(input ('Digite um número: '))
if nmro % 5 == 0 and nmro % 7 == 0:
    print('Este número é múltiplo de 5 e 7')
else:
    print('Este número não é multiplo de 5 e 7')

# 6*

# Verifique se um número é positivo e maior que 10
numb = int(input('Digite um número: '))
if numb > 0 and numb > 10:
    print('Esse número é positivo e maior que 10')
elif numb > 0 and numb < 10:
    print('Esse número é positivo mas não é maior que 10')
else:
    print('Esse número é negativo')

# 7*

# Verifique se um número é divisível por 3 ou 5.
nimb= int(input('Digite um número: '))
if nimb % 3 == 0 or nimb % 5 == 0:
    print('Esse número é divisível por 3 ou 5')
else:
    print('Não é possível dividir esse número por 3 ou 5')