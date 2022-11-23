import pygame

# ----- Gera tela principal
largura = 600
altura = 400
window = pygame.display.set_mode((largura, altura))


# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
fundo = pygame.image.load('assets/img/download (1).jpg').convert()
fundo = pygame.transform.scale(fundo, (largura,altura))

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
    
    

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()


