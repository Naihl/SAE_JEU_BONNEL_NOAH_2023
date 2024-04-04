import pygame
import noise
import random
from Case import Case
from Joueur import Joueur
from Enemy import Enemy
from Loup import Loup
from Maraudeur import Maraudeur
from Chevre import Chevre
from Bottes import Bottes

class Plateau:
    """
    Classe représentant le plateau de jeu.

    Attributes:
        largeur (int): La largeur du plateau.
        hauteur (int): La hauteur du plateau.
        taille_case (int): La taille d'une case sur le plateau.
        joueurs (pygame.sprite.Group): Groupe contenant les joueurs sur le plateau.
        enemies (pygame.sprite.Group): Groupe contenant les ennemis sur le plateau.
        objet (pygame.sprite.Group): Groupe contenant les objets sur le plateau.
        fenetre (pygame.Surface): La surface de la fenêtre du jeu.
        terrain (list): Une liste représentant le terrain du plateau.
        biome_tiles (dict): Un dictionnaire contenant les images des biomes du plateau.
        plateau_liste (list): Une liste contenant les objets Case représentant chaque case du plateau.
    """
    def __init__(self, largeur, hauteur, taille_case, joueurs=None, enemies=None, objet=None):
        """
        Initialise un nouvel objet Plateau.

        Args:
            largeur (int): La largeur du plateau.
            hauteur (int): La hauteur du plateau.
            taille_case (int): La taille d'une case sur le plateau.
            joueurs (pygame.sprite.Group): Groupe contenant les joueurs sur le plateau (par défaut None).
            enemies (pygame.sprite.Group): Groupe contenant les ennemis sur le plateau (par défaut None).
            objet (pygame.sprite.Group): Groupe contenant les objets sur le plateau (par défaut None).
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.taille_case = taille_case
        self.joueurs = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.objet = pygame.sprite.Group()

        pygame.init()
        #creation de la fentre
        self.fenetre = pygame.display.set_mode((largeur * taille_case, hauteur * taille_case))
        pygame.display.set_caption("Plateau")

        #appel de la generation du terrain
        self.terrain = self.generer_terrain()

        #creation des images des biomes(briome = type de terrain/case)
        self.biome_tiles = {
            "blue": pygame.image.load("img/blue.jpg"),  
            "dirt": pygame.image.load("img/sand.png"),  
            "grass": pygame.image.load("img/grass.png"),  
            "slow": pygame.image.load("img/slow.png"),  
            "sand": pygame.image.load("img/sand.jpg"), 
            "temple": pygame.image.load("img/temple.jpg")
        }

        #redimensionnement des images des biomes
        for biome_name in self.biome_tiles:
            self.biome_tiles[biome_name] = pygame.transform.scale(self.biome_tiles[biome_name], (taille_case, taille_case))
        
        #stockage du plateau dans une liste
        self.plateau_liste = self.afficher_plateau()
        
        
        

    def placer_joueur(self, joueur : Joueur, x : int, y : int):
        """
        Place un joueur sur le plateau aux coordonnées spécifiées.

        Args:
            joueur (Joueur): L'instance du joueur à placer.
            x (int): La coordonnée x où placer le joueur.
            y (int): La coordonnée y où placer le joueur.
        """
        joueur.rect.x = x * self.taille_case
        joueur.rect.y = y * self.taille_case
        self.joueurs.add(joueur)
    
    def placer_enemies(self, enemies : Enemy, x : int, y : int):
        """
        Place un ennemi sur le plateau aux coordonnées spécifiées.

        Args:
            enemies (Enemy): L'instance de l'ennemi à placer.
            x (int): La coordonnée x où placer l'ennemi.
            y (int): La coordonnée y où placer l'ennemi.
        """
        enemies.rect.x = x * self.taille_case
        enemies.rect.y = y * self.taille_case
        self.enemies.add(enemies)
    
    def placer_objet(self, objet, x : int, y : int):
        """
        Place un objet sur le plateau aux coordonnées spécifiées.

        Args:
            objet (Bottes): L'instance de l'objet à placer.
            x (int): La coordonnée x où placer l'objet.
            y (int): La coordonnée y où placer l'objet.
        """
        objet.rect.x = x * self.taille_case
        objet.rect.y = y * self.taille_case
        self.objet.add(objet)

    def generer_terrain(self):
        """
        Génère le terrain du plateau en utilisant le bruit de Perlin.
        """
        terrain = [[0 for _ in range(self.largeur)] for _ in range(self.hauteur)]
        scale = 25.0
        octaves = 2
        #creation de l'aleatoire pour le bruit de perlin
        lacunarity = random.uniform(2.0, 4.0)
        persistence = random.uniform(1.0, 2.0)

        for x in range(self.largeur):
            for y in range(self.hauteur):
                value = noise.pnoise2(x / scale, y / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeatx=self.largeur, repeaty=self.hauteur, base=0)
                biome_name = self.set_biome(value)
                terrain[y][x] = biome_name

        return terrain

    def set_biome(self, value):
        """
        Détermine le biome en fonction de la valeur fournie.

        Args:
            value (float): La valeur utilisée pour déterminer le biome.

        Returns:
            str: Le nom du biome correspondant à la valeur fournie.
        """
        if value < -0.07:
            return "slow"
        elif value < 0:
            return "dirt"
        elif value < 0.25:
            return "grass"
        elif value < 0.5:
            return "blue"
        else:
            return "sand"

    def get_biome(self, x, y):
        """
        Obtient le biome d'une case spécifique sur le plateau.

        Args:
            x (int): La coordonnée x de la case.
            y (int): La coordonnée y de la case.

        Returns:
            str: Le nom du biome de la case spécifiée.
        """
        return self.terrain[y][x]
    
    def get_case_content(self, x, y) -> Case: 
        """
        Obtient le contenu d'une case spécifique sur le plateau.

        Args:
            x (int): La coordonnée x de la case.
            y (int): La coordonnée y de la case.

        Returns:
            Case: L'objet Case représentant le contenu de la case spécifiée, ou None si la case est vide.
        """
        for case in self.plateau_liste:
            if case.x == x and case.y == y:
                return case
        return None

    def afficher_plateau(self):
        """
        Affiche le plateau de jeu avec ses biomes, joueurs, ennemis et objets.
        
        Returns:
            list: Une liste d'objets Case représentant le contenu de chaque case du plateau.
        """
        plateau_list = []
        for x in range(self.largeur):
            for y in range(self.hauteur):
                biome_name = self.terrain[y][x]
                tile_biome = self.biome_tiles[biome_name]
                self.fenetre.blit(tile_biome, (x * self.taille_case, y * self.taille_case)) 
                plateau_list.append(Case(biome_name,x, y))
                
        #ajout de la sortie (fin)
        
        self.fenetre.blit(self.biome_tiles["temple"], (31 * self.taille_case,31 * self.taille_case))
        plateau_list[2015] = Case("temple", 31, 31 )

        
        # Dessine les joueurs sur le plateau
        self.joueurs.draw(self.fenetre)
        self.enemies.draw(self.fenetre)
        self.objet.draw(self.fenetre)
        
            

        

        pygame.display.flip()
        return plateau_list
    
    def zoomer_plateau(self, joueur : Joueur):
        plateau_list = []
        vision_joueur = 10
        for x in range(-vision_joueur,vision_joueur+1):
            for y in range(-vision_joueur,vision_joueur+1):
                biome_name = self.terrain[joueur.case_actuelle[0]+y][joueur.case_actuelle[1]+x]
                tile_biome = self.biome_tiles[biome_name]
                self.fenetre.blit(tile_biome, (x*self.taille_case, y * self.taille_case))
                plateau_list.append(Case(biome_name,x,y))

    def runner(self):
        """
        Boucle principale du jeu qui affiche continuellement le plateau jusqu'à ce que le joueur quitte le jeu.
        """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.afficher_plateau()

        pygame.quit()


    

