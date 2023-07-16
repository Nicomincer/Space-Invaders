import pygame 
from pygame.locals import *
from sys import exit
import os
global move_to_left, move_to_right, shot, atirar

preto = (0, 0, 0)
move_to_right = False
move_to_left = False
shot = False
atirar = False 
largura = 800
altura = 670

pygame.init()

janela = pygame.display.set_mode((largura, altura))
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
        self.rect.center = (x*100, 120)
    
    def update(self):
        if self.index_lista >= len(self.images)-1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05
        
        self.image = self.images[int(self.index_lista)]
    

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = sprite_sheet.subsurface((2, 1), (11, 8))
        img = pygame.transform.scale(img, (50, 50))
        img2 = sprite_sheet.subsurface((2, 11.7), (11, 8))
        img2 = pygame.transform.scale(img2, (50, 50))
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


class Enemy3(pygame.sprite.Sprite):
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
        self.rect.center = (x*100, 180)
    
    def update(self):
        if self.index_lista >= len(self.images)-1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05
        
        self.image = self.images[int(self.index_lista)]

class Enemy4(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = sprite_sheet.subsurface((39, 1), (13, 8))
        img = pygame.transform.scale(img, (50, 50))
        img2 = sprite_sheet.subsurface((44, 11.7), (11, 8))
        img2 = pygame.transform.scale(img2, (50, 50))
        self.images.append(img)
        self.images.append(img2)
        
        self.index_lista = 0
        self.image = self.images[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100, 240)
    
    def update(self):
        if self.index_lista >= len(self.images)-1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05
        
        self.image = self.images[int(self.index_lista)]


class Enemy5(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        img = sprite_sheet.subsurface((39, 1), (13, 8))
        img = pygame.transform.scale(img, (50, 50))
        img2 = sprite_sheet.subsurface((44, 11.7), (11, 8))
        img2 = pygame.transform.scale(img2, (50, 50))

        self.images.append(img)
        self.images.append(img2)
        
        self.index_lista = 0
        self.image = self.images[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (x*100, 300)
    
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
        self.rect.center = (400, 580)

        
    def update(self):
        global move_to_left, move_to_right, shot
        
        if move_to_right == True:
            self.rect.x += 10
            move_to_right = False 
        if move_to_left == True: 
            self.rect.x -= 10
            move_to_left = False
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0


class Barreira(pygame.sprite.Sprite):
    def __init__(self, indice):
        pygame.sprite.Sprite.__init__(self)

        imagem_barreira = sprite_sheet.subsurface((45, 31), (24, 16))

        self.image = pygame.transform.scale(imagem_barreira, (100, 100))

        self.rect = self.image.get_rect()
        self.rect.center = (40*(indice*5), 440)


class Lifebar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        hp_image = sprite_sheet.subsurface((84, 91), (26, 3))
        self.image = pygame.transform.scale(hp_image, (150, 25))
        
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, altura)


grupo_de_sprites = pygame.sprite.Group()

for x in range(1, 8):
    personagem_inimigo2 = Enemy2(x)
    grupo_de_sprites.add(personagem_inimigo2)


for x in range(1, 8):
    personagem_inimigo = Enemy(x)
    grupo_de_sprites.add(personagem_inimigo)

for x in range(1, 8):
    personagem_inimigo3 = Enemy3(x)
    grupo_de_sprites.add(personagem_inimigo3)
for posicao2 in range(1, 4):
    protection = Barreira(posicao2)
    grupo_de_sprites.add(protection)
personagem_controlado_pelo_player = Personagem()

for x in range(1, 8):
    personagem_inimigo4 = Enemy4(x)
    grupo_de_sprites.add(personagem_inimigo4)

for x in range(1, 8):
    personagem_inimigo5 = Enemy5(x)
    grupo_de_sprites.add(personagem_inimigo5)

lifebar = Lifebar()
grupo_de_sprites.add(lifebar)

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