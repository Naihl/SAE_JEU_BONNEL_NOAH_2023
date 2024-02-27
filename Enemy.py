import pygame
from Entity import Entity  

class Enemy(Entity):
    """
    Classe représentant un ennemi dans un jeu, héritant de la classe Entity.

    Attributes:
        nom (str): Le nom de l'ennemi.
        x (int): La position horizontale initiale de l'ennemi.
        y (int): La position verticale initiale de l'ennemi.
        taille_case (int): La taille de la case dans laquelle l'ennemi évolue.
        hp (int): Les points de vie de l'ennemi.
        damage (int): Les dégâts infligés par l'ennemi.
        mouvement (int): La vitesse de déplacement de l'ennemi.
        path (str): Le chemin vers l'image représentant l'ennemi.
    """
    def __init__(self, nom, x, y, taille_case, hp, damage, mouvement, path = ""):
        """
        Initialise un nouvel objet Enemy.

        Args:
            nom (str): Le nom de l'ennemi.
            x (int): La position horizontale initiale de l'ennemi.
            y (int): La position verticale initiale de l'ennemi.
            taille_case (int): La taille de la case dans laquelle l'ennemi évolue.
            hp (int): Les points de vie de l'ennemi.
            damage (int): Les dégâts infligés par l'ennemi.
            mouvement (int): La vitesse de déplacement de l'ennemi.
            path (str, optional): Le chemin vers l'image représentant l'ennemi. Par défaut, c'est une chaîne vide.
        """
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)  
        self.path = ""
        self.hp = 100
        self.damage = 10
        self.mouvement = 3
    
    def obtenir_position(self):
        """
        Méthode pour obtenir la position de l'ennemi.

        Returns:
            tuple: Un tuple contenant les coordonnées (x, y) de l'ennemi.
        """
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    #attribut permettant de recuperer la position actuelle de l'enemy
    case_actuelle = property(obtenir_position)

    def deplacer(self, dx, dy):
        """
        Méthode pour déplacer l'ennemi.

        Args:
            dx (int): Le déplacement horizontal.
            dy (int): Le déplacement vertical.
        """
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
        
    
    
    
