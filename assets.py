import pygame
import os
from config import largura, altura, altura_raposa,largura_raposa,altura_jac,largura_jac,IMG_DIR,SND_DIR,FNT_DIR

fundo = 'fundo'
raposa = 'raposa'
jac = 'jac'

musica = 'musica'

def load_assets():
    assets = {}
    assets[fundo] = pygame.image.load(os.path.join(IMG_DIR, 'dowload(1).jpg')).convert()
    assets[raposa] = pygame.image.load(os.path.join(IMG_DIR, 'raposa.png')).convert_alpha()
    assets[raposa] = pygame.transform.scale(assets['raposa.png'], (altura_raposa, largura_raposa))
    assets[jac] = pygame.image.load(os.path.join(IMG_DIR, 'Desenho-jacaré-PNG.png')).convert_alpha()
    assets[jac] = pygame.transform.scale(assets['Desenho-jacaré-PNG.png'], (altura_jac,largura_jac))
    pygame.mixer.music.load(os.path.join(SND_DIR, 'SOM.mp3'))
    pygame.mixer.music.set_volume(0.4)
    assets[musica] = pygame.mixer.Sound(os.path.join(SND_DIR, 'Som.mp3'))
    return assets
