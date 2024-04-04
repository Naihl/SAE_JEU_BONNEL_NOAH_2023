import pygame
from Entity import Entity
from Enemy import Enemy
from Bottes import Bottes
import Plateau
import math

class IA:
    def __init__(self, joueur, plateau):
        self.joueur = joueur
        self.plateau = plateau

    def jouer_tour(self):
        if self.joueur.nombre_peau < 3:
            # S'il manque du cuir, chercher le cuir le plus proche
            self.se_deplacer_vers("chevre")
        elif self.joueur.nombre_griffes < 2:
            # S'il manque des griffes, chercher les griffes les plus proches
            self.se_deplacer_vers("loup")
        else:
            # Si le joueur a tout ce qu'il faut, se diriger vers la sortie
            self.se_deplacer_vers("temple")

    def se_deplacer_vers(self, ressource):
        # Déterminer les coordonnées du joueur
        x, y = self.joueur.obtenir_position()
        
        # Trouver les cases contenant la ressource recherchée
        cases_ressource = [(i, j) for i in range(self.plateau.largeur) for j in range(self.plateau.hauteur) 
                           if self.plateau.get_case_content(i, j).biome_name == ressource]

        # Trouver la case la plus proche de la ressource
        distance_min = float('inf')
        case_cible = None
        for case in cases_ressource:
            distance = abs(x - case[0]) + abs(y - case[1])
            if distance < distance_min:
                distance_min = distance
                case_cible = case
        
        # Déplacer le joueur vers la case cible
        if case_cible:
            self.joueur.deplacer_vers(case_cible[0], case_cible[1])