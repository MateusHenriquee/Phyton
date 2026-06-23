# #tipos de dados:
# #int = números inteiros 
# #float = armazena numero
# #booleano = armazena verdadeiro ou falso 
# #str = linha


# # import pygame
# # import sys

# # # 1. Inicializa o Pygame
# # pygame.init()

# # # 2. Configurações da tela
# # LARGURA = 800
# # ALTURA = 600
# # tela = pygame.display.set_mode((LARGURA, ALTURA))
# # pygame.display.set_caption("Meu Jogo 2D Base")

# # # Controle de FPS (Quadros por segundo)
# # relogio = pygame.time.Clock()
# # FPS = 60

# # # 3. Game Loop (Loop principal do jogo)
# # while True:
# #     # Captura eventos (como fechar a janela, cliques, etc.)
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     # Lógica do jogo (movimentação, colisões, etc.) virá aqui

# #     # Renderização (desenhar elementos na tela)
# #     tela.fill((0, 0, 0))  # Limpa a tela pintando de preto (RGB)

# #     # Atualiza a tela
# #     pygame.display.flip()

# #     # Mantém o jogo rodando a 60 FPS
# #     relogio.tick(FPS)

# # import pygame
# # import sys
# # import random

# # # 1. Inicializa o Pygame
# # pygame.init()

# # # 2. Configurações da tela
# # LARGURA = 800
# # ALTURA = 600
# # tela = pygame.display.set_mode((LARGURA, ALTURA))
# # pygame.display.set_caption("Jogo de Desviar 2D")

# # # Controle de FPS
# # relogio = pygame.time.Clock()
# # FPS = 60

# # # Cores (RGB)
# # PRETO = (0, 0, 0)
# # AZUL = (0, 100, 255)
# # VERMELHO = (255, 50, 50)
# # BRANCO = (255, 255, 255)

# # # Configurações do Jogador
# # jogador_tamanho = 50
# # jogador_x = LARGURA // 2 - jogador_tamanho // 2
# # jogador_y = ALTURA - jogador_tamanho - 20
# # jogador_velocidade = 7

# # # Configurações do Inimigo
# # inimigo_tamanho = 50
# # inimigo_x = random.randint(0, LARGURA - inimigo_tamanho)
# # inimigo_y = -inimigo_tamanho
# # inimigo_velocidade = 5

# # # Pontuação
# # pontos = 0
# # fonte = pygame.font.SysFont("Arial", 30)

# # # 3. Game Loop
# # while True:
# #     # Captura eventos
# #     for evento in pygame.event.get():
# #         if evento.type == pygame.QUIT:
# #             pygame.quit()
# #             sys.exit()

# #     # Movimentação do Jogador (Segurando as teclas)
# #     teclas = pygame.key.get_pressed()
# #     if teclas[pygame.K_LEFT] and jogador_x > 0:
# #         jogador_x -= jogador_velocidade
# #     if teclas[pygame.K_RIGHT] and jogador_x < LARGURA - jogador_tamanho:
# #         jogador_x += jogador_velocidade

# #     # Movimentação do Inimigo (Caindo)
# #     inimigo_y += inimigo_velocidade

# #     # Se o inimigo passar da tela, reseta ele no topo e ganha ponto
# #     if inimigo_y > ALTURA:
# #         inimigo_y = -inimigo_tamanho
# #         inimigo_x = random.randint(0, LARGURA - inimigo_tamanho)
# #         pontos += 1
# #         # Aumenta a velocidade gradualmente para ficar mais difícil
# #         inimigo_velocidade += 0.5

# #     # Sistema de Colisão (Retângulos se sobrepondo)
# #     rect_jogador = pygame.Rect(jogador_x, jogador_y, jogador_tamanho, jogador_tamanho)
# #     rect_inimigo = pygame.Rect(inimigo_x, inimigo_y, inimigo_tamanho, inimigo_tamanho)

# #     if rect_jogador.colliderect(rect_inimigo):
# #         print(f"Fim de Jogo! Sua pontuação: {pontos}")
# #         pygame.quit()
# #         sys.exit()

# #     # Desenhar na tela
# #     tela.fill(PRETO)  # Limpa a tela

# #     # Desenha o Jogador e o Inimigo (Formas geométricas simples)
# #     pygame.draw.rect(tela, AZUL, rect_jogador)
# #     pygame.draw.rect(tela, VERMELHO, rect_inimigo)

# #     # Desenha a Pontuação
# #     texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
# #     tela.blit(texto_pontos, (10, 10))

# #     # Atualiza a tela e controla o FPS
# #     pygame.display.flip()
# #     relogio.tick(FPS)
# import pygame
# import sys
# import random

# # 1. Inicializa o Pygame
# pygame.init()

# # 2. Configurações da tela (Horizontal para estilo arcade)
# LARGURA = 800
# ALTURA = 450
# tela = pygame.display.set_mode((LARGURA, ALTURA))
# pygame.display.set_caption("Shoot 'em Up Estilo R-Type")

# relogio = pygame.time.Clock()
# FPS = 60

# # Cores
# PRETO = (0, 0, 0)
# BRANCO = (255, 255, 255)
# VERDE = (0, 255, 100)      # Sua nave
# AMARELO = (255, 255, 0)    # Seus tiros
# VERMELHO = (255, 50, 50)   # Alienígenas inimigos

# # Configurações da Nave (Jogador)
# nave_w, nave_h = 40, 30
# nave_x, nave_y = 50, ALTURA // 2
# nave_velocidade = 6

# # Listas para gerenciar múltiplos objetos na tela
# tiros = []
# tiro_velocidade = 12
# tiro_w, tiro_h = 15, 4

# inimigos = []
# inimigo_w, enemy_h = 35, 35
# inimigo_velocidade = 4
# temporizador_inimigo = 0

# pontos = 0
# fonte = pygame.font.SysFont("Arial", 24)

# # 3. Game Loop Principal
# while True:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
            
#         # Atira quando pressiona a BARRA DE ESPAÇO
#         if evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_SPACE:
#                 # Cria o tiro saindo da frente da nave
#                 novo_tiro = pygame.Rect(nave_x + nave_w, nave_y + nave_h // 2 - tiro_h // 2, tiro_w, tiro_h)
#                 tiros.append(novo_tiro)

#     # Movimentação da Nave (Cima, Baixo, Esquerda, Direita)
#     teclas = pygame.key.get_pressed()
#     if teclas[pygame.K_UP] and nave_y > 0:
#         nave_y -= nave_velocidade
#     if teclas[pygame.K_DOWN] and nave_y < ALTURA - nave_h:
#         nave_y += nave_velocidade
#     if teclas[pygame.K_LEFT] and nave_x > 0:
#         nave_x -= nave_velocidade
#     if teclas[pygame.K_RIGHT] and nave_x < LARGURA - nave_w:
#         nave_x += nave_velocidade

#     # --- LÓGICA DOS TIROS ---
#     for tiro in tiros[:]:  # Usamos [:] para copiar a lista e evitar erros ao remover itens
#         tiro.x += tiro_velocidade
#         # Remove o tiro se ele sair da tela pela direita
#         if tiro.x > LARGURA:
#             tiros.remove(tiro)

#     # --- LÓGICA DOS INIMIGOS ---
#     temporizador_inimigo += 1
#     if temporizador_inimigo >= 40:  # Cria um novo inimigo a cada 40 quadros
#         inimigo_y_aleatorio = random.randint(20, ALTURA - enemy_h - 20)
#         novo_inimigo = pygame.Rect(LARGURA, inimigo_y_aleatorio, inimigo_w, enemy_h)
#         inimigos.append(novo_inimigo)
#         temporizador_inimigo = 0

#     for inimigo in inimigos[:]:
#         inimigo.x -= inimigo_velocidade
        
#         # Colisão: Se o inimigo encostar na sua nave
#         rect_nave = pygame.Rect(nave_x, nave_y, nave_w, nave_h)
#         if rect_nave.colliderect(inimigo):
#             print(f"Sua nave foi destruída! Pontuação final: {pontos}")
#             pygame.quit()
#             sys.exit()
            
#         # Remove inimigos que passaram da tela pela esquerda
#         if inimigo.x < -inimigo_w:
#             inimigos.remove(inimigo)

#     # --- SISTEMA DE COLISÃO (TIRO VS INIMIGO) ---
#     for tiro in tiros[:]:
#         for inimigo in inimigos[:]:
#             if tiro.colliderect(inimigo):
#                 # Se colidirem, remove ambos e adiciona pontuação
#                 if tiro in tiros: tiros.remove(tiro)
#                 if inimigo in inimigos: inimigos.remove(inimigo)
#                 pontos += 100

#     # --- DESENHAR ELEMENTOS ---
#     tela.fill(PRETO)  # Fundo do espaço

#     # Desenha a Nave
#     pygame.draw.rect(tela, VERDE, (nave_x, nave_y, nave_w, nave_h))

#     # Desenha todos os Tiros ativos
#     for tiro in tiros:
#         pygame.draw.rect(tela, AMARELO, tiro)

#     # Desenha todos os Inimigos ativos
#     for inimigo in inimigos:
#         pygame.draw.rect(tela, VERMELHO, inimigo)

#     # Placar
#     texto_placar = fonte.render(f"SCORE: {pontos}", True, BRANCO)
#     tela.blit(texto_placar, (15, 15))

#     pygame.display.flip()
#     relogio.tick(FPS)

import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Tela de Pintura")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
COR_ATUAL = PRETO

# Preenche o fundo de branco
tela.fill(BRANCO)

desenhando = False

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Começa a desenhar ao clicar e segurar o botão esquerdo
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if evento.button == 1: 
                desenhando = True
        
        # Para de desenhar ao soltar o botão
        if evento.type == pygame.MOUSEBUTTONUP:
            if evento.button == 1:
                desenhando = False
        
        # Desenha na tela enquanto o mouse se move com o botão pressionado
        if evento.type == pygame.MOUSEMOTION:
            if desenhando:
                posicao_mouse = pygame.mouse.get_pos()
                pygame.draw.circle(tela, COR_ATUAL, posicao_mouse, 5)

    pygame.display.update()
