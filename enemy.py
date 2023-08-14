import pygame
import random

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 0, 0))  
        self.rect = self.image.get_rect();

    def make_choice(self):
        choices = ["rock", "paper", "scissors"]
        return random.choice(choices)
