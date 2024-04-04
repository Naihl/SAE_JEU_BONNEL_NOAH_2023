"""
Fichier principal du jeu "King of Sand".

Ce fichier contient les définitions des fonctions principales du jeu ainsi que
l'initialisation des variables et des objets nécessaires au fonctionnement du jeu.

Auteur: Naihl
Date de création: 2023

"""

from turtle import Screen
import pygame
import sys
import pygame_gui
import pygame.font
from Plateau import Plateau
from Joueur import Joueur
from Chevre import Chevre
import random
from HealthBar import HealthBar
from UpdateText import UpdateText
from Bottes import Bottes
from Coeur import Coeur
from Loup import Loup
from Maraudeur import Maraudeur
import subprocess
import math
import time  # Importer le module time pour la fonction d'attente



# Initialisation des variables du plateau
largeur_plateau = 64
hauteur_plateau = 64
taille_case = 10

plateau = Plateau(largeur_plateau, hauteur_plateau, taille_case)

# Initialisation de la fenêtre principale
largeur_main = largeur_plateau * taille_case + 150
hauteur_main = hauteur_plateau * taille_case + 150

fenetre_main = pygame.display.set_mode((largeur_main + plateau.largeur * plateau.taille_case - 200, hauteur_main ))
pygame.display.set_caption("King of Sand")


def afficher_menu():
    fenetre_main.fill((87, 80, 66))
    
    # Chargement de l'image d'arrière-plan
    image_arriere_plan = pygame.image.load("img/background15.png").convert()  # Assurez-vous que "arriere_plan.jpg" est le chemin correct vers votre image
    image_arriere_plan = pygame.transform.scale(image_arriere_plan, (largeur_main + 600, hauteur_main))
    fenetre_main.blit(image_arriere_plan, (0, 0))
    
    font = pygame.font.SysFont('comicsansms', 45)  # Utilisation de la police "Comic Sans MS"
    text1 = font.render("Choisissez le nombre de joueurs (entre 1 et 4):", True, (0, 0, 0))  # Texte blanc
    text_rect = text1.get_rect(center=((largeur_main + 300) // 2, 250))  # Centrage du texte horizontalement
    fenetre_main.blit(text1, text_rect)
    pygame.display.flip()
    nb_ia = 3
    nb_joueurs = 1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    nb_joueurs = 1
                elif event.key == pygame.K_2:
                    nb_joueurs = 2
                elif event.key == pygame.K_3:
                    nb_joueurs = 3
                elif event.key == pygame.K_4:
                    nb_joueurs = 4
                elif event.key == pygame.K_RETURN:
                    return nb_joueurs, 4 - nb_joueurs

        font = pygame.font.SysFont('comicsansms', 40)  # Utilisation de la même police pour le texte
        pygame.display.flip()


def joueurs_adjacents(joueur1, joueur2):
    """
    Vérifie si deux joueurs sont adjacents sur le plateau.

    Args:
        joueur1 (Joueur): Le premier joueur.
        joueur2 (Joueur): Le deuxième joueur.

    Returns:
        bool: True si les joueurs sont adjacents, False sinon.
    """
    x1, y1 = joueur1.obtenir_position()
    x2, y2 = joueur2.obtenir_position()
    return abs(x1 - x2) + abs(y1 - y2) == 1



def deplacer_loups_vers_joueur(joueur, loups):
    """
    Déplace les loups vers un joueur donné.

    Args:
        joueur (Joueur): Le joueur vers lequel les loups doivent être déplacés.
        loups (list): Liste des loups à déplacer.
    """
    # Parcours tous les loups
    for loup in loups:
        if loup.hp <= 0:
            continue
        joueur_plus_proche = None
        distance_min = float('inf')
        loup_x, loup_y = loup.obtenir_position()

        for joueur in joueurs:
            joueur_x, joueur_y = joueur.obtenir_position()
            distance = abs(joueur_x - loup_x) + abs(joueur_y - loup_y)
            if distance < distance_min:
                distance_min = distance
                joueur_plus_proche = joueur

        if joueur_plus_proche:
            joueur_x, joueur_y = joueur_plus_proche.obtenir_position()
            deplacement_x = 0 if joueur_x == loup_x else (joueur_x - loup_x) // abs(joueur_x - loup_x)
            deplacement_y = 0 if joueur_y == loup_y else (joueur_y - loup_y) // abs(joueur_y - loup_y)
            loup.deplacer(deplacement_x, deplacement_y)
            if abs(joueur_x - loup_x) + abs(joueur_y - loup_y) <= 1:
                loup.attaquer(joueur_plus_proche)  # Le loup attaque le joueur s'il est à portée

        
        
            
# fonction permettant de deplacer les maraudeurs vers le joueur
def deplacer_maraudeurs_vers_joueur(joueur, maraudeurs):
    """
    Déplace les maraudeurs vers un joueur donné.

    Args:
        joueur (Joueur): Le joueur vers lequel les maraudeurs doivent être déplacés.
        maraudeurs (list): Liste des maraudeurs à déplacer.
    """
    # Parcours tous les maraudeurs
    for maraudeur in maraudeurs:
        # Ignore les maraudeurs déjà éliminés
        if maraudeur.hp <= 0:
            continue  
        joueur_x, joueur_y = joueur.obtenir_position()
        maraudeur_x, maraudeur_y = maraudeur.obtenir_position()
        deplacement_x = 0
        deplacement_y = 0

        # Vérifie si le maraudeur est sur une case
        case_maraudeur = plateau.get_case_content(maraudeur_x, maraudeur_y)
        if case_maraudeur is not None:
            if joueur_x < maraudeur_x:
                if plateau.get_case_content(maraudeur_x -1, maraudeur_y).biome_name == "blue":
                    break
                else:
                    deplacement_x = -1
            elif joueur_x > maraudeur_x:
                if plateau.get_case_content(maraudeur_x +1, maraudeur_y).biome_name == "blue":
                    break
                else:
                    deplacement_x = 1

            if joueur_y < maraudeur_y:
                if plateau.get_case_content(maraudeur_x, maraudeur_y -1).biome_name == "blue":
                    break
                else:
                    deplacement_y = -1
            elif joueur_y > maraudeur_y:
                if plateau.get_case_content(maraudeur_x, maraudeur_y +1).biome_name == "blue":
                    break
                else:
                    deplacement_y = 1

        if abs(joueur_x - maraudeur_x) + abs(joueur_y - maraudeur_y) <= 5:
            maraudeur.attaquer(joueur)  # Le maraudeur attaque le joueur s'il est à portée
        else:
            maraudeur.deplacer(deplacement_x, deplacement_y)

def tour_joueur(joueuractuel):
    """
    Change le tour des joueurs dans l'ordre prédéfini.

    Args:
        joueuractuel (Joueur): Le joueur dont c'est actuellement le tour.

    Returns:
        Joueur: Le joueur dont le tour est à venir.
    """
    if joueuractuel == joueur1:
        deplacer_loups_vers_joueur(joueuractuel, loups)
        deplacer_maraudeurs_vers_joueur(joueuractuel, maraudeurs)
        joueuractuel = joueur2
        updatetext.render(joueuractuel)
    elif joueuractuel == joueur2:
        deplacer_loups_vers_joueur(joueuractuel, loups)
        deplacer_maraudeurs_vers_joueur(joueuractuel, maraudeurs)
        joueuractuel = joueur3
        updatetext.render(joueuractuel)
    elif joueuractuel == joueur3:
        deplacer_loups_vers_joueur(joueuractuel, loups)
        deplacer_maraudeurs_vers_joueur(joueuractuel, maraudeurs)
        joueuractuel = joueur4
        updatetext.render(joueuractuel)
    elif joueuractuel == joueur4:
        deplacer_loups_vers_joueur(joueuractuel, loups)
        deplacer_maraudeurs_vers_joueur(joueuractuel, maraudeurs)
        joueuractuel = joueur1
        updatetext.render(joueuractuel)
    return joueuractuel

# fonction permettant de generer une position aleatoirement
def position_random(a,b,c,d):
    """
    Génère une position aléatoire dans les limites spécifiées.

    Args:
        a (int): Limite inférieure en x.
        b (int): Limite supérieure en x.
        c (int): Limite inférieure en y.
        d (int): Limite supérieure en y.

    Returns:
        tuple: Un tuple contenant les coordonnées x et y générées aléatoirement.
    """
    while True:
        x, y = random.randint(a, b), random.randint(c, d)
        #on verifie que la case n'est pas impossible d'acces
        if plateau.get_case_content(x, y).biome_name != "blue":
            break
    return x, y


# fonction permettant de generer les chèvres aleatoirement
def generer_chevres(nombre_de_chevres):
    """
    Génère des chèvres de manière aléatoire sur le plateau.

    Args:
        nombre_de_chevres (int): Le nombre de chèvres à générer.

    Returns:
        list: Une liste contenant les objets chèvre générés.
    """
    chevres = []
    for _ in range(nombre_de_chevres):
        x_chevre, y_chevre = position_random(0, 63, 0, 63  )
        chevre = Chevre("chevre", x_chevre, y_chevre, 10, 100, 10, 3, "img/chevre.png")
        plateau.placer_enemies(chevre, x_chevre, y_chevre)
        chevres.append(chevre)
    return chevres

# Crée  10 chèvres 
chevres = generer_chevres(10)

def generer_loups(nombre_de_loups):
    """
    Génère des loups de manière aléatoire sur le plateau.

    Args:
        nombre_de_loups (int): Le nombre de loups à générer.

    Returns:
        list: Une liste contenant les objets loup générés.
    """
    loups = []
    for _ in range(nombre_de_loups):
        x_loup, y_loup = position_random(0, 63, 0, 63)
        loup = Loup("loup", x_loup, y_loup, 10, 100, 30, 3, "img/loup.png")
        plateau.placer_enemies(loup, x_loup, y_loup)
        loups.append(loup)
    return loups
    
# Crée 10 loups
loups = generer_loups(10)  

def generer_maraudeurs(nombre_de_maraudeurs):
    """
    Génère des maraudeurs de manière aléatoire sur le plateau.

    Args:
        nombre_de_maraudeurs (int): Le nombre de maraudeurs à générer.

    Returns:
        list: Une liste contenant les objets maraudeur générés.
    """
    maraudeurs = []
    for _ in range(nombre_de_maraudeurs):
        x_maraudeur, y_maraudeur = position_random(28, 36, 28, 36)
        maraudeur = Maraudeur("maraudeur", x_maraudeur, y_maraudeur, 10, 150, 15, 2, "img/maraudeur.png")
        plateau.placer_enemies(maraudeur, x_maraudeur, y_maraudeur)
        maraudeurs.append(maraudeur)
    return maraudeurs

# Crée 3 maraudeurs
maraudeurs = generer_maraudeurs(3)  

def generer_coeurs(nombre_de_coeurs):
    """
    Génère des coeurs de manière aléatoire sur le plateau.

    Args:
        nombre_de_coeurs (int): Le nombre de coeurs à générer.

    Returns:
        list: Une liste contenant les objets coeur générés.
    """
    coeurs = []

    nombre_de_coeurs = 10  
    for _ in range(nombre_de_coeurs):
        x_coeur, y_coeur = position_random(0, 63, 0, 63)
        coeur = Coeur(x_coeur, y_coeur, taille_case)
        plateau.placer_objet(coeur, x_coeur, y_coeur)
        coeurs.append(coeur)
    return coeurs

# Crée 20 coeurs
coeurs = generer_coeurs(20)  

def generer_bottes(nombre_de_bottes):
    """
    Génère des bottes de manière aléatoire sur le plateau.

    Args:
        nombre_de_bottes (int): Le nombre de bottes à générer.

    Returns:
        list: Une liste contenant les objets bottes générés.
    """
    bottes = []

    nombre_de_bottes = 10  
    for _ in range(nombre_de_bottes):
        x_botte, y_botte = position_random(0, 63, 0, 63)
        botte = Bottes(x_botte, y_botte)
        plateau.placer_objet(botte, x_botte, y_botte)
        bottes.append(botte)
    return bottes

# Crée 20 bottes
bottes = generer_bottes(20) 



def faire_tour_ia(joueuractuel):
    joueur_x, joueur_y = joueuractuel.obtenir_position()
    loup_cible = None
    cible_chevre = None
    cible_joueur = None
    vie_joueur = joueuractuel.hp
    distance_min = float('inf')

    

    if vie_joueur <= joueuractuel.hp_max // 2:  # Si le joueur a la moitié ou moins de sa vie
        for coeur in coeurs:
            coeur_x, coeur_y = coeur.obtenir_position()
            distance = abs(joueur_x - coeur_x) + abs(joueur_y - coeur_y)
            if distance < distance_min:
                distance_min = distance
                cible_coeur = coeur

        # Si un coeur a été trouvé, déplacez le joueur vers ce coeur
        if cible_coeur:
            coeur_x, coeur_y = cible_coeur.obtenir_position()
            deplacement_x = 0 if joueur_x == coeur_x else (coeur_x - joueur_x) // abs(coeur_x - joueur_x)
            deplacement_y = 0 if joueur_y == coeur_y else (coeur_y - joueur_y) // abs(coeur_y - joueur_y)
            joueuractuel.deplacer(deplacement_x, deplacement_y)
            joueuractuel.mouvement -= 1
            if plateau.get_case_content(joueur_x, joueur_y).biome_name == "dirt":
                joueuractuel.hp -= 5
            # Mettre à jour la vie du joueur après avoir pris le coeur
            joueuractuel.hp += 50
            if joueuractuel.hp > joueuractuel.hp_max:
                joueuractuel.hp = joueuractuel.hp_max
            # Supprimer le coeur de la liste des coeurs disponibles
            coeurs.remove(cible_coeur)

    if joueuractuel.besoin_griffes():
        for loup in loups:
            if loup.hp <= 0:
                continue
            loup_x, loup_y = loup.obtenir_position()
            distance = abs(joueur_x - loup_x) + abs(joueur_y - loup_y)
            if distance < distance_min:
                distance_min = distance
                loup_cible = loup

        # Si un loup a été trouvé, déplace le joueur vers ce loup
        if loup_cible:
            loup_x, loup_y = loup_cible.obtenir_position()
            deplacement_x = 0 if joueur_x == loup_x else (loup_x - joueur_x) // abs(loup_x - joueur_x)
            deplacement_y = 0 if joueur_y == loup_y else (loup_y - joueur_y) // abs(loup_y - joueur_y)
            joueuractuel.deplacer(deplacement_x, deplacement_y)
            joueuractuel.mouvement -= 1
            if plateau.get_case_content(joueur_x, joueur_y).biome_name == "dirt":
                joueuractuel.hp -= 5
            if abs(loup_x - joueur_x) + abs(loup_y - joueur_y) <= 1:
                joueuractuel.attaquer(loup_cible)  # Le joueur attaque le loup s'il est à portée
    
    if joueuractuel.besoin_cuir():
        for chevre in chevres:
            chevre_x, chevre_y = chevre.obtenir_position()
            distance = abs(joueur_x - chevre_x) + abs(joueur_y - chevre_y)
            if distance < distance_min:
                distance_min = distance
                cible_chevre = chevre

        # Si une chèvre a été trouvée, déplacez le joueur vers cette chèvre
        if cible_chevre:
            chevre_x, chevre_y = cible_chevre.obtenir_position()
            deplacement_x = 0 if joueur_x == chevre_x else (chevre_x - joueur_x) // abs(chevre_x - joueur_x)
            deplacement_y = 0 if joueur_y == chevre_y else (chevre_y - joueur_y) // abs(chevre_y - joueur_y)
            joueuractuel.deplacer(deplacement_x, deplacement_y)
            joueuractuel.mouvement -= 1
            if plateau.get_case_content(joueur_x, joueur_y).biome_name == "dirt":
                joueuractuel.hp -= 5
            if abs(chevre_x - joueur_x) + abs(chevre_y - joueur_y) <= 1:
                joueuractuel.attaquer(cible_chevre)  # Le joueur attaque la chèvre s'il est à portée
        
    
    # Si le joueur a tout il va vers la sortie
    if joueuractuel.besoin_cuir() == False and joueuractuel.besoin_griffes() == False:
        cible_sortie_x, cible_sortie_y = 31,31
        joueuractuel.deplacer(cible_sortie_x, cible_sortie_y)
        joueuractuel.mouvement -= 1
        if plateau.get_case_content(joueur_x, joueur_y).biome_name == "dirt":
                joueuractuel.hp -= 5
        
    if plateau.get_case_content(joueur_x, joueur_y).biome_name == "temple" and joueuractuel.nombre_peau >= 3 and joueuractuel.nombre_griffes >= 2:
            pygame.quit()
            subprocess.run(["python", "victoire.py"])

    if joueur1.hp <= 0:
        plateau.placer_joueur(joueur1, x1, y1)
        joueur1.hp = 100
        joueur1.nombre_peau = 0
        joueur1.nombre_griffes = 0
        joueur1.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    if joueur2.hp <= 0:
        plateau.placer_joueur(joueur2, x2, y2)
        joueur2.hp = 100
        joueur2.nombre_peau = 0
        joueur2.nombre_griffes = 0
        joueur2.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    if joueur3.hp <= 0:
        plateau.placer_joueur(joueur3, x3, y3)
        joueur3.hp = 100
        joueur3.nombre_peau = 0
        joueur3.nombre_griffes = 0
        joueur3.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    if joueur4.hp <= 0:
        plateau.placer_joueur(joueur4, x4, y4)
        joueur4.hp = 100
        joueur4.nombre_peau = 0
        joueur4.nombre_griffes = 0
        joueur4.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    # Mettez à jour l'affichage après le déplacement du joueur
    pygame.display.flip()
        
    if joueuractuel.mouvement >0:
        faire_tour_ia(joueuractuel)



def trouver_cuir_plus_proche(joueur_x, joueur_y):
    plus_proche_distance = float('inf')
    plus_proche_cuir = None
    for chevre in chevres:
        chevre_x, chevre_y = chevre.obtenir_position()
        distance = distance_entre(joueur_x, joueur_y, chevre_x, chevre_y)
        if distance < plus_proche_distance:
            plus_proche_distance = distance
            plus_proche_cuir = chevre
    return plus_proche_cuir.x, plus_proche_cuir.y

def trouver_griffes_plus_proches(joueur_x, joueur_y):
    plus_proche_distance = float('inf')
    plus_proche_griffes = None
    for loup in loups:
        loup_x, loup_y = loup.obtenir_position()
        distance = distance_entre(joueur_x, joueur_y, loup_x, loup_y)
        if distance < plus_proche_distance:
            plus_proche_distance = distance
            plus_proche_griffes = loup
    return plus_proche_griffes.x, plus_proche_griffes.y



def deplacer_vers(joueur, cible_x, cible_y):
    joueur.x = cible_x
    joueur.y = cible_y
    
def distance_entre(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


nb_joueurs, nb_ia = afficher_menu()
print(nb_joueurs, nb_ia)


# Initialisation des joueurs
joueurs = []  # Création de la liste pour stocker les joueurs
is_ia = []  # Liste pour stocker si un joueur est une IA ou non

x1, y1 = position_random(0, 15, 0, 15)
joueur1 = Joueur("Joueur 1", x1, y1, 10, 100, 10, 5)
positionx_originale_joueur1 = x1
positiony_originale_joueur1 = y1
plateau.placer_joueur(joueur1, x1, y1)
joueurs.append(joueur1)


x2, y2 = position_random(48, 63, 0, 15)
joueur2 = Joueur("Joueur 2", x2, y2, 10, 100, 10, 5)
positionx_originale_joueur2 = x2
positiony_originale_joueur2 = y2
plateau.placer_joueur(joueur2, x2, y2)
joueurs.append(joueur2)


x3, y3 = position_random(0, 15, 48, 63)
joueur3 = Joueur("Joueur 3", x3, y3, 10, 100, 10, 5)
positionx_originale_joueur3 = x3
positiony_originale_joueur3 = y3
plateau.placer_joueur(joueur3, x3, y3)
joueurs.append(joueur3)


x4, y4 = position_random(48, 63, 48, 63)
joueur4 = Joueur("Joueur 4", x4, y4, 10, 100, 10, 5)
positionx_originale_joueur4 = x4
positiony_originale_joueur4 = y4
plateau.placer_joueur(joueur4, x4, y4)
joueurs.append(joueur4)

if nb_ia == 1:
    is_ia.append("Joueur 4")
elif nb_ia == 2:
    is_ia.append("Joueur 3")
    is_ia.append("Joueur 4")
elif nb_ia == 3:
    is_ia.append("Joueur 2")
    is_ia.append("Joueur 3")
    is_ia.append("Joueur 4")
else:
    is_ia = []

print(is_ia)






# Initialisation des variables de la fenêtre principale
fenetre_main.fill((77, 149, 203))
joueuractuel = joueur1


current_time = pygame.time.get_ticks()
last_update_time = current_time
clock = pygame.time.Clock()

   
updatetext = UpdateText(fenetre_main, joueur1, joueur2, joueur3, joueur4)

    
police = pygame.font.Font(None, 36)  # Charge une police (taille 36, police par défaut)


updatetext.render(joueuractuel)

healthbar1 = HealthBar(fenetre_main, joueur1, 700, 100)
healthbar2 = HealthBar(fenetre_main, joueur2, 700, 250)
healthbar3 = HealthBar(fenetre_main, joueur3, 700, 400)
healthbar4 = HealthBar(fenetre_main, joueur4, 700, 550)

# Boucle principale
running = True
while running:
    clock.tick(60)  
    if current_time - last_update_time >= 100:
        last_update_time = current_time
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        touches = pygame.key.get_pressed()
        joueur_x, joueur_y = joueuractuel.obtenir_position()

        # si le joueur à des mouvements restants
        if joueuractuel.mouvement > 0:
            
            if joueuractuel.nom in is_ia:
            # Si le joueur actuel est une IA, exécutez le code correspondant pour l'IA
            # Par exemple :
                faire_tour_ia(joueuractuel)  # Cette fonction doit être définie pour exécuter le tour de l'IA
            
            #mouvement gauche
            if touches[pygame.K_LEFT]:
                if joueuractuel.verif_deplacement(-1, +0, largeur_plateau, hauteur_plateau):
                    #si le joueur n'est pas sur une case bleue il peut se deplacer
                    if plateau.get_case_content(joueur_x - 1, joueur_y).biome_name != "blue":
                        joueuractuel.deplacer(-1, +0)
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case slow il perd un mouvement
                    if plateau.get_case_content(joueur_x - 1, joueur_y).biome_name == "slow":
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case dirt il perd 5 hp
                    if plateau.get_case_content(joueur_x - 1, joueur_y).biome_name == "dirt":
                        joueuractuel.hp -= 5
                        largeur_barre_actuelle = joueuractuel.hp * 2
                        rect_barre_actuelle = (700, 100, largeur_barre_actuelle, 20)
                    
                    
                    
                        
                        #mouvement droite
            elif touches[pygame.K_RIGHT]:
                if joueuractuel.verif_deplacement(+1, +0, largeur_plateau, hauteur_plateau):
                    #si le joueur n'est pas sur une case bleue il peut se deplacer
                    if plateau.get_case_content(joueur_x + 1, joueur_y).biome_name != "blue":
                        joueuractuel.deplacer(+1, +0)
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case slow il perd un mouvement
                    if plateau.get_case_content(joueur_x + 1, joueur_y).biome_name == "slow":
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case dirt il perd 5 hp
                    if plateau.get_case_content(joueur_x + 1, joueur_y).biome_name == "dirt":
                        joueuractuel.hp -= 5
                        largeur_barre_actuelle = joueuractuel.hp * 2
                        rect_barre_actuelle = (700, 100, largeur_barre_actuelle, 20)
                    
                    
                    #mouvement haut
            elif touches[pygame.K_UP]:
                if joueuractuel.verif_deplacement(+0, -1, largeur_plateau, hauteur_plateau):
                    #si le joueur n'est pas sur une case bleue il peut se deplacer
                    if plateau.get_case_content(joueur_x, joueur_y -1).biome_name != "blue":
                        joueuractuel.deplacer(+0, -1)
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case slow il perd un mouvement
                    if plateau.get_case_content(joueur_x, joueur_y - 1).biome_name == "slow":
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case dirt il perd 5 hp
                    if plateau.get_case_content(joueur_x, joueur_y - 1).biome_name == "dirt":
                        joueuractuel.hp -= 5
                        largeur_barre_actuelle = joueuractuel.hp * 2
                        rect_barre_actuelle = (700, 100, largeur_barre_actuelle, 20)
                        
                    
                    #mouvement bas
            elif touches[pygame.K_DOWN]:
                if joueuractuel.verif_deplacement(+0, +1, largeur_plateau, hauteur_plateau):
                    #si le joueur n'est pas sur une case bleue il peut se deplacer
                    if plateau.get_case_content(joueur_x, joueur_y +1).biome_name != "blue":
                        joueuractuel.deplacer(+0, +1)
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case slow il perd un mouvement
                    if plateau.get_case_content(joueur_x, joueur_y +1).biome_name == "slow":  
                        joueuractuel.mouvement -= 1
                        updatetext.render(joueuractuel)
                        #si le joueur est sur une case dirt il perd 5 hp
                    if plateau.get_case_content(joueur_x, joueur_y +1).biome_name == "dirt":  
                        joueuractuel.hp -= 5
                        largeur_barre_actuelle = joueuractuel.hp * 2
                        rect_barre_actuelle = (700, 100, largeur_barre_actuelle, 20)
                        
                #attaque
            elif touches[pygame.K_SPACE]:
                # Parcoure toutes les chèvres
                for chevre in chevres:
                    chevre_x, chevre_y = chevre.obtenir_position()
                    joueur_x, joueur_y = joueuractuel.obtenir_position()
                    distance_x = abs(joueur_x - chevre_x)
                    distance_y = abs(joueur_y - chevre_y)

                    # Vérifiez si la chèvre est à maximum une case d'écart du joueur
                    if distance_x <= 1 and distance_y <= 1:
                        joueuractuel.attaquer(chevre)
                        joueuractuel.mouvement -= 0.5
                        updatetext.render(joueuractuel)
                        break  
                    
                    # Parcoure tous les loups
                for loup in loups:
                    if loup.hp > 0:  
                        joueur_x, joueur_y = joueuractuel.obtenir_position()
                        loup_x, loup_y = loup.obtenir_position()
                        distance_x = abs(joueur_x - loup_x)
                        distance_y = abs(joueur_y - loup_y)

                        # Vérifiez si le joueur est à moins d'une case d'un loup
                        if distance_x <= 1 and distance_y <= 1:
                            joueuractuel.attaquer(loup)
                            joueuractuel.mouvement -= 0.5
                            updatetext.render(joueuractuel)
                            break  
                    
                    # Parcoure tous les maraudeurs
                for maraudeur in maraudeurs:
                    if maraudeur.hp > 0:
                        joueur_x, joueur_y = joueuractuel.obtenir_position()
                        maraudeur_x, maraudeur_y = maraudeur.obtenir_position()
                        distance_x = abs(joueur_x - maraudeur_x)
                        distance_y = abs(joueur_y - maraudeur_y)

                        # Vérifiez si le joueur est à moins d'une case d'un loup
                        if distance_x <= 1 and distance_y <= 1:
                            joueuractuel.attaquer(maraudeur)
                            joueuractuel.mouvement -= 0.5
                            updatetext.render(joueuractuel)
                            break  

                # permet de voir si le joueur est à coté d'un autre joueur pour l'attaquer
                for autre_joueur in [joueur2, joueur3, joueur4]:
                    if autre_joueur != joueuractuel and joueurs_adjacents(joueuractuel, autre_joueur):
                        autre_joueur.hp -= 15
                        if autre_joueur.hp < 0:
                            autre_joueur.hp = 0

         #permet de ramasser les bottes
         #parcourt toutes les bottes
        for botte in bottes:        
            if joueuractuel.rect.x == botte.rect.x and joueuractuel.rect.y == botte.rect.y:
                joueuractuel.ramasser_botte(botte)
                x5, y5 = position_random(0, 63, 0, 63)
                positionx_originale_joueur5 = x5
                positiony_originale_joueur5 = y5
                plateau.placer_objet(botte, x5, y5)
                updatetext.render(joueuractuel)

                
        #permet de ramasser les coeurs
        for coeur in coeurs:
            if joueuractuel.rect.x == coeur.rect.x and joueuractuel.rect.y == coeur.rect.y:
                joueuractuel.hp += 50
                if joueuractuel.hp > joueuractuel.hp_max:
                    joueuractuel.hp = joueuractuel.hp_max
                largeur_barre_actuelle = joueuractuel.hp * 2
                rect_barre_actuelle = (700, 100, largeur_barre_actuelle, 20)
                x_coeur, y_coeur = position_random(0, 63, 0, 63)
                coeur.rect.x = x_coeur * 10
                coeur.rect.y = y_coeur * 10
        
        #permet de remettre les mouvements à 0 en fin de tour pour eviter de casser le jeu
        if joueuractuel.mouvement<0:
            joueuractuel.mouvement = 0
        
        
        # echap pour retourner au menu
        elif touches[pygame.K_ESCAPE]: 
            running = False
            pygame.quit()
            subprocess.run(["python", "menu.py"])
          
          #permet de passer son tour et de redonner des mouvements pour le prochain tour
        elif joueuractuel.mouvement == 0:
            joueuractuel.mouvement = 10
            joueuractuel = tour_joueur(joueuractuel)
              
        #permet d'utiliser les bottes
        elif touches[pygame.K_b]:
            joueuractuel.utiliser_botte()
            updatetext.render(joueuractuel)
            
        # definition de la case de sortie et de ses conditions
        elif plateau.get_case_content(joueur_x, joueur_y).biome_name == "temple" and joueuractuel.nombre_peau >= 3 and joueuractuel.nombre_griffes >= 2:
            running = False
            pygame.quit()
            subprocess.run(["python", "victoire.py"])

        #genere des chevres quand elles sont tous mortes
        elif all(chevre.rect.x == -100 for chevre in chevres):
            joueuractuel.nombre_peau += 1
            chevres = generer_chevres(5)  
            updatetext.render(joueuractuel)
            
            #genere des loups quand ils sont tous morts
        elif all(loup.rect.x == -100 for loup in loups):
            joueuractuel.nombre_griffes += 1
            loups = generer_loups(5)  # Générez un nouveau lot de loups
            updatetext.render(joueuractuel)

        
        #mise à jour des barres de vie dans le runner
        healthbar1.update()
        healthbar2.update()
        healthbar3.update()
        healthbar4.update()

        
        
        pygame.display.flip()

    #mort des joueurs
    for loup in loups:
        if loup.hp <= 0:
            loup.mourir()
            joueuractuel.augmenter_nombre_griffes(1)
            texte4 = police.render(f"Griffe : {joueuractuel.nombre_griffes}", True, (255, 255, 255))
            loup.hp = 100
            updatetext.render(joueuractuel)
            healthbar1.update()
            healthbar2.update()
            healthbar3.update()
            healthbar4.update()
    
    #mort des maraudeurs
    for maraudeur in maraudeurs:
        if maraudeur.hp <= 0:
            maraudeur.mourir()
            maraudeur.hp = 100
            updatetext.render(joueuractuel)
            healthbar1.update()
            healthbar2.update()
            healthbar3.update()
            healthbar4.update()

    #mort des chevres
    for chevre in chevres:
        if chevre.hp <= 0:
            chevre.mourir()
            joueuractuel.augmenter_nombre_peau(1)
            texte2 = police.render(f"Peau : {joueuractuel.nombre_peau}", True, (255, 255, 255))
            chevre.hp = 100
            updatetext.render(joueuractuel)
            healthbar1.update()
            healthbar2.update()
            healthbar3.update()
            healthbar4.update()

    #mort des joueurs et reapparition en coin de carte. L'inventaire est aussi vidé
    if joueur1.hp <= 0:
        plateau.placer_joueur(joueur1, x1, y1)
        joueur1.hp = 100
        joueur1.nombre_peau = 0
        joueur1.nombre_griffes = 0
        joueur1.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    if joueur2.hp <= 0:
        plateau.placer_joueur(joueur2, x2, y2)
        joueur2.hp = 100
        joueur2.nombre_peau = 0
        joueur2.nombre_griffes = 0
        joueur2.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    if joueur3.hp <= 0:
        plateau.placer_joueur(joueur3, x3, y3)
        joueur3.hp = 100
        joueur3.nombre_peau = 0
        joueur3.nombre_griffes = 0
        joueur3.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)

    if joueur4.hp <= 0:
        plateau.placer_joueur(joueur4, x4, y4)
        joueur4.hp = 100
        joueur4.nombre_peau = 0
        joueur4.nombre_griffes = 0
        joueur4.inventaire = []
        joueuractuel = tour_joueur(joueuractuel)
            
    


        
        

    fenetre_main.blit
    plateau.joueurs.draw(fenetre_main)
    plateau.afficher_plateau()

    
    

    
    pygame.display.flip()

pygame.quit()
