import pygame 
from pygame.locals import *
from sys import exit

preto = (0, 0, 0)

pygame.init()

janela = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Space Invaders")

font = pygame.font.SysFont('Arial', 40, True, True)
mensagem = font.render('Hello, World!', False, (255, 0, 0))

class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

grupo_de_sprites = pygame.sprite.Group()
personagem_controlado_pelo_player = Space()
grupo_de_sprites.add(personagem_controlado_pelo_player)

relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    janela.fill(preto)
    janela.blit(mensagem, (100, 200))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    grupo_de_sprites.draw(janela)
    grupo_de_sprites.update()

    pygame.display.flip()