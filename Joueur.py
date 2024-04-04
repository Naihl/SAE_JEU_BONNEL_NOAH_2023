import pygame
from Entity import Entity
from Enemy import Enemy
from Bottes import Bottes
import Plateau
import math

class Joueur(Entity):
    """
    Classe représentant un joueur dans un jeu, héritant de la classe Entity.

    Attributes:
        nom (str): Le nom du joueur.
        x (int): La position horizontale initiale du joueur.
        y (int): La position verticale initiale du joueur.
        taille_case (int): La taille de la case dans laquelle le joueur évolue.
        hp (int): Les points de vie actuels du joueur.
        hp_max (int): Les points de vie maximum du joueur.
        damage (int): Les dégâts infligés par le joueur.
        mouvement (int): La vitesse de déplacement du joueur.
        nombre_peau (int): Le nombre de peaux dans l'inventaire du joueur.
        nombre_griffes (int): Le nombre de griffes dans l'inventaire du joueur.
        inventaire (list): La liste des objets dans l'inventaire du joueur.
    """
    def __init__(self, nom, x, y, taille_case, hp, damage, mouvement, path = "img/joueur.png"):
        """
        Initialise un nouvel objet Joueur.

        Args:
            nom (str): Le nom du joueur.
            x (int): La position horizontale initiale du joueur.
            y (int): La position verticale initiale du joueur.
            taille_case (int): La taille de la case dans laquelle le joueur évolue.
            hp (int): Les points de vie actuels du joueur.
            damage (int): Les dégâts infligés par le joueur.
            mouvement (int): La vitesse de déplacement du joueur.
            path (str, optional): Le chemin vers l'image représentant le joueur. Par défaut, c'est "img/joueur.png".
        """
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)  
        self.path = "img/joueur.png"
        self.hp = 100
        self.hp_max = 100
        self.damage = 25
        self.mouvement = 10
        self.nombre_peau = 0
        self.nombre_griffes = 0
        self.inventaire = []

    def deplacer(self, dx, dy):
        """
        Méthode pour déplacer le joueur.

        Args:
            dx (int): Le déplacement horizontal.
            dy (int): Le déplacement vertical.
        """
        self.rect.x += dx * self.taille_case
        self.rect.y += dy * self.taille_case
    
    def verif_deplacement(self, dx, dy, largeur, hauteur):
        """
        Méthode pour vérifier le déplacement du joueur.

        Args:
            dx (int): Le déplacement horizontal.
            dy (int): Le déplacement vertical.
            largeur (int): La largeur de la carte.
            hauteur (int): La hauteur de la carte.

        Returns:
            bool: True si le déplacement est possible, False sinon.
        """
        if self.rect.x + dx * self.taille_case < 0 or self.rect.x + dx * self.taille_case >= largeur * self.taille_case or self.rect.y + dy * self.taille_case < 0 or self.rect.y + dy * self.taille_case >= hauteur * self.taille_case:
            return False
        else:
            return True
        
    def obtenir_position(self):
        """
        Méthode pour obtenir la position du joueur.

        Returns:
            tuple: Un tuple contenant les coordonnées (x, y) du joueur.
        """
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    case_actuelle = property(obtenir_position)
    
    def distance_entre_deux_cases(self, case1, case2):
        """
        Méthode pour calculer la distance entre deux cases.

        Args:
            case1 (tuple): Les coordonnées de la première case (x, y).
            case2 (tuple): Les coordonnées de la deuxième case (x, y).

        Returns:
            int: La distance entre les deux cases.
        """
        dx = abs(case1[0] - case2[0])
        dy = abs(case1[1] - case2[1])
        return dx + dy
    
    def augmenter_nombre_peau(self, nombre):
        """
        Méthode pour augmenter le nombre de peau dans l'inventaire du joueur.

        Args:
            nombre (int): Le nombre de peaux à ajouter.
        """
        self.nombre_peau += nombre
        
    def augmenter_nombre_griffes(self, nombre):
        """
        Méthode pour augmenter le nombre de griffes dans l'inventaire du joueur.

        Args:
            nombre (int): Le nombre de griffes à ajouter.
        """
        self.nombre_griffes += nombre
        
    def attaquer(self, cible):
        """
        Méthode pour attaquer une cible (ennemi).

        Args:
            cible (Enemy): La cible à attaquer.
        """
        if isinstance(cible, Enemy):
            distance = self.distance_entre_deux_cases(self.case_actuelle, cible.case_actuelle)
            if distance <= 1.0:  
                cible.prendre_degats(self.damage)
    
    def ramasser_botte(self, botte):
        """
        Méthode pour ramasser une paire de bottes et l'ajouter à l'inventaire du joueur.

        Args:
            botte (Bottes): La paire de bottes à ramasser.
        """
        self.inventaire.append(botte)
        
    def utiliser_botte(self):
        """
        Méthode pour utiliser une paire de bottes et augmenter le mouvement du joueur.
        """
        for objet in self.inventaire:
            if isinstance(objet, Bottes):
                self.mouvement += 10
                self.inventaire.remove(objet)  # Retirez la botte de l'inventaire
                print("Vous avez utilisé la botte. Votre mouvement est maintenant de", self.mouvement)
                return
            
    def besoin_cuir(joueur):
        return joueur.nombre_peau < 3

    def besoin_griffes(joueur):
        return joueur.nombre_griffes < 2
        
    @property
    def getx(self):
        return self.x
    
    @getx.setter
    def setx(self, x):
        self.x = x
        
    @property
    def gety(self):
        return self.y
    
    @gety.setter
    def sety(self, y):
        self.y = y
        
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
        
    
    
    