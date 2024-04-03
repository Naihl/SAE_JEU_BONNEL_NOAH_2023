import pygame
import pygame_gui
import subprocess
import socket
import threading

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

# Paramètres du serveur
adresse = "127.0.0.1"  # Adresse IP du serveur
port = 5556  # Port du serveur (changé à partir de 5555)
nombre_joueurs_attendus = 4

# Création du socket
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serveur.bind((adresse, port))
serveur.listen()

print(f"Le serveur est en attente de connexions sur {adresse}:{port}")

# Liste des clients connectés
clients = []
nombre_joueurs_connectes = 0
mutex = threading.Lock()

# Fonction pour gérer la connexion avec un client
def gerer_client(client_socket, joueur):
    global nombre_joueurs_connectes

    while True:
        try:
            # Recevoir les données du client
            donnees = client_socket.recv(1024).decode("utf-8")
            if not donnees:
                break

            # Afficher les données reçues
            print(f"Joueur {joueur}: {donnees}")

            # Envoyer les données à tous les autres clients
            with mutex:
                for c in clients:
                    if c != client_socket:
                        c.send(f"Joueur {joueur}: {donnees}".encode("utf-8"))

        except:
            # En cas d'erreur, supprimer le client de la liste et fermer la connexion
            with mutex:
                clients.remove(client_socket)
                nombre_joueurs_connectes -= 1
                client_socket.close()
            break

# Fonction pour gérer l'attente des joueurs
def attendre_joueurs():
    global nombre_joueurs_connectes
    # Accepter les connexions jusqu'à ce que le nombre de joueurs requis soit atteint
    while nombre_joueurs_connectes < nombre_joueurs_attendus:
        client, adresse_client = serveur.accept()
        with mutex:
            clients.append(client)
            nombre_joueurs_connectes += 1

        print(f"Joueur {nombre_joueurs_connectes} connecté depuis {adresse_client}")

# Boucle principale du menu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                # Bouton joueur qui attend la connexion des joueurs
                if event.ui_element == bouton_jouer:
                    attendre_joueurs()
                    pygame.quit()
                    subprocess.run(["python", "game.py"])
                # Bouton tutoriel qui lance l'affichage du tutoriel
                if event.ui_element == bouton_tutoriel:
                    pygame.quit()
                    subprocess.run(["python", "tutoriel.py"])
                # Bouton quitter qui quitte le jeu
                if event.ui_element == bouton_quitter:
                    running = False

        manager.process_events(event)

    manager.update(1 / 60)
    fenetre_menu.fill((87, 80, 66))
    manager.draw_ui(fenetre_menu)
    pygame.display.update()

# Fermer le serveur
serveur.close()
# Quitter Pygame
pygame.quit()
