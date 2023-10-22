import pygame
from Enemy import Enemy
from Joueur import Joueur
import math

# Classe pour les Maraudeur (ennemis) qui hérite de la classe Enemy
class Maraudeur(Enemy):
    def __init__(self, nom, x, y, taille_case, hp=150, damage=15, mouvement=2, path="img/maraudeur.png"):
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)
        self.path = path  
        self.hp = 150
        self.damage = 10
        self.mouvement = 2
        self.mort = False
        
    # Méthode pour déplacer les Maraudeur vers le joueur
    def deplacer_vers_joueur(self, joueur):
        dx = joueur.rect.centerx - self.rect.centerx
        dy = joueur.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance != 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * self.vitesse
        self.rect.y += dy * self.vitesse
    
    # Méthode pour attaquer le joueur
    def attaquer(self, joueur):
        joueur.hp -= self.damage
    
    # Méthode pour mettre à jour la position du Maraudeur à sa mort
    def mourir(self):
        self.image.fill((0, 0, 0))
        self.rect.x = -100
        self.rect.y = -100
        self.mort = True
    
    # Méthode pour prendre des dégats
    def prendre_degats(self, degats):
        self.hp -= degats
        if self.hp <= 0:
            self.mourir()
            
    # Méthode pour obtenir la position du Maraudeur
    def obtenir_position(self):
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    # Méthode pour mettre à jour la position du Maraudeur
    def update(self, joueur):
        if self.hp <= 0:
            self.hp = 0
        else:
            self.deplacer_vers_joueur(joueur)
            self.attaquer_joueur(joueur)
    
        
    @property
    def getnom(self):
        return self.nom
    
    @getnom.setter
    def setnom(self, nom):
        self.nom = nom
        
    @property
    def gethp(self):
        return self.hp
    
    @gethp.setter
    def sethp(self, hp):
        self.hp = hp
        
    @property
    def getdamage(self):
        return self.damage
    
    @getdamage.setter
    def setdamage(self, damage):
        self.damage = damage
        
    @property
    def getmouvement(self):
        return self.mouvement
    
    @getmouvement.setter
    def setmouvement(self, mouvement):
        self.mouvement = mouvement
        
    
    
    
