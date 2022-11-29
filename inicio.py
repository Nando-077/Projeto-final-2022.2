def menu (pontos):

    
    import pygame

    pygame.init()

    # ----- Gera tela principal
    largura = 1300
    altura = 700
    window = pygame.display.set_mode((largura, altura))



  


    # ----- Inicia assets
    fundo = pygame.image.load('assets/img/FSC4900.jpg').convert()
    fundo = pygame.transform.scale(fundo, (largura,altura))

    #imagem do jacare
    jaca_L = 90
    jaca_A = 90
    jaca = pygame.image.load('assets/img/jacare.png').convert()
    jaca = pygame.transform.scale(jaca, (jaca_A,jaca_L))
    font = pygame.font.SysFont(None, 75)
    text = font.render('Precione 1 para começar', True, (0, 0, 0))
    game = True
    jaca_x = -jaca_L
    jaca_y = 290
    jaca_speedx= 1
    jaca_speedy = 0

    def vencedores(pontos):
            font = pygame.font.Font('freesansbold.ttf', 20)
            ordenado = sorted(pontos, reverse = True)
            dist = 100
            contador = 0
            for top_c in ordenado:
                imprime = top_c
                t_vence = font.render(str(imprime),True,(0,0,0))
                textRect = t_vence.get_rect()
                textRect.center = (200, dist)
                window.blit(t_vence, textRect)
                dist = dist +20
                contador = contador +1
                if contador > 5:
                    break


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
        
        userInput = pygame.key.get_pressed()

        # ----- Gera saídas
        window.fill((0, 0, 0)) 
        window.blit(fundo, (0, 0))
        window.blit(jaca, (jaca_x,jaca_y ))
        window.blit(text, (375,50 ))

        vencedores(pontos)
        if userInput[pygame.K_1]:
            from jogo import main
            main (pontos)

        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

    # ===== Finalização =====
    pygame.quit()