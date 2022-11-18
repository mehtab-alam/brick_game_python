#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:01:11 2022

@author: syed
"""
import pygame
from settings import Settings
import sys
from plane import Plane
from opponent_plane import OpponentPlane
from pygame import mixer

class BrickGame:
    
    
    def __init__(self):
        pygame.init()
        mixer.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Brick Game")
        mixer.music.load('sounds/explosion.flac')
        
        self.bg = pygame.image.load("images/bg.png")
        
        self.plane = Plane(self)
        self.opponent_plane1 = OpponentPlane(self)
        self.opponent_plane2 = OpponentPlane(self)
        
        
        self.is_game_finished = False
        self.is_started = False
        
        
    def run_game(self):
        while True:
            if not(self.is_game_finished):
                self._check_events()
                self.plane.update()
                self.repeat_opponent_plane()
                self.is_collision()
                self._update_screen()
            else:
                 self.lost_message()
                 mixer.music.play(start=0.2)
                 pygame.time.delay(5 * 1000)
                 break
            
           
    def repeat_opponent_plane(self):
        self.opponent_plane1.update()
        if self.is_started or self.opponent_plane1.rect.y > 250:   
            self.is_started = True
            self.opponent_plane2.update()
    
    
    def lost_message(self):
        green = (0, 255, 0)
        blue = (0, 0, 128)
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('You lost!', True, green, blue)
        textRect = text.get_rect()
 
        # set the center of the rectangular object.
        textRect.center = (self.settings.screen_width // 2, self.settings.screen_height // 2)
        self.screen.blit(text, textRect)
        pygame.display.update()
        
         
    
    def _check_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    
    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.plane.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.plane.moving_left = True
        
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.plane.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.plane.moving_left = False
    
    def draw_borders(self):
        pygame.draw.line(self.screen, self.settings.border_bg_color, (self.settings.border_x1, self.settings.border_y1), (self.settings.border_x1, self.settings.border_y2), 6)    
        pygame.draw.line(self.screen, self.settings.border_bg_color, (self.settings.border_x2, self.settings.border_y1), (self.settings.border_x2, self.settings.border_y2), 6)    
        
        pygame.display.flip()
    
    def is_collision(self):
        collide1 = pygame.Rect.colliderect(self.plane.rect, self.opponent_plane1.rect)
        collide2 = pygame.Rect.colliderect(self.plane.rect, self.opponent_plane2.rect)
        
        if collide1 or collide2: 
            self.is_game_finished = True
            #pygame.quit()
            #sys.exit() 
        
        
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        #self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg, (0, 0))
        self.plane.blitme()
        self.opponent_plane1.blitme()
        self.opponent_plane2.blitme()
        self.draw_borders()
        pygame.display.update()
    
if __name__ == '__main__':
    # Make a game instance, and run the game.
    bgi = BrickGame()
    bgi.run_game()
