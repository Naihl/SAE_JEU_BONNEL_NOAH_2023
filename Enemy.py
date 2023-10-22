import pygame
from Entity import Entity  

#classe Enemy permettant de créer un objet Enemy qui hérite de la classe Entity qui se decline en class d'enemy
class Enemy(Entity):
    def __init__(self, nom, x, y, taille_case, hp, damage, mouvement, path = ""):
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)  
        self.path = ""
        self.hp = 100
        self.damage = 10
        self.mouvement = 3
     
    # Méthode pour obtenir la position des enemies
    def obtenir_position(self):
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    #attribut permettant de recuperer la position actuelle de l'enemy
    case_actuelle = property(obtenir_position)

    # Méthode pour déplacer les enemies 
    def deplacer(self, dx, dy):
        self.rect.x += dx * self.taille_case
        self.rect.y += dy * self.taille_case
    
        
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
        
    
    
    
