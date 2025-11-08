#1 
#CRIE UMA FUNÇÃO PARA COMPARAR 2 NÚMEROS (par ou impar). UTILIZE VARIÁVEIS LOCAIS
prim = int(input('Vamos verificar o primeiro número: '))
seg = int(input('Agora, o segundo: '))
def parimp():
    if prim % 2 == 0:
        print ('O primeiro número é par')
    else:
        print ('O sprimeiro número é impar')
    if seg % 2 == 0:
        print ('O segundo número é par')
    else:
        print ('O segundo número é impar')
parimp()

#2
#CRIE UMA FUNÇÃO PARA MULTIPLICAR 3 NUMEROS.
numero  = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))
numero3 = int(input('Digite o último número: '))
def soma():
    somando = numero * numero2 * numero3
    print(somando)

soma()   

#3
#CRIE UMA FUNÇÃO PARA DESCOBRIR O VALOR ELEVADO DE UM NÚMERO.
numb = int(input('Digite um número: '))
qto = int(input('Digite a potência para elevar o número: '))
def elev():
    elevado = numb ** qto
    print(elevado)

elev()

#4
#CRIE UMA FUNÇÃO PARA MOSTRAR UMA MENSAGEM PERSONALIZADA NA TELA, SE O USUÁRIO  DIGITAR, 18 ANOS.
mensagem = input('Digite uma idade (PS: Digite "18 Anos para uma surpresa"): ')
def msg():
    if mensagem == '18':
        print ('Uma surpresa 😶‍🌫️, já és adulto ')
    else:
        print (mensagem)
msg()

#5
#DESENVOLVA UMA FUNÇÃO PARA DESCOBRIR A IDADE DE UMA PESSOA.
idade = int(input('Digite o ano que você nasceu e eu lhe direi sua idade: '))
def data():
    anos = 2025 - idade
    print(anos)
data()

#6
#DESENVOLVA UMA FUNÇÃO PARA VER SE O BRASIL GANHOU A COPA DE 1999.
ano = int(input('Digite um ano que teve copa para que eu verifique se o Brasil venceu a copa: '))
def copa():
        anos_copa = [1930, 1934, 1938, 1950, 1954, 1958, 1962, 1966, 1970, 1974, 1978, 1982, 1986, 1990, 1994, 1998, 2002, 2006, 2010, 2014, 2018, 2022]
        if ano == 1958 or 1962 or 1970 or 1994 or 2002 :
            print ('Sim, o Brasil foi campeão nessa copa! 🤩')
        elif ano not in anos_copa:
            print ('Não tivemos copa do mundo nesse ano, tente novamente 😒')         
        else:
            print ('Nesse ano o Brasil não foi campeão 😢')  
copa()

#7
#DESENVOLVA UM SISTEMA DE RESTAURANTE, ONDE O CLIENTE TEM OPÇÃO DE ESCOLHER ENTRE SALADA, MACARRONADA, SANDUICHE, SORVETE.  
#1 - Função -  cumprimentar o cliente
#2 - Função - restaurante
#3 - Sugestão utilize listas  e loops

def bistro():
    print ('Olá, bem vindo, selecione as opções desejadas: ') 
    carrinho = []
    escolha = input('''
      1 - Salada
      2 - Macarronada
      3 - Sanduíche
      4 - Sorvete
     ''')
    if escolha  == '1':
        valor_salada = input('Valor da salada: ',{15.00})
        print(valor_salada)
        escolha = input ('Deseja adcionar ao carrinho? S ou N?')
        if escolha == S:
            carrinho.append(valor_salada)
        elif escolha == N:
            print ('Certo, selecione outro item')
            
        else: 
            print ('Digitação inválida, digite novamente S ou N')
            escolha == '1'
        
        
    elif escolha  == '2':
        valor_macarronada = input('Valor da macarronada: ',{18.90})
        print(valor_macarronada)
        escolha1 = input ('Deseja adcionar ao carrinho? S ou N?')
        if escolha1 == S:
            carrinho.append(valor_macarronada)
        elif escolha1 == N:
            print('Certo, selecione outro item')
            
        else:
            print('Digitação inválida, digite novamente S ou N')
            escolha == '2'

    elif escolha  == '3':
        valor_sanduiche = input('Valor do sanduíche: ',{12.00})
        print(valor_sanduiche)
        escolhas = input ('Deseja adcionar ao carrinho? S ou N?')
        if escolhas == S:
            carrinho.append(valor_sanduiche)
        elif escolhas == N:
            print('Certo, selecione outro item')
            
        else:
            print('Digitação inválida, digite novamente S ou N')
            escolha == '3'

    elif escolha == '4':
        valor_sorvete = input('Valor do sorvete: ',{8.90})
        print(valor_sorvete)
        escolhasorv = input ('Deseja adcionar ao carrinho? S ou N?')
        if escolhasorv == S:
            carrinho.append(valor_sorvete)
        elif escolhasorv == N:
            print('Certo, selecione outro item')
            
        else:
            print('Digitação inválida, digite novamente S ou N')
            escolha == '4'
        
    else:
        print('essa opção não existe')
        
        
def loop():        
    while True:
        bistro()
    
        
loop() 