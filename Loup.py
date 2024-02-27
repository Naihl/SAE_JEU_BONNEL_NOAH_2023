import pygame
from Enemy import Enemy
from Joueur import Joueur
import math

class Loup(Enemy):
    """
    Classe représentant un loup (ennemi) dans un jeu, héritant de la classe Enemy.

    Attributes:
        nom (str): Le nom du loup.
        x (int): La position horizontale initiale du loup.
        y (int): La position verticale initiale du loup.
        taille_case (int): La taille de la case dans laquelle le loup évolue.
        hp (int): Les points de vie actuels du loup.
        damage (int): Les dégâts infligés par le loup.
        mouvement (int): La vitesse de déplacement du loup.
        path (str): Le chemin vers l'image représentant le loup.
        mort (bool): Indique si le loup est mort ou non.
    """
    def __init__(self, nom, x, y, taille_case, hp=150, damage=15, mouvement=2, path="img/loup.jpg"):
        """
        Initialise un nouvel objet Loup.

        Args:
            nom (str): Le nom du loup.
            x (int): La position horizontale initiale du loup.
            y (int): La position verticale initiale du loup.
            taille_case (int): La taille de la case dans laquelle le loup évolue.
            hp (int, optional): Les points de vie actuels du loup. Par défaut, c'est 150.
            damage (int, optional): Les dégâts infligés par le loup. Par défaut, c'est 15.
            mouvement (int, optional): La vitesse de déplacement du loup. Par défaut, c'est 2.
            path (str, optional): Le chemin vers l'image représentant le loup. Par défaut, c'est "img/loup.jpg".
        """
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)
        self.path = path 
        self.hp = 150
        self.damage = 15
        self.mouvement = 2
        self.mort = False
    
    def deplacer_vers_joueur(self, joueur):
        """
        Méthode pour déplacer le loup vers le joueur.

        Args:
            joueur (Joueur): Le joueur à attaquer.
        """
        dx = joueur.rect.centerx - self.rect.centerx
        dy = joueur.rect.centery - self.rect.centery
        distance = math.hypot(dx, dy)

        if distance != 0:
            dx /= distance
            dy /= distance

        self.rect.x += dx * self.vitesse
        self.rect.y += dy * self.vitesse
    
    def attaquer(self, joueur):
        """
        Méthode pour attaquer le joueur.

        Args:
            joueur (Joueur): Le joueur à attaquer.
        """
        joueur.hp -= self.damage
    
    def mourir(self):
        """
        Méthode pour mettre à jour la position du loup à sa mort.
        """
        self.image.fill((0, 0, 0))
        self.rect.x = -100
        self.rect.y = -100
        self.mort = True
        
    def prendre_degats(self, degats):
        """
        Méthode pour prendre des dégâts.

        Args:
            degats (int): Les dégâts infligés au loup.
        """
        self.hp -= degats
        if self.hp <= 0:
            self.mourir()
    
    def obtenir_position(self):
        """
        Méthode pour obtenir la position du loup.

        Returns:
            tuple: Un tuple contenant les coordonnées (x, y) du loup.
        """
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    def update(self, joueur):
        """
        Méthode pour mettre à jour la position du loup.

        Args:
            joueur (Joueur): Le joueur dans le jeu.
        """
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
        
    
        
    
        
    
    
    
