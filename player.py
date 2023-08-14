import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, choice):
        super().__init__()
        self.choice = choice  
        self.image = pygame.Surface((100, 100))
        self.image.fill((255, 255, 255))  
        self.rect = self.image.get_rect()
