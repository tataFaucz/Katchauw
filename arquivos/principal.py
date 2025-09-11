import pygame
from pygame import display
from pygame import event
from pygame.locals import QUIT, KEYUP, K_SPACE
from pygame import font
from pygame.time import Clock
from pygame.transform import scale
from pygame.image import load
from pygame.sprite import GroupSingle, Group, groupcollide
import botao
from jogador import Jogador
from inimigo import Inimigo 

class Jogo():
    def __init__(self):
        pygame.init()
        self.esta_rodando = True
        self.estado = 0
        self.tamanho = 800, 600
        self.superficie = display.set_mode(
            size = self.tamanho, 
            display = 0
        )
        display.set_caption(
            'Katchauw!'
        )
        self.font_destaque = font.SysFont('comicsans', 80)
        self.imagem_inicio = pygame.image.load('images/button_inicio.png').convert_alpha()
        self.imagem_sair = pygame.image.load('images/button_sair.png').convert_alpha()
        self.botao_inicio = botao.Botao(30, 450, self.imagem_inicio, 0.8)
        self.botao_sair = botao.Botao(600, 450, self.imagem_sair, 0.8)
        self.clock = Clock ()
        self.fundo = scale(
            load('images/space.jpg'),
            self.tamanho
        )
        self.fonte = font.SysFont('comicsans', 50)

    def novo_jogo(self):
        self.grupo_inimigos = Group()
        self.grupo_tiros = Group()
        self.jogador = Jogador(self)
        self.grupo_jogador = GroupSingle(self.jogador)
        self.grupo_inimigos.add(Inimigo(self))
        self.round = 0
        self.mortes = 0

    def rodar(self):
        while self.esta_rodando:
            for evento in event.get():
                if evento.type == QUIT:
                    self.esta_rodando = False 
                if self.estado == 1:
                    if evento.type==KEYUP:
                        if evento.key == K_SPACE:
                            self.jogador.atirar()
            if self.estado == 0:
                self.superficie.fill((15, 25, 54.51))
                titulo = self.font_destaque.render(
                    'Katchauw!', 
                    True,
                    (255, 165, 0)
                )
                self.superficie.blit(titulo, (190, 180))
                if self.botao_inicio.criar(self.superficie):
                    self.estado = 1
                    self.novo_jogo()
                if self.botao_sair.criar(self.superficie):
                    self.esta_rodando = False
            elif self.estado == 1:
                self.clock.tick(120)
                self.superficie.blit(self.fundo, (0,0))
                self.grupo_jogador.draw(self.superficie)
                self.grupo_jogador.update()
                self.grupo_inimigos.draw(self.superficie)
                self.round += 1
                if self.round %120 == 0:
                    self.grupo_inimigos.add(Inimigo(self))
                self.grupo_inimigos.update()
                self.grupo_tiros.draw(self.superficie)
                self.grupo_tiros.update()
                if groupcollide(
                    self.grupo_tiros,
                    self.grupo_inimigos, 
                    True,
                    True
                ):
                    self.mortes += 1
                fonte_mortes = self.fonte.render(
                    f'Mortes: {self.mortes}',
                    True,
                    (255, 255, 255)
                )
                self.superficie.blit(fonte_mortes, (20, 70))
            elif self.estado ==2:
                self.superficie.fill((202, 150, 150))
            display.update()

g = Jogo()
g.rodar()

pygame.quit()
exit()

#https://pixelartmaker.com/art/b26f04eb67d50bd