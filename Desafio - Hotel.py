# Desafio
# Contratado para desenvolver sistema de hotel. Criar sistema para gerenciar reservas de quartos e pagamento das diárias
# 1 - Cadastrar cliente ( deve permitir cadastrar nome e idade de até 3 clientes )
# 2 - Reservar quartos (deve oferecer 3 tipos de quartos: Simples, Duplo e Luxo)
# 3 - Cada cliente escolherá o quarto para a estadia e os valores variam com o tipo de quarto:
# Simples: R$ 100,00 por dia
# Duplo: R$ 150,00 por dia
# Luxo: R$ 250,00 por dia
# 4 - Calcule a estadia (usuário vai informar quantos dias vai ficar na estadia e o sistema calculará quantos ficará e multiplicará pelos dias que o cliente ficará)
# exemplo: valor_cliente3 = preco_duplo * cliente3_dias

#1 Cadastro dos clientes
quantidade =  int(input('Informe a quantidade de pessoas: '))

dados = {
'nomes':[],
'idades':[]
}

lista_quartos  =  ['', 'Simples', 'Duplo', 'Luxo']
valores_quartos = [0, 100,150,250]


if quantidade == 1:
    nome  =  input('Por favor, informe seu nome:')
    idade = int(input('Agora, informe sua idade: '))
    dados['nomes'].append(nome)
    dados['idades'].append(idade)
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome, '-> ', quantidade_dias)

elif quantidade == 2:
    nome1  =  input('Por favor, informe seu nome:')
    idade = int(input('Agora, informe a idade: '))

    nome2  =  input('Por favor, informe o seu nome:')
    idade = int(input('Agora, informe a sua idade: '))

    escolha =  int(input(f'''
                    Escolha de quarto hospede{nome1}     
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome1, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome1, '-> ', quantidade_dias)


    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome2, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome2, '-> ', quantidade_dias)


elif quantidade == 3:

    nome1  =  input('Por favor, informe seu nome:')
    idade = int(input('Agora, informe sua idade: '))
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome1, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome1, '-> ', quantidade_dias)


    nome2  =  input('Por favor, informe seu nome:')
    idade = int(input('Agora, informe sua idade: '))
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome2, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome2, '-> ', quantidade_dias)


    nome3  =  input('Por favor, informe seu nome:')
    idade = int(input('Agora, informe sua idade: '))
    escolha =  int(input(f'''
                    1 - {lista_quartos[1]} R$ {float(valores_quartos[1])}
                    2 - {lista_quartos[2]} R$ {float(valores_quartos[2])}
                    3 - {lista_quartos[3]} R$ {float(valores_quartos[3])}               
                    '''))
    
    print('O hospede', nome3, 'escolheu o quarto: ', lista_quartos[escolha])
    quantidade_dias =  int(input('Dias: '))
    calculo = quantidade_dias * valores_quartos[escolha]
    print(f'R$, {calculo:.2f}')
    print('Quantidade de dias do hospede', nome3, '-> ', quantidade_dias)



else:
    print('Para mais hospedes, entre em contato com a coordenação.')
