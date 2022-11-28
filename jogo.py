from re import A
import pygame
import numpy as np
import random
import time
import os
from inicio import menu

#from raposa import raposa
from assets import musica, load_assets
#from menu import menu

pygame.init()




largura = 1300
altura = 700
window = pygame.display.set_mode((largura, altura))


imagem = pygame.image.load('assets/img/download (1).jpg').convert_alpha()
correndo = pygame.image.load('assets/img/jacare.png').convert_alpha()
abaixando = pygame.image.load('assets/img/jacare2.png').convert_alpha()
pulando = pygame.image.load('assets/img/jacare.png').convert_alpha()
raposa_tx = pygame.image.load('assets/img/raposa.png').convert_alpha()

pontos = [1,0,2,3,4]
raposa_tx= pygame.transform.scale(raposa_tx, (120,90))
raposa_tx= pygame.transform.flip(raposa_tx,True,False)

correndo= pygame.transform.scale(correndo, (120,90))
pulando= pygame.transform.scale(pulando, (120,90))
abaixando= pygame.transform.scale(abaixando, (120,45))

class jacare:
    X_POS =200
    Y_POS = 405
    Y_POS_bai = 450
    pulo_VEL = 8.5

    def __init__(self):
        self.ab_img = abaixando
        self.corr_img = correndo
        self.pul_img = pulando

        self.jac_ab = False
        self.jac_corr = True
        self.jac_pul = False

        self.step_index = 0
        self.pulo_vel = self.pulo_VEL
        self.image = self.corr_img
        self.jac_rect = self.image.get_rect()
        self.jac_rect.x = self.X_POS
        self.jac_rect.y = self.Y_POS
    def update(self, userInput):
        if self.jac_ab:
            self.duck()
        if self.jac_corr:
            self.run()
        if self.jac_pul:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.jac_pul:
            self.jac_ab = False
            self.jac_corr = False
            self.jac_pul = True
        elif userInput[pygame.K_DOWN] and not self.jac_pul:
            self.jac_ab = True
            self.jac_corr = False
            self.jac_pul = False
        elif not (self.jac_pul or userInput[pygame.K_DOWN]):
            self.jac_ab = False
            self.jac_corr = True
            self.jac_pul = False
    def duck(self):
        self.image = self.ab_img
        self.jac_rect = self.image.get_rect()
        self.jac_rect.x = self.X_POS
        self.jac_rect.y = self.Y_POS_bai
        self.step_index += 1
        self.image = pygame.transform.scale(self.image, (90,45))
    def run(self):
        self.image = self.corr_img
        self.jac_rect = self.image.get_rect()
        self.jac_rect.x = self.X_POS
        self.jac_rect.y = self.Y_POS
        self.step_index += 1
        self.image = pygame.transform.scale(self.image, (90,90))

    def jump(self):
        self.image = self.pul_img
        if self.jac_pul:
            self.jac_rect.y -= self.pulo_vel * 4
            self.pulo_vel -= 0.8
            self.image = pygame.transform.scale(self.image, (90,90))
        if self.pulo_vel < - self.pulo_VEL:
            self.jac_pul = False
            self.pulo_vel = self.pulo_VEL
            self.image = pygame.transform.scale(self.image, (90,90))

    def draw(self, window):
        window.blit(self.image, (self.jac_rect.x, self.jac_rect.y))


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = largura
        self.step_index = 0
        



    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, window):
        window.blit(self.image[self.type], self.rect)

class raposa(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        nivel = random.randint (1,2)
        if nivel == 1:
            self.rect.y = 340
        if nivel == 2:
            self.rect.y = 410
        self.index = 0
        

    def draw(self, window):
        if self.index >= 9:
            self.index = 0
        window.blit(self.image, self.rect)
        self.index += 1
        



def main(pontos):

    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    game = True
    clock = pygame.time.Clock()
    jogador = jacare()
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    points = 0
    game_speed = 20
    perdeu = False
    x_pos_bg = 0
    y_pos_bg = 380
  

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1

        text = font.render("Points: " + str(points), True, (225, 225, 225))
        textRect = text.get_rect()
        textRect.center = (1000, 100)
        window.blit(text, textRect)
        
    
    def vencedores(pontos):
        ordenado = sorted(pontos, reverse = True)
        dist = 100
        contador = 0
        for top_c in ordenado:
            imprime = top_c
            t_vence = font.render(str(imprime),True,(50,50,225))
            textRect = t_vence.get_rect()
            textRect.center = (200, dist)
            window.blit(t_vence, textRect)
            dist = dist +20
            contador = contador +1
            if contador > 5:
                break
            



            

 
    while game:

            # ----- Trata eventos
        for event in pygame.event.get():

            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        window.fill((225,225,225))
        fundo = pygame.image.load('assets/img/download (1).jpg').convert()
        fundo = pygame.transform.scale(fundo, (largura, altura))
        userInput = pygame.key.get_pressed()
        window.blit(fundo, (0, 0))
        

        jogador.draw(window)
        jogador.update(userInput)
        if len(obstacles) == 0:
            #if random.randint(0, 2) == 2:
            obstacles.append(raposa(raposa_tx))

        for obstacle in obstacles:
            obstacle.draw(window)
            obstacle.update()
            if jogador.jac_rect.colliderect(obstacle.rect):
                pygame.draw.rect(window, (255,0,0), jogador.jac_rect,2)
                pygame.time.delay(30)
                perdeu = True
                #death_count += 1
                #menu(death_count)
        score()
        vencedores(pontos)
        
        if perdeu == True:
            pontos.append(points)
            menu (pontos)
            perdeu = False
            
            #game = False
            #vencedores()

        clock.tick(30)
        pygame.display.update()
    

main (pontos)

#assets = load_assets
#assets[musica].play()


