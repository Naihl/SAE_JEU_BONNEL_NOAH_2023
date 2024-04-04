import pygame
from pygame.sprite import Sprite

class Coeur(Sprite):
    """
    Classe représentant un objet cœur dans un jeu.

    Cette classe hérite de pygame.sprite.Sprite, ce qui permet
    d'utiliser cette classe pour créer des sprites dans un jeu Pygame.

    Attributes:
        x (int): La position horizontale initiale de l'objet cœur.
        y (int): La position verticale initiale de l'objet cœur.
        path (str): Le chemin vers l'image représentant l'objet cœur.
        image (pygame.Surface): L'image représentant l'objet cœur.
        rect (pygame.Rect): Le rectangle de collision de l'objet cœur.
    """
    def __init__(self, x, y, taille_case, path = "img/coeur.png"):
        """
        Initialise un nouvel objet Coeur.

        Args:
            x (int): La position horizontale initiale de l'objet cœur.
            y (int): La position verticale initiale de l'objet cœur.
            path (str, optional): Le chemin vers l'image représentant l'objet cœur.
                Par défaut, c'est "img/coeur.png".
        """
        super().__init__()
        self.path = path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.taille_case = taille_case



    def obtenir_position(self):
        """
        Méthode pour obtenir la position du coeur.

        Returns:
            tuple: Un tuple contenant les coordonnées (x, y) du coeur.
        """
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
