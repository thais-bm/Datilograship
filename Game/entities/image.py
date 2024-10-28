import pygame

from entities.entity_base import Entity

class Image(Entity):
    '''
    Shows a Image on screen

    Attributes
    ----------
    path:
        The path to load the image from
    center:
        The center position of the textbox
    witdh:
        The width to draw the image, if none is given it will use the original image size
    height:
        The width to draw the image, if none is given it will use the original image size
    '''
    def __init__(self, path, center, width = None, height = None, layer = 2):
        super().__init__(center, layer)
        self.path = path

        # Loading the image
        self.image = pygame.image.load(path)

        # If the width or height was not given the original value is used
        if width == None:
            width = self.image.get_width()
        if height == None:
            height = self.image.get_height()

        self.position = (center[0] - width/2, center[1] - height/2)

        # Scaling the image to the right size
        self.image = pygame.transform.scale(self.image, (width, height))

    def draw(self, screen):
        screen.blit(self.image, self.position)

