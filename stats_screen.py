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
manager = pygame_gui.UIManager((largeur_menu, hauteur_menu),"./img/font.json")


bouton_retour = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((300, 450), (200, 50)),
    text="retour",
    manager=manager
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == bouton_retour:
                    pygame.quit()
                    subprocess.run(["python", "menu.py"])

        manager.process_events(event)

    manager.update(1 / 60)
    #fenetre_menu.fill((87, 80, 66))
    manager.draw_ui(fenetre_menu)
    pygame.display.update()

