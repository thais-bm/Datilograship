from entities.entity_base import Entity
from entities.letter import Letter

class Letter_Generator(Entity):
    def __init__(self, layer = 0):
        super().__init__(layer)
        Letter("A", (0,0))
        
    def process(self):
        #Thats where the logic for the letter being spawned will go
        #Let this code and the letter one with me :D
        #I think i know how to do it already - Milton
        pass
