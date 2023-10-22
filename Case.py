#class Case qui permet de créer une case avec un biome, une position x et y
class Case(object):
    def __init__(self, biome_name, x, y):
        self.biome_name = biome_name
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f'Case({self.biome_name}, {self.x}, {self.y})'
    
    