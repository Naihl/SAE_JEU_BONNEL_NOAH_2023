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

# Classe pour le plateau de jeu
class Plateau:
    def __init__(self, largeur, hauteur, taille_case, joueurs=None, enemies=None, objet=None):
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
            "dirt": pygame.image.load("img/sand.jpg"),  
            "grass": pygame.image.load("img/grass.jpg"),  
            "slow": pygame.image.load("img/slow.jpg"),  
            "sand": pygame.image.load("img/sand.jpg"), 
            "temple": pygame.image.load("img/temple.jpg")
        }

        #redimensionnement des images des biomes
        for biome_name in self.biome_tiles:
            self.biome_tiles[biome_name] = pygame.transform.scale(self.biome_tiles[biome_name], (taille_case, taille_case))
        
        #stockage du plateau dans une liste
        self.plateau_liste = self.afficher_plateau()
        
        
        

    # Méthode pour placer un joueur sur le plateau
    def placer_joueur(self, joueur, x, y):
        joueur.rect.x = x * self.taille_case
        joueur.rect.y = y * self.taille_case
        self.joueurs.add(joueur)
    
    # Méthode pour placer un enemy sur le plateau
    def placer_enemies(self, enemies, x, y):
        enemies.rect.x = x * self.taille_case
        enemies.rect.y = y * self.taille_case
        self.enemies.add(enemies)
    
    # Méthode pour placer un objet sur le plateau
    def placer_objet(self, objet, x, y):
        objet.rect.x = x * self.taille_case
        objet.rect.y = y * self.taille_case
        self.objet.add(objet)

    # Méthode pour générer le terrain en bruit de perlin
    def generer_terrain(self):
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

    # Méthode pour définir les biomes
    def set_biome(self, value):
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

    # Méthode pour obtenir le biome d'une case
    def get_biome(self, x, y):
        return self.terrain[y][x]
    
    # Méthode pour obtenir le contenu d'une case
    def get_case_content(self, x, y):
        for case in self.plateau_liste:
            if case.x == x and case.y == y:
                return case
        return None

    # Méthode pour afficher le plateau
    def afficher_plateau(self):
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


    # Boucle Principale	
    def runner(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.afficher_plateau()

        pygame.quit()


    

