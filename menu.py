import pygame
import pygame_gui
import subprocess
import json
from stats import *
pygame.init()

# Configuration de la fenêtre du menu
largeur_menu = 800
hauteur_menu = 600
fenetre_menu = pygame.display.set_mode((largeur_menu, hauteur_menu))
pygame.display.set_caption("King of Sand")

manager = pygame_gui.UIManager((largeur_menu, hauteur_menu))

# Création de l'interface du menu
menu_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((200, 100), (400, 100)),
    text="King of Sand",
    manager=manager
)

bouton_jouer = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 250), (200, 50)),
    text="Jouer",
    manager=manager
)


bouton_tutoriel = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 350), (200, 50)),
    text="Tutoriel",
    manager=manager
)


bouton_quitter = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 450), (200, 50)),
    text="Quitter",
    manager=manager
)



# initialisation du temps de debut de partie
now = time_checker()
#ecriture dans le json
with open("data_partie.json", "r") as f:
    data = json.load(f)
with open("data_partie.json", "w") as f:
    data["temps_deb"] = str(now)
    json.dump(data, f, indent=4)
    

# Boucle principale du menu    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                #bouton joueur qui lance le jeu
                if event.ui_element == bouton_jouer:
                    # initialisation du temps de debut de partie
                    now = time_checker()
                    #ecriture dans le json
                    with open("data_partie.json", "r") as f:
                        data = json.load(f)
                        with open("data_partie.json", "w") as f:
                            data["temps_deb"] = str(now)
                            json.dump(data, f, indent=4)
                            
                    with open("data_global.json", "r") as f:
                        data = json.load(f)
                        with open("data_global.json", "w") as f:
                            data["nb_partie_jouee"] =+ 1
                            json.dump(data, f, indent=4)
                    
                    #lancement du jeu
                    pygame.quit()
                    subprocess.run(["python", "game.py"])
                    #bouton tutoriel qui lance l'affichage tutoriel
                if event.ui_element == bouton_tutoriel:
                    pygame.quit()
                    subprocess.run(["python", "tutoriel.py"])
                    #bouton quitter qui quitte le jeu
                if event.ui_element == bouton_quitter:
                    running = False
                


        manager.process_events(event)

    manager.update(1 / 60)
    fenetre_menu.fill((87, 80, 66))
    manager.draw_ui(fenetre_menu)
    pygame.display.update()

# Quitter Pygame
pygame.quit()
