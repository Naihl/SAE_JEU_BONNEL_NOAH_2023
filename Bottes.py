import pygame
from pygame.sprite import Sprite

class Bottes(Sprite):
    """
    Classe représentant un objet bottes dans un jeu.

    Cette classe hérite de pygame.sprite.Sprite, ce qui permet
    d'utiliser cette classe pour créer des sprites dans un jeu Pygame.

    Attributes:
        x (int): La position horizontale initiale de l'objet bottes.
        y (int): La position verticale initiale de l'objet bottes.
        path (str): Le chemin vers l'image représentant l'objet bottes.
        image (pygame.Surface): L'image représentant l'objet bottes.
        rect (pygame.Rect): Le rectangle de collision de l'objet bottes.
    """
    def __init__(self, x, y, path = "img/botte.png"):
        """
    Classe représentant un objet bottes dans un jeu.

    Cette classe hérite de pygame.sprite.Sprite, ce qui permet
    d'utiliser cette classe pour créer des sprites dans un jeu Pygame.

    Attributes:
        x (int): La position horizontale initiale de l'objet bottes.
        y (int): La position verticale initiale de l'objet bottes.
        path (str): Le chemin vers l'image représentant l'objet bottes.
        image (pygame.Surface): L'image représentant l'objet bottes.
        rect (pygame.Rect): Le rectangle de collision de l'objet bottes.
    """
        super().__init__()
        self.path = path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


