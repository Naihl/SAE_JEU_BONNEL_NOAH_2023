from datetime import datetime
import json

class stats_game:
    

    def __init__(self):
        self.temps_deb = time_checker() 
        self.temps_fin = "partie non completee" 
        self.gagnant = "partie non completee"
        self.nb_tours = 0
        self.nb_deplacement = [0,0,0,0]
        self.degat_subit = [0,0,0,0] 
        self.degat_inflige = [0,0,0,0] 
        self.nb_kills = [0,0,0,0] #ne prend en compte que le pvp
        self.nb_morts = [0,0,0,0]
        

    #getters
    def get_temps_deb(self):
        return self.temps_deb
    
    def get_temps_fin(self):
        return self.temps_fin
     
    def get_nb_deplacement(self):
        return self.nb_deplacement
    
    def get_degat_subit(self):
        return self.degat_subit
    
    def get_degat_inflige(self):
        return self.degat_inflige
    
    def get_gagnant(self):
        return self.gagnant
    
    def set_temps_fin(self):
        self.temps_fin = time_checker()


    #setters
    def set_degat_subit(self, degat_subit:int, joueur:int):
        self.degat_subit[joueur] = degat_subit
    
    def set_degat_inflige(self, degat_inflige:int, joueur:int):
        self.degat_inflige[joueur] = degat_inflige

    def set_gagnant(self, gagnant:str):
        self.gagnant = gagnant


    #methodes
    def add_nb_deplacement(self, deplacement:int, joueuractuel:str):
        last_char = joueuractuel[-1]
        joueur_id = int(last_char)-1
        self.nb_deplacement[joueur_id] += deplacement

    
    def add_degat_subit(self, degat:int, joueuractuel:str):
        last_char = joueuractuel[-1]
        joueur_id = int(last_char)-1
        self.degat_subit[joueur_id] += degat

    
    def add_degat_inflige(self, degat:int, joueuractuel:str):
        last_char = joueuractuel[-1]
        joueur_id = int(last_char)-1
        self.degat_inflige[joueur_id] += degat


    def add_nb_kills(self, joueuractuel:str):
        last_char = joueuractuel[-1]
        joueur_id = int(last_char)-1
        self.nb_kills[joueur_id] += 1


    def add_nb_morts(self, joueuractuel:str):
        last_char = joueuractuel[-1]
        joueur_id = int(last_char)-1
        self.nb_morts[joueur_id] += 1

    
    def add_nb_tours(self):
        self.nb_tours += 1

    def to_json(self):
            # Open the global data file and get the game number
            with open('./saves_stats/data_global.json', 'r') as f:
                data_global = json.load(f)
                game_number = data_global['nb_partie_jouee']

            # Prepare the game data
            data = {
                'temps_deb': self.temps_deb,
                'temps_fin': self.temps_fin,
                'gagnant': self.gagnant,
                'nb_tours': self.nb_tours,
                'nb_deplacement': self.nb_deplacement,
                'degat_subit': self.degat_subit,
                'degat_inflige': self.degat_inflige,
                'nb_kills': self.nb_kills,
                'nb_morts': self.nb_morts
                
            }

            # Write the game data to a new file
            with open(f'./saves_stats/partie_numero_{game_number}.json', 'w') as f:
                json.dump(data, f, indent=4)

    
    

def time_checker():
    
    now = datetime.now()
    now = now.strftime("%H:%M:%S")
    return now

def time_diff(start, end):
    diff = end - start
    return diff





