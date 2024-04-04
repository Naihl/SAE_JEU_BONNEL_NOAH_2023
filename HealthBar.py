import pygame
from Joueur import Joueur

class HealthBar:
    """
    Classe représentant une barre de vie dans un jeu.

    Attributes:
        fenetre (pygame.Surface): La surface sur laquelle la barre de vie est dessinée.
        joueur (Joueur): Le joueur associé à la barre de vie.
        x (int): La position horizontale de la barre de vie.
        y (int): La position verticale de la barre de vie.
        largeur_barre_max (int): La largeur maximale de la barre de vie.
        largeur_barre_actuelle (int): La largeur actuelle de la barre de vie, basée sur les points de vie du joueur.
        couleur_sante_max (tuple): La couleur de la barre de vie lorsque la santé est au maximum.
        couleur_sante_actuelle (tuple): La couleur de la barre de vie en fonction de la santé actuelle du joueur.
    """
    def __init__(self, fenetre, joueur : Joueur, x, y):
        """
        Initialise une nouvelle instance de HealthBar.

        Args:
            fenetre (pygame.Surface): La surface sur laquelle la barre de vie est dessinée.
            joueur (Joueur): Le joueur associé à la barre de vie.
            x (int): La position horizontale de la barre de vie.
            y (int): La position verticale de la barre de vie.
        """
        self.fenetre = fenetre
        self.joueur = joueur
        self.x = x
        self.y = y
        self.largeur_barre_max = joueur.hp * 2
        self.largeur_barre_actuelle = joueur.hp * 2
        self.couleur_sante_max = (192, 192, 192)
        self.couleur_sante_actuelle = (0, 128, 0)

    def update(self):
        """
        Met à jour la barre de vie en fonction des points de vie actuels du joueur.
        """
        self.largeur_barre_actuelle = self.joueur.hp * 2
        rect_barre_max = pygame.Rect(self.x, self.y, self.largeur_barre_max, 20)
        rect_barre_actuelle = pygame.Rect(self.x, self.y, self.largeur_barre_actuelle, 20)
        
        pygame.draw.rect(self.fenetre, self.couleur_sante_max, rect_barre_max)
        pygame.draw.rect(self.fenetre, self.couleur_sante_actuelle, rect_barre_actuelle) 