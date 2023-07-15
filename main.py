from typing import Any
import pygame 
from pygame.locals import *
from sys import exit
import os
from time import sleep
global move_to_left, move_to_right, shot, atirar
from threading import Thread

preto = (0, 0, 0)
move_to_right = False
move_to_left = False
shot = False
atirar = False 

pygame.init()

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invaders")

diretorio_atual = os.path.dirname(__file__)
diretorio_das_sprites = os.path.join(diretorio_atual, "images")
sprite_sheet = pygame.image.load(os.path.join(diretorio_das_sprites, "sprites.png")).convert_alpha()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img2 = sprite_sheet.subsurface((22, 1), (11, 8))
        img2 = pygame.transform.scale(img2, (50, 50))
        img = sprite_sheet.subsurface((22, 11.7), (11, 8))
        img = pygame.transform.scale(img, (50, 50))
        self.images.append(img)
        self.images.append(img2)
        
        self.index_lista = 0
        self.image = self.images[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100, 50)
    
    def update(self):
        if self.index_lista >= len(self.images)-1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05
        
        self.image = self.images[int(self.index_lista)]

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens = []
        img = sprite_sheet.subsurface((1, 50), (15, 6.8))
        img = pygame.transform.scale(img, (50, 50))
    
        self.imagens.append(img)
        self.indice_da_imagem = 0
        self.image = self.imagens[self.indice_da_imagem]
        self.rect = self.image.get_rect()
        self.rect.center = (400, 560)

        
    def update(self):
        global move_to_left, move_to_right, shot
        
        if move_to_right == True:
            self.rect.x += 10
            move_to_right = False 
        elif move_to_left == True: 
            self.rect.x -= 10
            move_to_left = False

class Shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        img = sprite_sheet.subsurface((51, 22), (3, 7))
        self.image = pygame.transform.scale(img, (20, 20))
        self.rect = self.image.get_rect()
        
        #self.rect.center = (403, 500)
    
    def update(self):
        global shot
        if shot == True:
            self.loop = Thread(target=self.loop_infinito)
            self.loop.start()
    
    def loop_infinito(self):
        global shot
        atirando = True
        while atirando:
            self.rect.center = (403, 500)
            self.rect.y -= 20
            if self.rect.y <= 0:
                shot = False
                self.rect.y = 0
                atirando = True


grupo_de_sprites = pygame.sprite.Group()
for posicao in range(1, 8):
    personagem_inimigo = Enemy(posicao)
    grupo_de_sprites.add(personagem_inimigo)
personagem_controlado_pelo_player = Personagem()
tiro = Shot()

grupo_de_sprites.add(tiro)
grupo_de_sprites.add(personagem_controlado_pelo_player)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    janela.fill(preto)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                shot = True
                
        


    if pygame.key.get_pressed()[K_d]:
        move_to_right = True
    elif pygame.key.get_pressed()[K_a]:
        move_to_left = True

    grupo_de_sprites.draw(janela)
    grupo_de_sprites.update()

    pygame.display.flip()