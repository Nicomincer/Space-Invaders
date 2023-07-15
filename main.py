import pygame 
from pygame.locals import *
from sys import exit
import os

preto = (0, 0, 0)

pygame.init()

janela = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Space Invaders")

diretorio_atual = os.path.dirname(__file__)
diretorio_das_sprites = os.path.join(diretorio_atual, "images")
sprite_sheet = pygame.image.load(os.path.join(diretorio_das_sprites, "sprites.png")).convert_alpha()

class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = sprite_sheet.subsurface((22, 1), (11, 8))
        img = pygame.transform.scale(img, (50, 50))
        self.images.append(img)
        
        self.index_lista = 0
        self.image = self.images[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 370)


grupo_de_sprites = pygame.sprite.Group()
personagem_controlado_pelo_player = Space()
grupo_de_sprites.add(personagem_controlado_pelo_player)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    janela.fill(preto)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    grupo_de_sprites.draw(janela)
    grupo_de_sprites.update()

    pygame.display.flip()