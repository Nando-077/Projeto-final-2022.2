# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random


pygame.init()

# ----- Gera tela principal
largura = 1300
altura = 700
window = pygame.display.set_mode((largura, altura))


# ----- Inicia assets
alt_rapo = 90
larg_rapo = 90
font = pygame.font.SysFont(None, 48)
fundo = pygame.image.load('assets/img/download (1).jpg').convert_alpha()
fundo = pygame.transform.scale(fundo, (largura,altura))
rapo_img = pygame.image.load('assets/img/raposa.png').convert_alpha()
rapo_img= pygame.transform.scale(rapo_img, (larg_rapo, alt_rapo))

# ----- Inicia estruturas de dados
# Definindo os novos tipos
class Meteor(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = -larg_rapo
        self.rect.y = random.randint(350, 550)
        self.speedx = random.randint(4, 6)
        self.speedy = 0

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > altura or self.rect.right < 0 or self.rect.left > largura:
            self.rect.x = -larg_rapo
            self.rect.y = random.randint(350, 550 )
            self.speedx = random.randint(4, 6)
           

game = True
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 30

# Criando dois meteoros
rapo1 = Meteor(rapo_img)
rapo2 = Meteor(rapo_img)

# ===== Loop principal =====
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição dos meteoros
    rapo1.update()
    rapo2.update()

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(fundo, (0, 0))
    # Desenhando meteoros
    window.blit(rapo1.image, rapo1.rect)
    window.blit(rapo2.image, rapo2.rect)

    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados