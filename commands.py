import random

#A helper file to do pokemon oriented tasks

class pokemon:
    def __init__(self):
        bug, dark, dragon, electric, fight = "bug", "dark", "dragon", "electric", "fight"
        fire, ghost, grass, ground, ice = "fire", "ghost", "grass", "ground", "ice"
        fairy, normal, flying, poison = "fairy", "normal", "flying", "poison"
        psychic, rock, steel, water = "psychic", "rock", "steel", "water"

        self.types_long = {
            "normal": [normal,normal,69],"water": [water, water, 68],"grass": [grass,grass,43],
            "psychic": [psychic, psychic, 39], "fire": [fire,fire,34],"electric": [electric, electric, 32],
            "fight": [fight,fight,29], "normal_flying": [normal, flying, 26], "bug": [bug,bug,19],
            "fairy": [fairy,fairy, 19],"ice": [ice,ice,18], "ground": [ground, ground, 17], 
            "poison": [poison,poison,16],"bug_flying": [bug, flying, 14],"ghost": [ghost,ghost,14], 
            "grass_poison": [grass, poison, 14], "rock": [rock,rock,13],"dragon": [dragon, dragon, 13],
            "dark": [dark,dark,13], "bug_poison": [bug, poison, 12], "rock_water": [rock,water,11],
            "steel": [steel,steel, 11],"rock_ground": [rock,ground,9], "water_ground": [water, ground, 9],
            "psychic_flying": [psychic,flying,9],"steel_psychic": [steel, psychic, 8],"water_flying": [water,flying,8], 
            "psychic_fairy": [psychic, fairy, 8], "steel_rock": [steel,rock,7],"water_ice": [water, ice, 7],
            "grass_flying": [grass,flying,7], "poison_dark": [poison, dark, 7], "ground_ghost": [ground,ghost,6],
            "ground_dragon": [ground, dragon, 6],"bug_rock": [bug,rock,6], "bug_steel": [bug, steel, 6],
            "bug_grass": [bug,grass,6],"ghost_fire": [ghost, fire, 6],"ghost_grass": [ghost, grass, 6],
            "fire_fight": [fire,fight,6],"fire_flying": [fire, flying, 6],"water_poison": [water,poison,6], 
            "water_dark": [water,dark, 6], "dragon_flying": [dragon,flying,6],"dark_flying": [dark, flying, 6],
            "normal_psychic": [normal,psychic,5], "normal_fairy": [normal, fairy, 5], "bug_water": [bug,water,5],
            "steel_ground": [steel, ground, 5],"fire_rock": [fire,rock,5], "water_psychic": [water, psychic, 5], 
            "grass_fight": [grass,fight,5],"grass_dragon": [grass, dragon, 5],"grass_fairy": [grass,fairy,5], 
            "electric_flying": [electric, flying, 5], "ice_psychic": [ice,psychic,5],"dark_normal": [dark, normal, 5],
            "normal_fight": [normal,fight,4], "fight_psychic": [fight, psychic, 4], "poison_fight": [poison,fight,4],
            "rock_flying": [rock, flying, 4],"bug_fire": [bug,fire,4], "bug_electric": [bug, electric, 4], 
            "ghost_dragon": [ghost,dragon,4],"steel_dragon": [steel,dragon,4],"steel_fairy": [steel,fairy,4], 
            "water_fairy": [water, fairy, 4], "grass_psychic": [grass,psychic,4],"grass_dark": [grass, dark, 4],
            "electric_steel": [electric,steel,4], "psychic_ghost": [psychic, ghost, 4], "dark_dragon": [dark,dragon,4],
            "dark_fight": [dark,fight,4],"fight_steel": [fight,steel,3], "flying": [flying, flying, 3], 
            "poison_flying": [poison,flying,3],"poison_dragon": [poison,dragon,3],"ground_flying": [ground,flying,3], 
            "ground_dark": [ground,dark,3], "rock_electric": [rock,electric,3],"rock_ice": [rock,ice,3],
            "bug_fight": [bug,fight,3],"ghost_flying": [ghost,flying,3],"ghost_poison": [ghost, poison, 3],
            "steel_flying": [steel,flying,3], "steel_ghost": [steel, ghost, 3], "fire_ground": [fire,ground,3],
            "water_fight": [water, fight, 3],"water_ghost": [water,ghost,29], "water_grass": [water, grass, 3], 
            "water_electric": [water,electric,3],"water_dragon": [water, dragon, 3],"grass_steel": [grass,steel,3], 
            "electric_grass": [electric, grass, 3], "psychic_fire": [psychic,fire,3],"ice_ground": [ice, ground, 3],
            "dragon_fire": [dragon,fire,3], "dragon_electric": [dragon, electric, 3], "dragon_psychic": [dragon,psychic,3],
            "dark_fire": [dark, fire, 3],"dark_psychic": [dark,psychic,3], "dark_fairy": [dark, fairy, 3],
            "fairy_flying": [fairy,flying,3],"normal_ground": [normal, ground, 2],"normal_ghost": [normal,ghost,2], 
            "normal_grass": [normal, grass, 2], "fight_flying": [fight,flying,2],"poison_ground": [poison, ground, 2],
            "poison_fire": [poison,fire,2], "poison_psychic": [poison, psychic, 2], "ground_psychic": [ground,psychic,2],
            "rock_grass": [rock, grass, 2],"rock_psychic": [rock,psychic,2], "rock_dragon": [rock, dragon, 2], 
            "rock_fairy": [rock,fairy,2],"bug_ground": [bug, ground, 2],"bug_psychic": [bug,psychic,2],
            "bug_fairy": [bug, fairy, 2],"fire_normal": [fire,normal,2],"grass_ice": [grass, ice, 2],
            "electric_normal": [electric,normal,2],"electric_poison": [electric,poison,2],"electric_ice": [electric, ice, 2],
            "electric_fairy": [electric,flying,2],"ice_flying": [ice,flying,2], "ice_bug": [ice,bug,2],
            "ice_steel": [ice,steel,2],"dragon_fight": [dragon,fight,2], "dark_ghost": [dark, ghost, 2], 
            "dark_steel": [dark,steel,2],"dark_ice": [dark,ice,2],"normal_water": [normal,water,1], 
            "normal_dragon": [normal,dragon,1],"fight_ghost": [fight,ghost,1],"fight_ice": [fight,ice,1],
            "poison_fairy": [poison,fairy,1],"ground_electric": [ground,electric,1],"rock_fight": [rock,fight,1],
            "rock_poison": [rock,poison,1],"rock_dark": [rock,dark,1],"rock_ghost": [rock,ghost,1],
            "ghost_fairy": [ghost,fairy,1],"fire_steel": [fire,steel,1],"fire_water": [fire,water,1],
            "grass_ground": [grass,ground,1],"electric_ghost": [electric,ghost,1],"electric_fire": [electric,fire,1],
            "electric_psychic": [electric,psychic,1],"electric_dark": [electric,dark,1],"ice_ghost": [ice,ghost,1], 
            "ice_fire": [ice,fire,1],"ice_fairy": [ice,fairy,1],"dragon_ice": [dragon,ice,1],"dragon_fairy": [dragon,fairy,1]
        }

    def random_type(self):
        types_short = [x for x in self.types_long]
        types_weights = [self.types_long[x][2] for x in self.types_long]
        
        '''
        # Declaring the variables without comprehensions
        types_short = []
        for x in self.types_long:
            types_short.append(x)
        
        types_weights = []
        for x in self.types_long:
            types_weights.append(self.types_long[x][2])
        '''

        return random.choices( types_short, weights=types_weights, k=1 )

if __name__ == "__main__":
  poke = pokemon()
  print(poke.random_type())