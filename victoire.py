import pygame
import sys

pygame.init()

# Configuration de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Victoire")

couleur = ((87, 80, 66))

# Police de texte
font = pygame.font.Font(None, 36)

# Message de victoire
message = "Le joueur a passé le temple et a gagné!"

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    fenetre.fill(couleur)
    
    # Affiche le message de victoire
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre // 2))
    fenetre.blit(text, text_rect)

    pygame.display.flip()

pygame.quit()
sys.exit()
