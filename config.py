from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'assets', 'img')
SND_DIR = path.join(path.dirname(__file__), 'assets', 'snd')
FNT_DIR = path.join(path.dirname(__file__), 'assets', 'font')



# Dados gerais do jogo.
largura = 480 # Largura da tela
altura = 600 # Altura da tela
FPS = 60 # Frames por segundo

altura_raposa = 50
largura_raposa = 38
altura_jac = 50
largura_jac = 38

INIT = 0
GAME = 1
QUIT = 2


