def menu ():

    import pygame

    pygame.init()

    # ----- Gera tela principal
    largura = 600
    altura = 400
    window = pygame.display.set_mode((largura, altura))



  


    # ----- Inicia assets
    fundo = pygame.image.load('assets/img/download (1).jpg').convert()
    fundo = pygame.transform.scale(fundo, (largura,altura))

    #imagem do jacare
    jaca_L = 90
    jaca_A = 90
    jaca = pygame.image.load('assets/img/Desenho-Jacaré-PNG.png').convert()
    jaca = pygame.transform.scale(jaca, (jaca_A,jaca_L))

    game = True
    jaca_x = -jaca_L
    jaca_y = 290
    jaca_speedx= 0.1
    jaca_speedy = 0


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

        jaca_x += jaca_speedx
        jaca_y += jaca_speedy

        if jaca_y > altura or jaca_x + jaca_L < 0 or jaca_x > largura:
            jaca_x = -jaca_L
            jaca_y = 290
            
        # ----- Gera saídas
        window.fill((0, 0, 0)) 
        window.blit(fundo, (0, 0))
        window.blit(jaca, (jaca_x,jaca_y ))
        

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()