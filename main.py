import pygame
from pygame.locals import *
from sys import exit
import os
from random import randint 

preto = (0, 0, 0)
move_to_right = False
move_to_left = False
shot = False
score = 0 
largura = 800
altura = 670

pygame.init()

janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Space Invaders")

font = pygame.font.SysFont('Arial', 40)

diretorio_atual = os.path.dirname(__file__)
diretorio_das_sprites = os.path.join(diretorio_atual, "images")
sprite_sheet = pygame.image.load(os.path.join(diretorio_das_sprites, "sprites.png")).convert_alpha()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img2 = sprite_sheet.subsurface((22, 1), (11, 8))
        img2 = pygame.transform.scale(img2, (40, 40))
        img = sprite_sheet.subsurface((22, 11.7), (11, 8))
        img = pygame.transform.scale(img, (40, 40))
        img3 = sprite_sheet.subsurface((22, 11.7), (11, 8))
        img3 = pygame.transform.scale(img3, (40, 40))
        self.images.append(img)
        self.images.append(img2)
        self.images.append(img3)

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
        img = pygame.transform.scale(img, (40, 40))
        img2 = sprite_sheet.subsurface((2, 11.7), (11, 8))
        img2 = pygame.transform.scale(img2,(40, 40))
        img3 = sprite_sheet.subsurface((2, 11.7), (11, 8))
        img3 = pygame.transform.scale(img3, (40, 40))
        self.images.append(img)
        self.images.append(img2)
        self.images.append(img3)

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
        img2 = pygame.transform.scale(img2, (40, 40))
        img = sprite_sheet.subsurface((22, 11.7), (11, 8))
        img = pygame.transform.scale(img, (40, 40))
        img3 = sprite_sheet.subsurface((22, 11.7), (11, 8))
        img3 = pygame.transform.scale(img3, (40, 40))
        self.images.append(img)
        self.images.append(img2)
        self.images.append(img3)

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
        img = pygame.transform.scale(img, (40, 40))
        img2 = sprite_sheet.subsurface((39.8, 11.7), (13, 8))
        img2 = pygame.transform.scale(img2, (40, 40))
        img3 = sprite_sheet.subsurface((39.8, 11.7), (13, 8))
        img3 = pygame.transform.scale(img3, (40, 40))
        self.images.append(img)
        self.images.append(img2)
        self.images.append(img3)

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
        img = pygame.transform.scale(img, (40, 40))
        img2 = sprite_sheet.subsurface((39.8, 11.7), (13, 8))
        img2 = pygame.transform.scale(img2, (40, 40))
        img3 = sprite_sheet.subsurface((39.8, 11.7), (13, 8))
        img3 = pygame.transform.scale(img3, (40, 40))

        self.images.append(img)
        self.images.append(img2)
        self.images.append(img3)

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
        self.rect.center = (randint(100, 800), randint(60, 300))
        

    def update(self):
        if self.rect.bottom <= altura:
            self.rect.y = self.rect.y + 20
        else:
            self.rect.y = randint(60, 300)
            self.rect.x = randint(100, 800)



grupo_de_sprites = pygame.sprite.Group()
grupo_protecao = pygame.sprite.Group()
grupo_de_sprites2 = pygame.sprite.Group()
for i in range(120, 301, 60):
    for c in range(1, 8):
        if i == 120:
            personagem_inimigo = Enemy(c, i)
            grupo_de_sprites2.add(personagem_inimigo)
        if i == 180:
            personagem_inimigo = Enemy2(c, i)
            grupo_de_sprites2.add(personagem_inimigo)
        if i == 240:
            personagem_inimigo = Enemy3(c, i)
            grupo_de_sprites2.add(personagem_inimigo)
        if i == 300:
            personagem_inimigo = Enemy4(c, i)
            grupo_de_sprites2.add(personagem_inimigo)
        if i == 360:
            personagem_inimigo = Enemy5(c, i)
            grupo_de_sprites2.add(personagem_inimigo)

for posicao2 in range(1, 4):
    protection = Barreira(posicao2)
    grupo_protecao.add(protection)

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
    mensagem = f"Score: {score}"

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
        score += 50 
    
    colisao2 = pygame.sprite.spritecollide(tiro_inimigo, grupo_unitario, False)
    if colisao2:
        lifebar.rect.x -= 50
        tiro_inimigo.rect.y = randint(60, 300)
        tiro_inimigo.rect.x = randint(100, 800)
    
    colisao3 = pygame.sprite.spritecollide(tiro_inimigo, grupo_protecao, False)
    if colisao3:
        tiro_inimigo.rect.y = randint(60, 300)
        tiro_inimigo.rect.x = randint(100, 800)
    
    colisao4 = pygame.sprite.spritecollide(object_shot, grupo_protecao, False)
    if colisao4:
        object_shot.rect.bottom = 0

    if pygame.key.get_pressed()[K_d]:
        move_to_right = True
    elif pygame.key.get_pressed()[K_a]:
        move_to_left = True
    
    render = font.render(mensagem, False, (255, 255, 255))

    grupo_de_sprites2.draw(janela)
    grupo_protecao.draw(janela)
    grupo_de_sprites.draw(janela)
    grupo_de_sprites.update()

    janela.blit(render, (320, 0))
    pygame.display.flip()