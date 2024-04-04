import pygame
import sys
import subprocess

pygame.init()

# Configuration de la fenêtre
largeur_fenetre = 800
hauteur_fenetre = 600
fenetre = pygame.display.set_mode((largeur_fenetre, hauteur_fenetre))
pygame.display.set_caption("Victoire")

couleur = ((87, 80, 66))


font = pygame.font.Font(None, 36)
font1 = pygame.font.Font(None, 24)


page = 1

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif page == 1 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            page += 1
        elif page == 2 and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            page = 1            
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            pygame.quit()
            subprocess.run(["python", "menu.py"])
        
    fenetre.fill(couleur)
    
    # affichage premiere page tutoriel
    if page == 1:
        
        #affichage du premier paragraphe
        message = "King of Sand"
        message2 = "King of Sand est un jeu de plateau se jouant à 4 joueurs. Les joueurs s'affrontent sur une carte "
        message3= "avec comme objectif de recuperer des objets et de les amener à la sortie. Pour se faire ils doivent"
        message4= "eliminer des ennemis pour recuperer les objets. Recuperer 3 peaux sur les chevres et 2 griffes de loups"
        message5= "pour pouvoir passer la sortie. Mais attention à vos adversaires ou aux gardes du temple qui tenteront"
        message6= "de vous eliminer. Bonne chance !"
        
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(center=(largeur_fenetre // 2, 20))
        fenetre.blit(text, text_rect)
        
        text2 = font1.render(message2, True, (0, 0, 0))
        text_rect2 = text2.get_rect(center=(largeur_fenetre // 2, 50))
        fenetre.blit(text2, text_rect2)

        text3 = font1.render(message3, True, (0, 0, 0))
        text_rect3 = text3.get_rect(center=(largeur_fenetre // 2, 70))
        fenetre.blit(text3, text_rect3)
        
        text4 = font1.render(message4, True, (0, 0, 0))
        text_rect4 = text4.get_rect(center=(largeur_fenetre // 2, 90))
        fenetre.blit(text4, text_rect4)
        
        text5= font1.render(message5, True, (0, 0, 0))
        text_rect5 = text5.get_rect(center=(largeur_fenetre // 2, 110))
        fenetre.blit(text5, text_rect5)
        
        text6 = font1.render(message6, True, (0, 0, 0))
        text_rect6 = text6.get_rect(center=(largeur_fenetre // 2, 130))
        fenetre.blit(text6, text_rect6)

        #affichage explication temple
        image = pygame.image.load("img/temple.jpg")
        image = pygame.transform.scale(image, (50, 50))
        rect = image.get_rect(center=(50,200))
        fenetre.blit(image, rect)
        
        messagetemple = "Temple: Sortie, avoir 2 griffes de loup et 3 peaux de chevre pour gagner la partie"
        texttemple = font1.render(messagetemple, True, (0, 0, 0))
        fenetre.blit(texttemple, (100, 200))

        #affichage explication chevre
        image2 = pygame.image.load("img/chevre.png")
        image2 = pygame.transform.scale(image2, (50, 50))
        rect2 = image2.get_rect(center=(50,250))
        fenetre.blit(image2, rect2)
        
        messagechevre = "Chevre: Enemie, innofensive, peut etre tue pour recuperer des peaux"
        textchevre = font1.render(messagechevre, True, (0, 0, 0))
        fenetre.blit(textchevre, (100, 250))
        
        #affichage explication loup
        image3 = pygame.image.load("img/loup.png")
        image3 = pygame.transform.scale(image3, (50, 50))
        rect3 = image3.get_rect(center=(50,300))
        fenetre.blit(image3, rect3)
        
        messageloup = "Loup: Enemie, peut etre tue pour recuperer des griffes"
        textloup = font1.render(messageloup, True, (0, 0, 0))
        fenetre.blit(textloup, (100, 300))

        #affichage explication maraudeur
        
        image4 = pygame.image.load("img/maraudeur.png")
        image4 = pygame.transform.scale(image4, (50, 50))
        rect4 = image4.get_rect(center=(50,350))
        fenetre.blit(image4, rect4)
        
        messagegarde = "Maraudeur: Enemie, defend le temple et tente d'eliminer les joueurs qui s'en approchent"
        textgarde = font1.render(messagegarde, True, (0, 0, 0))
        fenetre.blit(textgarde, (100, 350))

        #affichage explication botte
       
        image5 = pygame.image.load("img/botte.png")
        image5 = pygame.transform.scale(image5, (50, 50))
        rect5 = image5.get_rect(center=(50,400))
        fenetre.blit(image5, rect5)
        
        messagebottes = "Bottes: Objet, octroie + 10 points de deplacement à l'activation"
        textbottes = font1.render(messagebottes, True, (0, 0, 0))
        fenetre.blit(textbottes, (100, 400))

        #affichage explication coeur
        
        image6 = pygame.image.load("img/coeur.png")
        image6 = pygame.transform.scale(image6, (50, 50))
        rect6 = image6.get_rect(center=(50,450))
        fenetre.blit(image6, rect6)
        
        messagecoeur = "Coeur: Objet, octroie + 50 point de vie au ramassage"
        textcoeur = font1.render(messagecoeur, True, (0, 0, 0))
        fenetre.blit(textcoeur, (100, 450))
    
    #affichage deuxieme page tutoriel      
    elif page == 2:
        #affichage explication eau

        image7 = pygame.image.load("img/blue.jpg")
        image7 = pygame.transform.scale(image7, (50, 50))
        rect7 = image7.get_rect(center=(50,50))
        fenetre.blit(image7, rect7)
        
        messageblue = "Eau: Case, bloque le chemin"
        textblue = font1.render(messageblue, True, (0, 0, 0))
        fenetre.blit(textblue, (100, 50))

        #affichage explication sable mouvant
        
        image8 = pygame.image.load("img/slow.jpg")
        image8 = pygame.transform.scale(image8, (50, 50))
        rect8 = image8.get_rect(center=(50,100))
        fenetre.blit(image8, rect8)
        
        messageslow = "Sable mouvant: Case, ralentit les joueurs"
        textslow = font1.render(messageslow, True, (0, 0, 0))
        fenetre.blit(textslow, (100, 100))

        #affichage explication sable chaud
       
        image9 = pygame.image.load("img/sand.jpg")
        image9 = pygame.transform.scale(image9, (50, 50))
        rect9 = image9.get_rect(center=(50,150))
        fenetre.blit(image9, rect9)
        
        messagedirt = "Sable Chaud: Case, brule le joueur, lui infligeant des degats"
        textdirt = font1.render(messagedirt, True, (0, 0, 0))
        fenetre.blit(textdirt, (100, 150))

        #affichage explication controles
        
        messagecontrole = "Controle du jeu"
        textcontrole = font.render(messagecontrole, True, (0, 0, 0))
        rectcontrole = textcontrole.get_rect(center=(400,250))
        fenetre.blit(textcontrole, rectcontrole)
        
        image10 = pygame.image.load("img/fleche_clavier.png")
        image10 = pygame.transform.scale(image10, (50, 50))
        rect10 = image10.get_rect(center=(50,300))
        fenetre.blit(image10, rect10)
        
        messagefleche = "Fleches: Deplacement du joueur avec les fleches du clavier"
        textfleche = font1.render(messagefleche, True, (0, 0, 0))
        fenetre.blit(textfleche, (100, 300))
        
        image11 = pygame.image.load("img/espace.png")
        image11 = pygame.transform.scale(image11, (50, 50))
        rect11 = image11.get_rect(center=(50,350))
        fenetre.blit(image11, rect11)
        
        messageespace = "Espace: Attaque du joueur avec la touche espace du clavier"
        textespace = font1.render(messageespace, True, (0, 0, 0))
        fenetre.blit(textespace, (100, 350))
        
        image12 = pygame.image.load("img/b.png")
        image12 = pygame.transform.scale(image12, (50, 50))
        rect12 = image12.get_rect(center=(50,400))
        fenetre.blit(image12, rect12)
        
        messageechap = "B: Activer les bottes si le joueur en possede lors du tour"
        textechap = font1.render(messageechap, True, (0, 0, 0))
        fenetre.blit(textechap, (100, 400))
        
        messageh = "H: Activer un boost de vie une fois par partie"
        texteh = font1.render(messageh, True, (0, 0, 0))
        fenetre.blit(texteh, (100, 450))
        
        
        

    # Afficher le bouton "Page suivante"

    font2 = pygame.font.Font(None, 24)
    bouton = font2.render("Page suivante (Espace)", True, (255, 255, 255))
    bouton_rect = bouton.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre - 20))
    fenetre.blit(bouton, bouton_rect)
    
    # Afficher le bouton "Retour au menu"
    bouton_retour = font2.render("Retour au menu (Echap)", True, (255, 255, 255))
    bouton_retour_rect = bouton_retour.get_rect(center=(largeur_fenetre // 2, hauteur_fenetre - 50))
    fenetre.blit(bouton_retour, bouton_retour_rect)

    pygame.display.flip()
        


pygame.quit()
sys.exit()
