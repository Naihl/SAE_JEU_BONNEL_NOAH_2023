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
new_font = pygame.font.Font("./img/Dune_Rise.ttf", 50)
background = pygame.image.load("./img/cover_desert1.jpeg")
fenetre_menu.blit(background, (0, 0))
import pygame_gui.elements.ui_button as pygame_gui_button

pygame.display.set_caption("King of Sand")
theme_data = {
    "UILabel": {
        "font_path": "./img/Dune_Rise.ttf",
        "font_size": 50
    }
}
manager = pygame_gui.UIManager((largeur_menu, hauteur_menu),"./img/font.json")

# Création de l'interface du menu


menu_label = pygame_gui.elements.UILabel(
    relative_rect=pygame.Rect((200, 100), (400, 100)),
    text="King of Sand",
    manager=manager
)

bouton_jouer = pygame_gui_button.UIButton(
    relative_rect=pygame.Rect((300, 250), (200, 50)),
    text="Jouer",
    manager=manager
)


bouton_tutoriel = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 350), (200, 50)),
    text="Tutoriel",
    manager=manager
)

bouton_stats = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 400), (200, 50)),
    text="Stats",
    manager=manager
)


bouton_quitter = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 450), (200, 50)),
    text="Quitter",
    manager=manager
)
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
                            
                    with open("./saves_stats/data_global.json", "r+") as f:
                        data = json.load(f)
                        data["nb_partie_jouee"] += 1
                        f.seek(0)
                        json.dump(data, f, indent=4)
                        f.truncate()
                    
                    #lancement du jeu
                    pygame.quit()
                    subprocess.run(["python", "game.py"])
                    #bouton tutoriel qui lance l'affichage tutoriel
                if event.ui_element == bouton_tutoriel:
                    pygame.quit()
                    subprocess.run(["python", "tutoriel.py"])
                    #bouton quitter qui quitte le jeu
                if event.ui_element == bouton_stats:
                    pygame.quit()
                    subprocess.run(["python", "stats_screen.py"])

                if event.ui_element == bouton_quitter:
                    running = False
                


        manager.process_events(event)

    manager.update(1 / 60)
    #fenetre_menu.fill((87, 80, 66))
    manager.draw_ui(fenetre_menu)
    pygame.display.update()

# Quitter Pygame
pygame.quit()
