# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame

# Inicializa o Pygame
pygame.init()



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/




# Elaborando a exibição de tela, possui tamanho de 400px de largura por 400px de altura, o nome do jogo é exibido na tela "Labirinto"
largura, altura = 400, 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Labirinto")

# Variáveis separadas para serem usadas futuramente, podem ser usadas de forma universal no código sendo chamadas pelo nome da variável, os números apresentados são códigos das cores em formato
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Essa lista constrói a estrutura do labirinto, indicando o tamanho das células que servirão de parede, caminho e personagem e os números listados indicam o caminho que poderá ser
#percorrido pelo personagem
tamanho_celula = 40
labirinto = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Construção do objeto jogável, está determinando seu tamanho e sua velocidade de movimento no percurso do labirinto
x, y = 1 * tamanho_celula, 1 * tamanho_celula
velocidade = 40
# Construção geral do labirinto, vale destacar que ele está construído em formato de colunas. As partes que se usa a variável preto são inacessíveis, indicam parede, enquanto a parte
#branco indicará o caminho que pode ser seguido, associa-se à lista anterior, onde o número 1 está indicando a parte preta do labirinto e caso não seja, será uma parte caminhável
def desenhar_labirinto():
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            cor = preto if labirinto[linha][coluna] == 1 else branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))
            # As variáveis usadas como características foram criadas anteriormente, para construir as características físicas dos objetos do jogo que terão formato retangular (rect)

# Comportamento do programa, indica que o programa irá rodar por eventos, até que seja solicitado o encerramento por uma ação QUIT que no caso do jogo será o botão de fechar a janela 
executando = True
while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

# Nessa parte está codificado o processo feito pelo jogador, conforme as teclas listadas são pressionadas ocorre  mudança de comportamento do personagem no labirinto, getp _pressed indica o acionamento das teclas
    teclas = pygame.key.get_pressed()
# Comportamento do personagem de acordo com o uso da tecla de seta para esquerda (LEFT), sendo a movimentação limitada pelo espaço disponível (branco) para movimentação para a esquerda no eixo Y 
#atenção especial no segundo if que indica que o personagem está parado e só se moverá se for resultado 0     
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
# Comportamento do personagem de acordo com o uso da tecla de seta para direita (RIGHT), sendo a movimentação limitada pelo espaço disponível (branco) para movimentação para a direita no eixo Y 
#atenção especial no segundo if que indica que o personagem está parado e só se moverá se o resultado for 0            
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
# Comportamento do personagem de acordo com o uso da tecla de seta para cima (UP), sendo a movimentação limitada pelo espaço disponível (branco) para movimentação para cima no eixo Y
#atenção especial no segundo if que indica que o personagem está parado e só se moverá se o resultado for 0 
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
# Comportamento do personagem de acordo com o uso da tecla de seta para baixo (DOWN), sendo a movimentação limitada pelo espaço disponível (branco) para movimentação para baixo no eixo Y
#atenção especial no segundo if que indica que o personagem está parado e só se moverá se o resultado for 0           
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y

# Representa que a cor da tela será preenchida com a cor da variável utilizada, no caso branco. Está será a parte que o cubo pode se mover
    tela.fill(branco)

# Aqui está sendo representado o personagem do jogo e sua cor, suas dimensões são definidas anteriormente pelas variáveis e lhe foi indicada a cor vermelha pela variável    
    desenhar_labirinto()
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula))

# Permite identificarmos que a modificação na tela foi feita, quando selecionamos aonde o personagem andou. Sobrepoe na tela a situação atual pela que havia ocorrido antes
    pygame.display.flip()

# Indica a taxa de quadros de resposta do programa, no caso 10 frames por segundo
    pygame.time.Clock().tick(10)

# Possibilita o encerramento do programa
pygame.quit()
