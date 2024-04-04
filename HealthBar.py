import pygame
from Joueur import Joueur

#classe healthbar permettant de créer une barre de vie
class HealthBar:
    def __init__(self, fenetre, joueur : Joueur, x, y):
        self.fenetre = fenetre
        self.joueur = joueur
        self.x = x
        self.y = y
        self.largeur_barre_max = joueur.hp * 2
        self.largeur_barre_actuelle = joueur.hp * 2
        self.couleur_sante_max = (192, 192, 192)
        self.couleur_sante_actuelle = (0, 128, 0)

    # Méthode pour mettre à jour la barre de vie
    def update(self):
        self.largeur_barre_actuelle = self.joueur.hp * 2
        rect_barre_max = pygame.Rect(self.x, self.y, self.largeur_barre_max, 20)
        rect_barre_actuelle = pygame.Rect(self.x, self.y, self.largeur_barre_actuelle, 20)
        
        pygame.draw.rect(self.fenetre, self.couleur_sante_max, rect_barre_max)
        pygame.draw.rect(self.fenetre, self.couleur_sante_actuelle, rect_barre_actuelle) 