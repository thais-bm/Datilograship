import managers.game_manager as mng

class Entity():
    '''
    Class with the basics of an entity that can be put in a screen

    Attributes
    ----------
    layer: int
        In whith render layer it will render, under (0), middle (1) or upper layer (2) 
    
    Methods
    -------
    process():
        Runs the entity's logic
    draw(screen):
        Draw the entity on screen, in the entity's layer
    event(event):
        React to a event
    destroy():
        Remove the entity of the screen
    '''
    def __init__(self, layer):
        self.layer = layer
        mng.Game_Manager.current_screen.add_entity(self, layer)

    def event(self, event):
        pass
    
    def destroy(self):
        mng.Game_Manager.current_screen.remove_entity(self, self.layer)

    def process(self):
        pass
    
    def draw(self, screen):
        pass
