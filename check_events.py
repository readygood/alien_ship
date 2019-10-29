import pygame
import sys

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()