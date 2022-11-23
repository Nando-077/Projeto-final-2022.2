import pygame
import random
from os import path

from config import IMG_DIR, FPS, GAME, QUIT


def init_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial
    largura = 600
    altura = 400
    fundo = pygame.image.load('assets/img/download (1).jpg').convert()
    fundo = pygame.transform.scale(fundo, (largura,altura))
    #imagem jacare
    jaca_L = 90
    jaca_A = 90
    jaca = pygame.image.load('assets/img/Desenho-Jacaré-PNG.png').convert()
    jaca = pygame.transform.scale(jaca, (jaca_A,jaca_L))

    
    jaca_x = -jaca_L
    jaca_y = 290
    jaca_speedx= 5
    jaca_speedy = 0
    

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        jaca_x += jaca_speedx
        jaca_y += jaca_speedy

        if jaca_y > altura or jaca_x + jaca_L < 0 or jaca_x > largura:
            jaca_x = -jaca_L
            jaca_y = 290

        # A cada loop, redesenha o fundo e os sprites
        window.fill((0, 0, 0)) 
        window.blit(fundo, (0, 0))
        window.blit(jaca, (jaca_x,jaca_y ))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()
        pygame.display.update()

    return state

    
   