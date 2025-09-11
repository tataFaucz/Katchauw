import pygame 
from random import randint 
from pygame.image import load 
from pygame.sprite import Sprite 

class Inimigo(Sprite): 
    def __init__(self, jogo): 
        super().__init__() 

        self.jogo = jogo 
        self.image = load('images/kart.png') 
        self.image = pygame.transform.scale(self.image, (80, 80)) 
        self.rect = self.image.get_rect( 
            center=(self.jogo.tamanho[0], randint(20, 580)) 
        ) 
    
    def update(self):
        self.rect.x -= 1
        if self.rect.x == 0:
            self.kill()
            self.jogo.estado = 2
