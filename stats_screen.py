import pygame
import pygame_gui
import json
import subprocess
import tkinter as tk
from tkinter import filedialog

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BUTTON_WIDTH = 400
BUTTON_HEIGHT = 50
TEXT_BOX_WIDTH = 200
TEXT_BOX_HEIGHT = 40

# initialisation de la fenetre pygame
window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
background = pygame.image.load("./img/cover_desert1.jpeg")
window_surface.blit(background, (0, 0))
manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

#création des boutons et des textboxes
load_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((WINDOW_WIDTH // 2 - BUTTON_WIDTH // 2, 525),
        (BUTTON_WIDTH, BUTTON_HEIGHT)), 
        text="charger les statistique d'une partie", 
        manager=manager)
bouton_retour = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((25, 525), (150, 50)),
        text="retour",
        manager=manager
)


global_data_boxes = [pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((200+ i*200, 25  ), (
        TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)),
        html_text='', 
        manager=manager)for i in range(2)]
text_boxes = [pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((200, 100 + i * TEXT_BOX_HEIGHT), 
        (TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)), 
        html_text='', 
        manager=manager) for i in range(10)]
data_boxes = [pygame_gui.elements.UITextBox(relative_rect=pygame.Rect((400, 100 + i * TEXT_BOX_HEIGHT), 
        (TEXT_BOX_WIDTH, TEXT_BOX_HEIGHT)), 
        html_text='', 
        manager=manager) for i in range(10)]


clock = pygame.time.Clock()

# boucle principale
running = True
while running:
    time_delta = clock.tick(60)/1000.0  # time_delta est requis, sinon le programme plante

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        with open('./saves_stats/data_global.json', 'r') as f:
                data_global = json.load(f)
                game_number = data_global['nb_partie_jouee']
                for i, key in enumerate(data_global):
                        global_data_boxes[i].html_text = f'{key}: {data_global[key]}'
                        global_data_boxes[i].rebuild()
        with open(f'./saves_stats/partie_numero_{game_number}.json', 'r') as f:
                        data = json.load(f)
                        # convertie chaque champ de données en str et l'affiche dans une zone de texte séparée
                        for i , key in enumerate(data):
                            text_boxes[i].html_text = f'{key}: '
                            text_boxes[i].rebuild()
                            data_boxes[i].html_text = f'{data[key]}'
                            data_boxes[i].rebuild()
                            if i == 3:
                                break #separation entre les stats des joueurs et les stats generales de cette partie
                        text_boxes[4].html_text = 'stats des joueurs:'
                        data_boxes[4].html_text = 'J1, J2, J3, J4'
                        text_boxes[4].rebuild()
                        data_boxes[4].rebuild()
                        for i , key in enumerate(data):
                            if i > 3:
                                text_boxes[i+1].html_text = f'{key}: '
                                text_boxes[i+1].rebuild()
                                data_boxes[i+1].html_text = f'{data[key]}'
                                data_boxes[i+1].rebuild()
                            
                                
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == load_button:
                    # ouvre une fenetre de selection de fichier
                    root = tk.Tk()
                    root.withdraw()  # cache la fenetre principale
                    file_path = filedialog.askopenfilename(filetypes=[('JSON files', '*.json')],initialdir='./saves_stats')
                    if not file_path: # permet de ne pas planter si on annule la selection du fichier
                        continue

                    #  ouvre le fichier selectionné et affiche les données
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                        # convertie chaque champ de données en str et l'affiche dans une zone de texte séparée
                        for i , key in enumerate(data):
                            text_boxes[i].html_text = f'{key}: '
                            text_boxes[i].rebuild()
                            data_boxes[i].html_text = f'{data[key]}'
                            data_boxes[i].rebuild()
                            if i == 3:
                                break
                        text_boxes[4].html_text = 'stats des joueurs:'
                        data_boxes[4].html_text = 'J1, J2, J3, J4'
                        text_boxes[4].rebuild()
                        data_boxes[4].rebuild()
                        for i , key in enumerate(data):
                            if i > 3:
                                text_boxes[i+1].html_text = f'{key}: '
                                text_boxes[i+1].rebuild()
                                data_boxes[i+1].html_text = f'{data[key]}'
                                data_boxes[i+1].rebuild()

                if event.ui_element == bouton_retour:
                    pygame.quit()
                    subprocess.run(["python", "menu.py"])
        manager.process_events(event)

    manager.update(time_delta)  
    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

pygame.quit()