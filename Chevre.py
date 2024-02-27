import pygame
from Enemy import Enemy
from Joueur import Joueur

class Chevre(Enemy):
    """
    Classe représentant les chèvres (ennemis) dans un jeu, héritant de la classe Enemy.

    Attributes:
        nom (str): Le nom de la chèvre.
        x (int): La position horizontale initiale de la chèvre.
        y (int): La position verticale initiale de la chèvre.
        taille_case (int): La taille de la case dans laquelle la chèvre évolue.
        hp (int): Les points de vie de la chèvre.
        damage (int): Les dégâts infligés par la chèvre.
        mouvement (int): La vitesse de déplacement de la chèvre.
        path (str): Le chemin vers l'image représentant la chèvre.
        mort (bool): Indique si la chèvre est morte ou non.
    """
    def __init__(self, nom, x, y, taille_case, hp=100, damage=5, mouvement=4, path="img/chevre.png"):
        """
        Initialise une nouvelle instance de Chevre.

        Args:
            nom (str): Le nom de la chèvre.
            x (int): La position horizontale initiale de la chèvre.
            y (int): La position verticale initiale de la chèvre.
            taille_case (int): La taille de la case dans laquelle la chèvre évolue.
            hp (int, optional): Les points de vie de la chèvre. Par défaut, c'est 100.
            damage (int, optional): Les dégâts infligés par la chèvre. Par défaut, c'est 5.
            mouvement (int, optional): La vitesse de déplacement de la chèvre. Par défaut, c'est 4.
            path (str, optional): Le chemin vers l'image représentant la chèvre. Par défaut, c'est "img/chevre.png".
        """
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)
        self.path = path  # Chargez l'image spécifique pour les chèvres
        self.hp = 150
        self.damage = 15
        self.mouvement = 2
        self.mort = False
        
    def deplacer(self, dx, dy):
        """
        Méthode pour déplacer les chèvres vers le joueur.

        Args:
            dx (int): Le déplacement horizontal.
            dy (int): Le déplacement vertical.
        """
        self.rect.x += dx * self.taille_case
        self.rect.y += dy * self.taille_case
    
    def prendre_degats(self, degats):
        """
        Méthode pour infliger des dégâts à la chèvre.

        Args:
            degats (int): Les dégâts à infliger.
        """
        self.hp -= degats
        if self.hp <= 0:
            self.mourir()
            
    def obtenir_position(self):
        """
        Méthode pour obtenir la position de la chèvre.

        Returns:
            tuple: Un tuple contenant les coordonnées (x, y) de la chèvre.
        """
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    def mourir(self):
        """
        Méthode pour mettre à jour la position de la chèvre à sa mort.
        """
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
        
    
        
    
    
    

