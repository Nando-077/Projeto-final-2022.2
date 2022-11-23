def menu ():

    import pygame

    pygame.init()

    # ----- Gera tela principal
    largura = 600
    altura = 400
    window = pygame.display.set_mode((largura, altura))


    # ----- Inicia estruturas de dados
    game = True

    # ----- Inicia assets
    fundo = pygame.image.load('assets/img/download (1).jpg').convert()
    fundo = pygame.transform.scale(fundo, (largura,altura))

    #imagem do jacare
    jaca = pygame.image.load('assets/img/Desenho-Jacaré-PNG.png').convert()
    jaca = pygame.transform.scale(jaca, (100,100))

    # ===== Loop principal =====
    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    x = 1
            
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(fundo, (0, 0))
        window.blit(jaca, (250, 100))

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()