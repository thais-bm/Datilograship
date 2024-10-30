class Screen():
    '''
    Class with the basics of a screen, used to show things when created and selected

    Attributes
    ----------
    process : list
        A list of Callables that run game logic
    draw : list
        A list of layers, each one being a list
        of Callables that put entities on screen
    event : list
        A list of Callables that receive game
        input and run code acordingly

    Methods
    -------
    add_entity(entity, layer)
        Adds something that should be rendered while this screen is current
    remove_entity(entity, layer)
        Removes something that should not be rendered while this screen is current
    clear_screen()
        Removes all entities from this screen
    populate()
        Function that should be overwriten to add every entity that should appear while this screen is current
    '''
    def __init__(self):
        self.process = []
        self.draw = [[],[],[]] # the draw function have 2 layers, the thing on the botton have to be in layer 0, the things on top on layer 1
        self.event = []

    def add_entity(self, entity, layer):
        self.process.append(entity.process)
        self.draw[layer].append(entity.draw)
        self.event.append(entity.event)

    def remove_entity(self, entity, layer):
        try:
            self.process.remove(entity.process)
        except:
            print("INFO: Process that is not here tried to be removed")
        try:
            self.draw[layer].remove(entity.draw)
        except:
            print("INFO: Draw that is not here tried to be removed")
        try:
            self.event.remove(entity.event)
        except:
            print("INFO: Event that is not here tried to be removed")


    def clear_screen(self):
        self.process.clear()
        for layer in self.draw:
            layer.clear()
        self.event.clear()

    def populate(self):
        pass
