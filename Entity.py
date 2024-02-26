import pygame

class Entity(pygame.sprite.Sprite):
    """
    Classe représentant une entité dans un jeu, pouvant être utilisée pour créer des ennemis ou des joueurs.

    Attributes:
        nom (str): Le nom de l'entité.
        hp (int): Les points de vie de l'entité.
        damage (int): Les dégâts infligés par l'entité.
        mouvement (int): La vitesse de déplacement de l'entité.
        taille_case (int): La taille de la case dans laquelle l'entité évolue.
        path (str): Le chemin vers l'image représentant l'entité.
        image (pygame.Surface): L'image représentant l'entité.
        rect (pygame.Rect): Le rectangle de collision de l'entité.
    """
    def __init__(self, nom, x, y, taille_case, hp, damage, mouvement, path):
        """
        Initialise un nouvel objet Entity.

        Args:
            nom (str): Le nom de l'entité.
            x (int): La position horizontale initiale de l'entité.
            y (int): La position verticale initiale de l'entité.
            taille_case (int): La taille de la case dans laquelle l'entité évolue.
            hp (int): Les points de vie de l'entité.
            damage (int): Les dégâts infligés par l'entité.
            mouvement (int): La vitesse de déplacement de l'entité.
            path (str): Le chemin vers l'image représentant l'entité.
        """
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
    
    def deplacer(self, dx, dy):
        """
        Méthode pour déplacer l'entité.

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
        
    
    
    