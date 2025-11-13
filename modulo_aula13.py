# 1 Crie número aleatório de 5,10

import random
def num_aleatorio():
    n = random.randrange (5,11)
    print('Número aleatório de 5 a 10 é: ', n)

#2 Crie 3 números aleatórios

import random
def n_rand():
    nr = random.randrange (0,10000000)
    nr2 = random.randrange (0,10000000)
    nr3 = random.randrange (0,10000000)
    print('Os três números alearótios são: ',[nr], [nr2], [nr3])

# 3 Crie um número aleatório entre 10 a 30 utilize o range()

import random
def nmr_rand(): 
    nmr = random.randrange(10,31)
    print('O número aleatório entre 10 e 30 é: ',nmr)


# 4  Contagem regressiva simples
# Escreva programa que exiba contagem regressiva de 10 a 1, e depois imprima "Fogo!" (loop for)

def ctg_regr():
    for c in range (1, 11):
            print(c)
        
        
    print ('Fogo!')
            

# 5 Soma de números pares
# Peça ao usuário que insira número inteiro positivo e calcule a soma de todos os números pares de 2 até o número inserido

def nm_par():
    qlr = int(input('Digite um número qualquer: '))
    soma = 0
    for x in range(2,qlr,2):
        soma = soma + x
        print (soma)
    
# 6  - Tabuada de multiplicação
# Peça ao usuário para inserir um número inteiro e mostre a tabuada de multiplicação desse número de 1 a 10.
# (while ou for )

def tabu():
    tabuada = int(input('Digite um número inteiro: '))
    
    #     m = [tabuada * 1, tabuada *2, tabuada * 3, tabuada * 4, tabuada * 5, tabuada * 6, tabuada * 7, tabuada * 8, tabuada * 9, tabuada * 10]
    # print (m)
    for m in range (0,11):
        c = tabuada * m
        print(tabuada,'x ', m, '= ', c)
    
    

# 7 Exiba uma contagem regressiva de números ímpares de 99 a 1.
# (for)

def regr():
    for c in range (99,-1,-1):
        print (c)