#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 01:07:21 2022

@author: syed
"""

class Settings:
    
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (255, 255, 255)
        
        self.border_bg_color = (0, 0, 0) # to set the background color if needed
        
        
        self.border_x1 = 125 # x1 point of border line
        self.border_y1 = 0 # y1 point of border line
        
        self.border_x2 = 375 # x2 point of border line
        self.border_y2 = 500 # y2 point of border line
        
        
        self.left_most_position = 170 # It is for the Plane left position
        self.right_most_position = 330 # It is for the Plane right most position
        
        
        self.o_left = 130 # Opponent Plane left position
        self.o_right = 290 # Opponent Plane right position
        
         # Ship settings
        self.plane_speed = 81 # Plane right/left movement Speed
        self.plane_limit = 3
        
        self.opponent_plane_speed = 0.5 # Opponent plane spped moving in vertical direction