#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 14:55:59 2022

@author: syed
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 23:46:20 2022

@author: syed
"""

import pygame
import random

class OpponentPlane:
    """A class to manage the plane."""
 
    def __init__(self, brick_game):
        """Initialize the plane and set its starting position."""
        self.screen = brick_game.screen
        self.settings = brick_game.settings
        self.screen_rect = brick_game.screen.get_rect()

        # Load the plane image and get its rect.
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        mid_top_shift = (self.settings.left_most_position,self.settings.border_y1)
        #mid_top_shift = (self.settings.right_most_position,self.settings.border_y1)
        # Start each new ship at the bottom center of the screen.
        self.rect.midtop = mid_top_shift
        
        print(float(self.rect.y))
        
        # Store a decimal value for the ship's horizontal position.
        self.y = float(self.rect.y)
        
        

    
    def update(self):
        """Update the plane's position based on movement flags."""
        # Update the opponent's plane x value, not the rect.
        if self.y == 0:
            myRandomPlan = bool(random.getrandbits(1)) # it creates random boolean variable
            if myRandomPlan:
                self.rect.x = self.settings.o_left
            else: 
                self.rect.x = self.settings.o_right
        
        if self.rect.y < self.settings.border_y2:
            self.y += self.settings.opponent_plane_speed
        else:
            self.y = 0 #
        
        
        # Update rect object from self.x.
        self.rect.y = self.y
        
    def blitme(self):
        """Draw the plane at its current location."""
        self.screen.blit(self.image, self.rect)

    