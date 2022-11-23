from re import A
import pygame
import numpy as np
import random
import time
import os
#from menu import menu

pygame.init()




largura = 1300
altura = 700
window = pygame.display.set_mode((largura, altura))


imagem = pygame.image.load('assets/img/download (1).jpg').convert_alpha()
#RUNNING = pygame.image.load('assets/img/jacare.jpg').convert_alpha()
#DUCKING = pygame.image.load('assets/img/jacare2.jpg').convert_alpha()
#JUMPING = pygame.image.load('assets/img/jacare.jpg').convert_alpha()
#raposa = pygame.image.load('assets/img/raposa.png').convert_alpha()

correndo = [pygame.image.load(os.path.join("assets/img", "jacare.jpg")),
           pygame.image.load(os.path.join("assets/img", "jacare.jpg"))]
#RUNNING = pygame.transform.scale(RUNNING, (90,90))
pulando = pygame.image.load(os.path.join("assets/img", "jacare.jpg"))
abaixando = [pygame.image.load(os.path.join("assets/img", "jacare2.jpg")),
           pygame.image.load(os.path.join("assets/img", "jacare2.jpg"))]


class jacare:
    X_POS = 30
    Y_POS = 405
    Y_POS_bai = 450
    pulo_VEL = 8.5

    def __init__(self):
        self.ab_img = abaixando
        self.run_img = correndo
        self.jump_img = pulando

        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False

        self.step_index = 0
        self.jump_vel = self.pulo_VEL
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
    def update(self, userInput):
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if userInput[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
        elif userInput[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
        elif not (self.dino_jump or userInput[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
    def duck(self):
        self.image = self.ab_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_bai
        self.step_index += 1
        self.image = pygame.transform.scale(self.image, (90,45))
    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1
        self.image = pygame.transform.scale(self.image, (90,90))

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            self.image = pygame.transform.scale(self.image, (90,90))
        if self.jump_vel < - self.pulo_VEL:
            self.dino_jump = False
            self.jump_vel = self.pulo_VEL
            self.image = pygame.transform.scale(self.image, (90,90))

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.dino_rect.x, self.dino_rect.y))







def main():

    game = True
    clock = pygame.time.Clock()
    jogador = jacare()

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

        clock.tick(30)
        pygame.display.update()


main ()