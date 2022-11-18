#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 23:46:20 2022

@author: syed
"""

import pygame
 
class Plane:
    """A class to manage the plane."""
 
    def __init__(self, brick_game):
        """Initialize the plane and set its starting position."""
        self.screen = brick_game.screen
        self.settings = brick_game.settings
        self.screen_rect = brick_game.screen.get_rect()

        # Load the plane image and get its rect.
        self.image = pygame.image.load('images/plane.png')
        self.rect = self.image.get_rect()
        
        print(self.screen_rect.midbottom)
        mid_bottom_shift = (self.settings.left_most_position,self.settings.border_y2)
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = mid_bottom_shift
        
        print(float(self.rect.x))
        
        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the plane's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.settings.right_most_position:
            self.x += self.settings.plane_speed
        if self.moving_left and self.rect.left > self.settings.left_most_position:
            self.x -= self.settings.plane_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the plane at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_plane(self):
        """Center the plane on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)