import pygame

#classe entity permettant de créer un objet entity qui se décline en class d'enemy et de joueur
class Entity(pygame.sprite.Sprite):
    def __init__(self, nom, x, y, taille_case, hp, damage, mouvement, path):
        super().__init__()
        self.nom = nom
        self.hp = 100
        self.damage = 10
        self.mouvement = 3
        self.taille_case = taille_case
        self.path = path
        self.image = pygame.image.load(self.path)
        self.image = pygame.transform.scale(self.image, (taille_case, taille_case))
        self.rect = self.image.get_rect()
        self.rect.x = x * taille_case
        self.rect.y = y * taille_case
    
    # Méthode pour obtenir la position des entity
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
        
    
    
    