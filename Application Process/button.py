import random
import time
import pygame


pygame.init()

class Button(pygame.sprite.Sprite):
    def __init__(self, color_clicked, color_released, sound_clicked,rect_pos_x, rect_pos_y ): # Add given properties as parameters
        super().__init__()
        # Initialize properties here
        self.color_on = color_clicked
        self.sound = sound_clicked
        self.color_off = color_released

        self.image = pygame.Surface((230, 230))
        self.image.fill(self.color_off)

        self.rect = self.image.get_rect()

        # Assign x, y coordinates to the top left of the sprite
        self.rect.topleft = (rect_pos_x, rect_pos_y) # Position of each sprite

        self.x = rect_pos_x
        self.y = rect_pos_y

        self.clicked = False

    def draw(self, screen):
        '''
        Draws button sprite onto pygame window when called
        '''
        # blit image here
        screen.blit(self.image, (self.x, self.y)) # (object to display, pos to display it)
        
    def selected(self, mouse_pos):
        '''
        Used to check if given button is clicked/selected by player
        '''
        if self.rect.collidepoint(mouse_pos):
            self.clicked = True
            return self.clicked
        self.clicked = False

    def update(self, screen):
        '''
        Illuminates button selected and plays corresponding sound.
        Sets button color back to default color after being illuminated.
        '''
        # Illuminate button by filling color here

        self.image.fill(self.color_on)

        # blit the image here so it is visible to the player
        screen.blit(self.image, (self.x, self.y))
        # Play sound
        self.sound.play()
        pygame.display.update() # update the display with illuminated button

        pygame.time.wait(200) # Duration of illumation

        # turn off illuminated button
        self.image.fill(self.color_off)
        screen.blit(self.image, (self.x, self.y))
        pygame.display.update(self.rect)