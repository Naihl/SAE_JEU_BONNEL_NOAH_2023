import pygame
from Entity import Entity
from Enemy import Enemy
from Bottes import Bottes
import Plateau
import math


#classe joueur permettant de créer un objet joueur
class Joueur(Entity):
    
    def __init__(self, nom, x, y, taille_case, hp, damage, mouvement, path = "img/joueur.png"):
        super().__init__(nom, x, y, taille_case, hp, damage, mouvement, path)  
        self.path = "img/joueur.png"
        self.hp = 100
        self.hp_max = 100
        self.damage = 25
        self.mouvement = 10
        self.nombre_peau = 0
        self.nombre_griffes = 0
        self.inventaire = []

    # Méthode pour déplacer le joueur
    def deplacer(self, dx, dy):
        self.rect.x += dx * self.taille_case
        self.rect.y += dy * self.taille_case
    
    # Méthode pour verifier le déplacement du joueur et voir si il est possible ou non de se déplacer sans sortir de la map
    def verif_deplacement(self, dx, dy, largeur, hauteur):
        if self.rect.x + dx * self.taille_case < 0 or self.rect.x + dx * self.taille_case >= largeur * self.taille_case or self.rect.y + dy * self.taille_case < 0 or self.rect.y + dy * self.taille_case >= hauteur * self.taille_case:
            return False
        else:
            return True
        
    # Méthode pour obtenir la positino du joueur
    def obtenir_position(self):
        return self.rect.x // self.taille_case, self.rect.y // self.taille_case
    
    case_actuelle = property(obtenir_position)
    
    # Methode pour calculer la distance entre deux cases
    def distance_entre_deux_cases(self, case1, case2):
        dx = abs(case1[0] - case2[0])
        dy = abs(case1[1] - case2[1])
        return dx + dy
    
    # Methode pour augmenter le nombre de peau dans l'attribut du joueur
    def augmenter_nombre_peau(self, nombre):
        self.nombre_peau += nombre
        
    # Methode pour augmenter le nombre de griffes dans l'attribut du joueur
    def augmenter_nombre_griffes(self, nombre):
        self.nombre_griffes += nombre
        
    # Methode pour attaquer les ennemies
    def attaquer(self, cible):
        if isinstance(cible, Enemy):
            distance = self.distance_entre_deux_cases(self.case_actuelle, cible.case_actuelle)
            if distance <= 1.0:  
                cible.prendre_degats(self.damage)
    
    # Methode pour mettre l'objet botte dans l'inventaire du joueur
    def ramasser_botte(self, botte):
        self.inventaire.append(botte)
        
    # Methode pour utiliser l'objet botte qui augmente le mouvement du joueur
    def utiliser_botte(self):
        for objet in self.inventaire:
            if isinstance(objet, Bottes):
                self.mouvement += 10
                self.inventaire.remove(objet)  # Retirez la botte de l'inventaire
                print("Vous avez utilisé la botte. Votre mouvement est maintenant de", self.mouvement)
                return
        
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
        
    
    
    