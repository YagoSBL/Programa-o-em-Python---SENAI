# 1 - Verificando se número é par ou impar
num = int(input('Digite um número para verificá-lo: '))

match num:
    case x if x % 2 == 0:
        print ("Par")
    case x if x % 2 != 0:
        print ("Ímpar")


# 2 - Verificando se número é positivo, negativo ou zero
num = int(input('Digite um número para verificá-lo: '))

match num:
    case 0:
        print ("Zero")
    case x if x > 0:
        print ("Positivo")
    case x if x < 0:
        print ("Negativo")        

# 3 - Verificando se uma string é vazia ou não
num = (input('Digite algo: '))
match num:
    case '':
        print ("Vazia")
    case _:
        print ("Está com dados")

# 4 - Verificando se um número é maior, igual ou menor que 10
num = int(input('Digite um número para verificá-lo: '))

match num:
    case x if x <10:
        print ("É menor que 10")
    case x if x == 10:
        print ("É igual a 10")
    case x if x > 10:
        print ("É maior que 10") 

# 5 - Classificar faixas etárias -  criança(12), adolescente(17), jovem(35), adulto 35 ><64, idoso(65)
num = int(input('Digite uma idade para verificar a faixa etária: '))

match num:
    case x if x <= 12:
        print ("É uma criança")
    case x if x <= 17:
        print ("É um adolescente")
    case x if x < 35:
        print ("É um jovem") 
    case x if x < 64:
        print ("É um adulto")
    case x if x >= 65:

        print ("E um idoso")
