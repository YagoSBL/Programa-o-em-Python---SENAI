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

cliente1_name = (input('Por favor, informe seu nome: '))
cliente1_idade = int(input('Agora, informe sua idade para completar o cadastro: '))
cliente1 = [cliente1_name, cliente1_idade]
cliente2_name = (input('Por favor, informe seu nome: '))
cliente2_idade = int(input('Agora, informe sua idade para completar o cadastro: '))
cliente2 = [cliente2_name, cliente2_idade]
cliente3_name = (input('Por favor, informe seu nome: '))
cliente3_idade = int(input('Agora, informe sua idade para completar o cadastro: '))
cliente3 = [cliente3_name, cliente3_idade]

#2 Reserva de quartos
qrt_cliente1 = input(f'Seja bem vindo {cliente1_name}, escolha o quarto desejado: ')
qrt_simple = (input('Quarto Simples'))
qrt_double = (input('Quarto Duplo'))
qrt_lux = (input('Quarto Luxo'))
escolha1 = [cliente1, qrt_cliente1]
qrt_cliente2 = input(f'Seja bem vindo {cliente2_name}, escolha o quarto desejado: ')
qrt_simple = (input('Quarto Simples'))
qrt_double = (input('Quarto Duplo'))
qrt_lux = (input('Quarto Luxo'))
escolha2 = [cliente2, qrt_cliente2]
