import pygame

#classe update text permettant de mettre à jour le texte du jeu (inventaire, joueur actuel, mouvement)
class UpdateText:
    def __init__(self, fenetre_main, joueur1, joueur2, joueur3, joueur4):
        self.fenetre_main = fenetre_main
        self.joueurs = [joueur1, joueur2, joueur3, joueur4]
        self.police = pygame.font.Font(None, 36)
        self.police2 = pygame.font.Font(None, 24)

    # Méthode pour mettre à jour le texte
    def render(self, joueuractuel):
        self.fenetre_main.fill((87, 80, 66))

        # Affiche le texte de l'inventaire de chaque joueur
        for i, joueur in enumerate(self.joueurs):
            texte = self.police.render(f"Joueur {i + 1}", True, (255, 255, 255))
            texte1 = self.police.render("Inventaire", True, (255, 255, 255))
            texte2 = self.police2.render(f"Peau : {joueur.nombre_peau}", True, (255, 255, 255))
            texte3 = self.police2.render(f"Botte : {len(joueur.inventaire)}", True, (255, 255, 255))
            texte4 = self.police2.render(f"Griffe : {joueur.nombre_griffes}", True, (255, 255, 255))
            self.fenetre_main.blit(texte, (700, 50 + i * 150))
            self.fenetre_main.blit(texte1, (1000, 50 + i * 150))
            self.fenetre_main.blit(texte2, (1000, 100 + i * 150))
            self.fenetre_main.blit(texte3, (1000, 150 + i * 150))
            self.fenetre_main.blit(texte4, (1000, 125 + i * 150))
        
        # Affiche le texte retour au menu
        bouton_retour = self.police2.render("Retour au menu (Echap)", True, (255, 255, 255))
        bouton_retour_rect = bouton_retour.get_rect(center=(900, 750))
        self.fenetre_main.blit(bouton_retour, bouton_retour_rect)

        # Affiche le texte du joueur actuel
        mouvementtexte = self.police.render(f"Mouvement : {round(joueuractuel.mouvement)}", True, (255, 255, 255))
        self.fenetre_main.blit(mouvementtexte, (100, 710))
        
        joueuractueltexte = self.police.render(f"Joueur actuel : {joueuractuel.nom}", True, (255, 255, 255))
        self.fenetre_main.blit(joueuractueltexte, (100, 670))
        
        
        pygame.display.flip()
