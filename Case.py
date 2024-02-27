class Case(object):
    """
    Classe représentant une case dans un jeu avec un biome et des coordonnées.

    Attributes:
        biome_name (str): Le nom du biome de la case.
        x (int): La position horizontale de la case.
        y (int): La position verticale de la case.
    """
    def __init__(self, biome_name, x, y):
        """
        Initialise une nouvelle instance de Case.

        Args:
            biome_name (str): Le nom du biome de la case.
            x (int): La position horizontale de la case.
            y (int): La position verticale de la case.
        """
        self.biome_name = biome_name
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        """
        Retourne une représentation de chaîne de caractères de l'objet Case.

        Returns:
            str: Représentation de l'objet Case sous la forme 'Case(biome_name, x, y)'.
        """
        return f'Case({self.biome_name}, {self.x}, {self.y})'
    
    