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
import socket

# Définition des informations de connexion au serveur
SERVER_HOST = '127.0.0.1'  # Adresse IP du serveur
SERVER_PORT = 5555          # Port utilisé par le serveur

# Initialisation du socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

# Fonction pour envoyer des données au serveur
def send_data(data):
    try:
        client_socket.send(data.encode())
    except Exception as e:
        print(f"Erreur lors de l'envoi de données : {e}")

# Fonction pour envoyer les données de jeu au serveur
def send_game_data():
    # Exemple : envoyer les coordonnées du joueur au serveur
    player_x, player_y = joueuractuel.obtenir_position()
    data = f"PLAYER_POSITION {player_x} {player_y}"
    send_data(data)

# Fonction pour recevoir les données du serveur
def receive_game_data():
    try:
        data = client_socket.recv(1024)
        if data:
            # Traitez les données reçues du serveur ici (mise à jour de l'état du jeu, etc.)
            print(f"Reçu des données du serveur : {data.decode()}")
    except Exception as e:
        print(f"Erreur lors de la réception de données : {e}")
        
#fichier principale du jeu

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

# fonction permettant de voir si le joueur est à coté d'un autre joueur
def joueurs_adjacents(joueur1, joueur2):
    x1, y1 = joueur1.obtenir_position()
    x2, y2 = joueur2.obtenir_position()
    return abs(x1 - x2) + abs(y1 - y2) == 1

# fonction permettant de deplacer les loups vers le joueur
def deplacer_loups_vers_joueur(joueur, loups):
    # Parcoure tous les loups
    for loup in loups:
        # Ignore les loups déjà éliminés
        if loup.hp <= 0:
            continue  
        joueur_x, joueur_y = joueur.obtenir_position()
        loup_x, loup_y = loup.obtenir_position()
        deplacement_x = 0
        deplacement_y = 0

        # Vérifie si le loup est sur une case
        case_loup = plateau.get_case_content(loup_x, loup_y)
        if case_loup is not None:
            if joueur_x < loup_x:
                if plateau.get_case_content(loup_x -1, loup_y).biome_name == "blue":
                    break
                else:
                    deplacement_x = -1
            elif joueur_x > loup_x:
                if plateau.get_case_content(loup_x +1, loup_y).biome_name == "blue":
                    break
                else:
                    deplacement_x = 1

            if joueur_y < loup_y:
                if plateau.get_case_content(loup_x, loup_y -1).biome_name == "blue":
                    break
                else:
                    deplacement_y = -1
            elif joueur_y > loup_y:
                if plateau.get_case_content(loup_x, loup_y +1).biome_name == "blue":
                    break
                else:
                    deplacement_y = 1

        if abs(joueur_x - loup_x) + abs(joueur_y - loup_y) <= 1:
            loup.attaquer(joueur)  # Le loup attaque le joueur s'il est à portée
        else:
            loup.deplacer(deplacement_x, deplacement_y)
            
# fonction permettant de deplacer les maraudeurs vers le joueur
def deplacer_maraudeurs_vers_joueur(joueur, maraudeurs):
    # Parcoure tous les maraudeurs
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
            maraudeur.attaquer(joueur)  # Le loup attaque le joueur s'il est à portée
        else:
            maraudeur.deplacer(deplacement_x, deplacement_y)



# fonction permettant de generer une position aleatoirement
def position_random(a,b,c,d):
    while True:
        x, y = random.randint(a, b), random.randint(c, d)
        #on verifie que la case n'est pas impossible d'acces
        if plateau.get_case_content(x, y).biome_name != "blue":
            break
    return x, y

# fonction permettant de generer les chèvres aleatoirement
def generer_chevres(nombre_de_chevres):
    chevres = []
    for _ in range(nombre_de_chevres):
        x_chevre, y_chevre = position_random(0, 63, 0, 63  )
        chevre = Chevre("chevre", x_chevre, y_chevre, 10, 100, 10, 3, "img/chevre.png")
        plateau.placer_enemies(chevre, x_chevre, y_chevre)
        chevres.append(chevre)
    return chevres

# Crée  10 chèvres 
chevres = generer_chevres(10)

# fonction permettant de generer les loups aleatoirement
def generer_loups(nombre_de_loups):
    loups = []
    for _ in range(nombre_de_loups):
        x_loup, y_loup = position_random(0, 63, 0, 63)
        loup = Loup("loup", x_loup, y_loup, 10, 100, 30, 3, "img/loup.png")
        plateau.placer_enemies(loup, x_loup, y_loup)
        loups.append(loup)
    return loups
    
# Crée 10 loups
loups = generer_loups(10)  

# fonction permettant de generer les maraudeurs aleatoirement
def generer_maraudeurs(nombre_de_maraudeurs):
    maraudeurs = []
    for _ in range(nombre_de_maraudeurs):
        x_maraudeur, y_maraudeur = position_random(28, 36, 28, 36)
        maraudeur = Maraudeur("maraudeur", x_maraudeur, y_maraudeur, 10, 150, 15, 2, "img/maraudeur.png")
        plateau.placer_enemies(maraudeur, x_maraudeur, y_maraudeur)
        maraudeurs.append(maraudeur)
    return maraudeurs

# Crée 3 maraudeurs
maraudeurs = generer_maraudeurs(3)  

# fonction permettant de generer les coeurs aleatoirement
def generer_coeurs(nombre_de_coeurs):
    coeurs = []

    nombre_de_coeurs = 10  
    for _ in range(nombre_de_coeurs):
        x_coeur, y_coeur = position_random(0, 63, 0, 63)
        coeur = Coeur(x_coeur, y_coeur)
        plateau.placer_objet(coeur, x_coeur, y_coeur)
        coeurs.append(coeur)
    return coeurs

# Crée 20 coeurs
coeurs = generer_coeurs(20)  

# fonction permettant de generer les bottes aleatoirement
def generer_bottes(nombre_de_bottes):
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




# Initialisation des joueurs
x1, y1 = position_random(0, 15, 0, 15)
joueur1 = Joueur("Joueur 1", x1, y1, 10, 100, 10, 5)
positionx_originale_joueur1 = x1
positiony_originale_joueur1 = y1
plateau.placer_joueur(joueur1, x1, y1)

x2, y2 = position_random(48, 63, 0, 15)
joueur2 = Joueur("Joueur 2", x2, y2, 10, 100, 10, 5)
positionx_originale_joueur2 = x2
positiony_originale_joueur2 = y2
plateau.placer_joueur(joueur2, x2, y2)

x3, y3 = position_random(0, 15, 48, 63)
joueur3 = Joueur("Joueur 3", x3, y3, 10, 100, 10, 5)
positionx_originale_joueur3 = x3
positiony_originale_joueur3 = y3
plateau.placer_joueur(joueur3, x3, y3)

x4, y4 = position_random(48, 63, 48, 63)
joueur4 = Joueur("Joueur 4", x4, y4, 10, 100, 10, 5)
positionx_originale_joueur4 = x4
positiony_originale_joueur4 = y4
plateau.placer_joueur(joueur4, x4, y4)







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

# fonction permettant de changer les tours des joueurs
def tour_joueur(joueuractuel):
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
