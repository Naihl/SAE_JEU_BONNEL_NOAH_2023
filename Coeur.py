import pygame
from pygame.sprite import Sprite

#classe coeur permettant de créer un objet coeur
class Coeur(Sprite):
    def __init__(self, x, y, path = "img/coeur.png"):
        super().__init__()
        self.path = path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

