import socket
import threading

# Paramètres du serveur
adresse = "127.0.0.1"  # Adresse IP du serveur
port = 5555  # Port du serveur
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
    global joueur_actuel
    joueur_actuel = 0

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

            # Gérer le tour à tour des joueurs
            if joueur == joueur_actuel:
                # Envoyer le tour du joueur actuel à ce client
                client_socket.send("C'est votre tour.".encode("utf-8"))
                joueur_actuel = (joueur_actuel + 1) % nombre_joueurs_attendus

        except:
            # En cas d'erreur, supprimer le client de la liste et fermer la connexion
            with mutex:
                clients.remove(client_socket)
                nombre_joueurs_connectes -= 1
                client_socket.close()
            break

# Accepter les connexions jusqu'à ce que le nombre de joueurs requis soit atteint
while nombre_joueurs_connectes < nombre_joueurs_attendus:
    client, adresse_client = serveur.accept()
    with mutex:
        clients.append(client)
        nombre_joueurs_connectes += 1

    print(f"Joueur {nombre_joueurs_connectes} connecté depuis {adresse_client}")

    # Si le nombre de joueurs atteint la limite, envoyer un message à tous les clients
    if nombre_joueurs_connectes == nombre_joueurs_attendus:
        with mutex:
            for c in clients:
                c.send("Le groupe est plein, La Partie se lance !".encode("utf-8"))

    # Créer un thread pour gérer chaque client
    thread_client = threading.Thread(target=gerer_client, args=(client, nombre_joueurs_connectes))
    thread_client.start()

# Fermer le serveur
serveur.close()
