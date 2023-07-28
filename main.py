import pygame
from pygame.locals import *
from sys import exit
import os

preto = (0, 0, 0)
move_to_right = False
move_to_left = False
shot = False
largura = 800
altura = 670

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Space Invaders")

diretorio_atual = os.path.dirname(__file__)
diretorio_das_sprites = os.path.join(diretorio_atual, "images")
sprite_sheet = pygame.image.load(os.path.join(diretorio_das_sprites, "sprites.png")).convert_alpha()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.rect.center = (x * 100, y)

    def update(self):
        if self.index_lista >= len(self.images) - 1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05

        self.image = self.images[int(self.index_lista)]


class Enemy2(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.rect.center = (x * 100, y)


    def update(self):
        if self.index_lista >= len(self.images) - 1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05

        self.image = self.images[int(self.index_lista)]


class Enemy3(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.rect.center = (x * 100, y)

    def update(self):
        if self.index_lista >= len(self.images) - 1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05

        self.image = self.images[int(self.index_lista)]


class Enemy4(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.rect.center = (x * 100, y)

    def update(self):
        if self.index_lista >= len(self.images) - 1:
            self.index_lista = 0
        else:
            self.index_lista += 0.05

        self.image = self.images[int(self.index_lista)]


class Enemy5(pygame.sprite.Sprite):
    def __init__(self, x, y):
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
        self.rect.center = (x * 100, y)

    def update(self):
        if self.index_lista >= len(self.images) - 1:
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
        self.rect.center = (40 * (indice * 5), 440)


class Lifebar(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        hp_image = sprite_sheet.subsurface((84, 91), (26, 3))
        self.image = pygame.transform.scale(hp_image, (150, 25))

        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, altura)


class Shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        shot_image = sprite_sheet.subsurface((52, 22), (1, 6))
        self.image = pygame.transform.scale(shot_image, (11, 20))
        self.rect = self.image.get_rect()

    def put_shot(self, x):
        global shot
        if shot == True:
            self.rect.center = (x + 28, 520)

    def update(self):
        global shot
        if self.rect.bottom > 0:
            self.rect.y -= 25
        else:
            shot = False

class Shot_enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        shot_image = sprite_sheet.subsurface((52, 22), (1, 6))
        self.image = pygame.transform.scale(shot_image, (11, 20))
        self.rect = self.image.get_rect()
        self.rect.center = (95, 330)
        

    def update(self):
        if self.rect.bottom <= altura:
            self.rect.y = self.rect.y + 20
        else:
            self.rect.y = 330



grupo_de_sprites = pygame.sprite.Group()
grupo_de_sprites2 = pygame.sprite.Group()
personagem_inimigo_1_1 = Enemy(1, 120)
personagem_inimigo_1_2 = Enemy(2, 120)
personagem_inimigo_1_3 = Enemy(3, 120)
personagem_inimigo_1_4 = Enemy(4, 120)
personagem_inimigo_1_5 = Enemy(5, 120)
personagem_inimigo_1_6 = Enemy(6, 120)
personagem_inimigo_1_7 = Enemy(7, 120)

personagem_inimigo2_1 = Enemy2(1, 50)
personagem_inimigo2_2 = Enemy2(2, 50)
personagem_inimigo2_3 = Enemy2(3, 50)
personagem_inimigo2_4 = Enemy2(4, 50)
personagem_inimigo2_5 = Enemy2(5, 50)
personagem_inimigo2_6 = Enemy2(6, 50)
personagem_inimigo2_7 = Enemy2(7, 50)

personagem_inimigo3_1 = Enemy3(1, 180)
personagem_inimigo3_2 = Enemy3(2, 180)
personagem_inimigo3_3 = Enemy3(3, 180)
personagem_inimigo3_4 = Enemy3(4, 180)
personagem_inimigo3_5 = Enemy3(5, 180)
personagem_inimigo3_6 = Enemy3(6, 180)
personagem_inimigo3_7 = Enemy3(7, 180)

personagem_inimigo4_1 = Enemy4(1, 240)
personagem_inimigo4_2 = Enemy4(2, 240)
personagem_inimigo4_3 = Enemy4(3, 240)
personagem_inimigo4_4 = Enemy4(4, 240)
personagem_inimigo4_5 = Enemy4(5, 240)
personagem_inimigo4_6 = Enemy4(6, 240)
personagem_inimigo4_7 = Enemy4(7, 240)

personagem_inimigo5_1 = Enemy5(1, 300)
personagem_inimigo5_2 = Enemy5(2, 300)
personagem_inimigo5_3 = Enemy5(3, 300)
personagem_inimigo5_4 = Enemy5(4, 300)
personagem_inimigo5_5 = Enemy5(5, 300)
personagem_inimigo5_6 = Enemy5(6, 300)
personagem_inimigo5_7 = Enemy5(7, 300)

grupo_de_sprites.add(personagem_inimigo_1_1)
grupo_de_sprites.add(personagem_inimigo_1_2)
grupo_de_sprites.add(personagem_inimigo_1_3)
grupo_de_sprites.add(personagem_inimigo_1_4)
grupo_de_sprites.add(personagem_inimigo_1_5)
grupo_de_sprites.add(personagem_inimigo_1_6)
grupo_de_sprites.add(personagem_inimigo_1_7)
grupo_de_sprites.add(personagem_inimigo2_1)
grupo_de_sprites.add(personagem_inimigo2_2)
grupo_de_sprites.add(personagem_inimigo2_3)
grupo_de_sprites.add(personagem_inimigo2_4)
grupo_de_sprites.add(personagem_inimigo2_5)
grupo_de_sprites.add(personagem_inimigo2_6)
grupo_de_sprites.add(personagem_inimigo2_7)
grupo_de_sprites.add(personagem_inimigo3_1)
grupo_de_sprites.add(personagem_inimigo3_2)
grupo_de_sprites.add(personagem_inimigo3_3)
grupo_de_sprites.add(personagem_inimigo3_4)
grupo_de_sprites.add(personagem_inimigo3_5)
grupo_de_sprites.add(personagem_inimigo3_6)
grupo_de_sprites.add(personagem_inimigo3_7)
grupo_de_sprites.add(personagem_inimigo4_1)
grupo_de_sprites.add(personagem_inimigo4_2)
grupo_de_sprites.add(personagem_inimigo4_3)
grupo_de_sprites.add(personagem_inimigo4_4)
grupo_de_sprites.add(personagem_inimigo4_5)
grupo_de_sprites.add(personagem_inimigo4_6)
grupo_de_sprites.add(personagem_inimigo4_7)
grupo_de_sprites.add(personagem_inimigo5_1)
grupo_de_sprites.add(personagem_inimigo5_2)
grupo_de_sprites.add(personagem_inimigo5_3)
grupo_de_sprites.add(personagem_inimigo5_4)
grupo_de_sprites.add(personagem_inimigo5_5)
grupo_de_sprites.add(personagem_inimigo5_6)
grupo_de_sprites.add(personagem_inimigo5_7)

grupo_de_sprites2.add(personagem_inimigo_1_1)
grupo_de_sprites2.add(personagem_inimigo_1_2)
grupo_de_sprites2.add(personagem_inimigo_1_3)
grupo_de_sprites2.add(personagem_inimigo_1_4)
grupo_de_sprites2.add(personagem_inimigo_1_5)
grupo_de_sprites2.add(personagem_inimigo_1_6)
grupo_de_sprites2.add(personagem_inimigo_1_7)
grupo_de_sprites2.add(personagem_inimigo2_1)
grupo_de_sprites2.add(personagem_inimigo2_2)
grupo_de_sprites2.add(personagem_inimigo2_3)
grupo_de_sprites2.add(personagem_inimigo2_4)
grupo_de_sprites2.add(personagem_inimigo2_5)
grupo_de_sprites2.add(personagem_inimigo2_6)
grupo_de_sprites2.add(personagem_inimigo2_7)
grupo_de_sprites2.add(personagem_inimigo3_1)
grupo_de_sprites2.add(personagem_inimigo3_2)
grupo_de_sprites2.add(personagem_inimigo3_3)
grupo_de_sprites2.add(personagem_inimigo3_4)
grupo_de_sprites2.add(personagem_inimigo3_5)
grupo_de_sprites2.add(personagem_inimigo3_6)
grupo_de_sprites2.add(personagem_inimigo3_7)
grupo_de_sprites2.add(personagem_inimigo4_1)
grupo_de_sprites2.add(personagem_inimigo4_2)
grupo_de_sprites2.add(personagem_inimigo4_3)
grupo_de_sprites2.add(personagem_inimigo4_4)
grupo_de_sprites2.add(personagem_inimigo4_5)
grupo_de_sprites2.add(personagem_inimigo4_6)
grupo_de_sprites2.add(personagem_inimigo4_7)
grupo_de_sprites2.add(personagem_inimigo5_1)
grupo_de_sprites2.add(personagem_inimigo5_2)
grupo_de_sprites2.add(personagem_inimigo5_3)
grupo_de_sprites2.add(personagem_inimigo5_4)
grupo_de_sprites2.add(personagem_inimigo5_5)
grupo_de_sprites2.add(personagem_inimigo5_6)
grupo_de_sprites2.add(personagem_inimigo5_7)

for posicao2 in range(1, 4):
    protection = Barreira(posicao2)
    grupo_de_sprites.add(protection)

personagem_controlado_pelo_player = Personagem()
grupo_de_sprites.add(personagem_controlado_pelo_player)

lifebar = Lifebar()
object_shot = Shot()
tiro_inimigo = Shot_enemy()
grupo_de_sprites.add(object_shot)
grupo_de_sprites.add(lifebar)
grupo_de_sprites.add(tiro_inimigo)
grupo_unitario = pygame.sprite.Group()
grupo_unitario.add(personagem_controlado_pelo_player)

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
                if shot == False:
                    shot = True
                    object_shot.put_shot(personagem_controlado_pelo_player.rect.x)
                else:
                    pass

    colisoes = pygame.sprite.spritecollide(object_shot, grupo_de_sprites2, True)
    if colisoes:
        object_shot.rect.bottom = 0
    
    colisao2 = pygame.sprite.spritecollide(tiro_inimigo, grupo_unitario, False)
    if colisao2:
        lifebar.rect.x -= 50
        tiro_inimigo.rect.y = 330

    if pygame.key.get_pressed()[K_d]:
        move_to_right = True
    elif pygame.key.get_pressed()[K_a]:
        move_to_left = True

    grupo_de_sprites.draw(janela)
    grupo_de_sprites.update()

    pygame.display.flip()