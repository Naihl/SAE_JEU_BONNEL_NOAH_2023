import pygame
from Enemy import Enemy
from Joueur import Joueur

# Classe pour les chèvres (ennemis) qui hérite de la classe Enemy 
class Chevre(Enemy):
    def __init__(self, nom, x, y, taille_case, hp=100, damage=5, mouvement=4, path="img/chevre.png"):
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)
        self.path = path  # Chargez l'image spécifique pour les chèvres
        self.hp = 150
        self.damage = 15
        self.mouvement = 2
        self.mort = False
        
    # Méthode pour déplacer les chèvres vers le joueur
    def deplacer(self, dx, dy):
        self.rect.x += dx * self.taille_case
        self.rect.y += dy * self.taille_case
    
    # Méthode pour attaquer le joueur
    def prendre_degats(self, degats):
        self.hp -= degats
        if self.hp <= 0:
            self.mourir()
            
    # Méthode pour obtenir la position de la chèvre
    def obtenir_position(self):
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    # Méthode pour mettre à jour la position de la chèvre à sa mort
    def mourir(self):
        self.image.fill((0, 0, 0))
        self.rect.x = -100
        self.rect.y = -100
        self.mort = True
        
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
        
    
        
    
    
    

