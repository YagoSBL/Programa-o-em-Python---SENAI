# Atividade 1
#1 - Faça um programa, utilizando ***while***, que mostre na tela os números de 0 a 1000.
#2 -  Faça um sistema, utilizando ***while e listas***, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.


# 1
n = 0
while n <= 1000:
     print (n)
     n = n+1 

# 2
lista_nomes = []
c = 0
while c <= 10:
     nome= input ('Digite os nomes :')
     lista_nomes.append(nome)
     print (lista_nomes)
     c = c+1

# Atividade 2
# Crie um sistema de notas alunos
# - Acesso a conta com condicionais
# - 3 chances de acessar o sistema
# - Após errar 3 x mensagem que diga que a conta bloqueada (senha incorreta)
# - Inserir notas (se Senha correta)
# - Fazer a média

senhas = '340'
logins = 'Joao'
for n in range (3): 
     
        acesso_login = input('Digite o login: ')
        acesso_senha = input('Digite a senha: ')
        if senhas == acesso_senha and logins == acesso_login:
            print ('Seja bem vindo, professor')
            quantidade = int(input('Quantidade de alunos: '))
            for n in range (quantidade):
                nome = input('Nome do aluno: ')
                nota1 = float(input('Nota 1: '))
                nota2 = float(input('Nota 2: '))
                nota3 = float(input('Nota 3: '))
                media = (nota1+nota2+nota3)/3
                print('A média do aluno',  nome, 'é', media)
            input('Digite enter para sair')
                
        else:
            print('Informações incorretas, tente novamente')
                     
else:
       print('Senha bloqueada')
       
          

