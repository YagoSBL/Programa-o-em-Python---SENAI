#def display():
 #   try:
        # n  =  1/0
  #      n  = 10
   #     l = []
    #    print(l[10])
        # x  = int(input('='))
        # print(n + x)
        # print(a)
   # except NameError as erro:
    #    print(erro)   
   # except ZeroDivisionError as erro:
    #    print(erro)   
   # except ValueError as erro:
    #    print(erro)  
   # except IndexError as erro:
    #    print(erro)            
    #else:
     #   print('Ocorreu um erro não identificado')
    #finally:
   #     print('fim de carregamento...')        


#display()

# 1 - Peça ao usuário para inserir um número e manipule a exceção caso ele insira algo que não seja um número inteiro.

try:
  nmb = int (input('Digite um número: ')) 
  print(nmb)
except ValueError:
    print('Não digitaram um número')
    



# 2 - Peça ao usuário para inserir dois números e realize uma operação de divisão. Manipule a exceção caso ocorra um erro na operação  -  ZeroDivisionError.

try:
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    print(a/b)
except ZeroDivisionError:
    print('erro')



# 3 - Crie uma lista e um índice como entrada e retorne o índice. Manipule a exceção caso o índice seja inválido(caso imprima um indice que não exista na lista).

try:
  lista = ['Bola', 'Carro', 'Sapato']
  liserro = int(input('Digite um indice: '))
  print(lista[liserro])
except IndexError:
    print('Não contém esse valor na lista')       