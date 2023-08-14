import pygame
from player import Player
from enemy import Enemy
from game import Game

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Rock Paper Scissors Game")


bg_color = (0, 0, 0)

game = Game()

chosen_enemy = None

player = None
enemy = None
enemy_choice_text = ""

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                chosen_enemy = "Dr Maligno"
            elif event.key == pygame.K_2:
                chosen_enemy = "2plas"
            elif event.key == pygame.K_3:
                chosen_enemy = "Rinoloco"
            elif event.key in [pygame.K_r, pygame.K_p, pygame.K_s]:
                if chosen_enemy:
                    player_choice = "rock" if event.key == pygame.K_r else "paper" if event.key == pygame.K_p else "scissors"
                    enemies = {"Dr Maligno": Enemy("Dr Maligno"), "2plas": Enemy("2plas"), "Rinoloco": Enemy("Rinoloco")}
                    enemy_choice = enemies[chosen_enemy].make_choice()

                    result = game.play(player_choice, enemy_choice)

                    player = Player(player_choice)
                    enemy = enemies[chosen_enemy]
                    enemy_choice_text = f"Enemy chose: {enemy_choice}"

    screen.fill(bg_color)
    if player and enemy:
        screen.blit(player.image, (100, 200))
        screen.blit(enemy.image, (600, 200))

        font = pygame.font.Font(None, 36)
        player_name = font.render("Player", True, (255, 255, 255))
        enemy_name = font.render(enemy.name, True, (255, 255, 255))
        enemy_choice_render = font.render(enemy_choice_text, True, (255, 255, 255))
        screen.blit(player_name, (100, 160))
        screen.blit(enemy_name, (600, 160))
        screen.blit(enemy_choice_render, (200, 450))

        pygame.display.flip()

        pygame.time.delay(1000)

    clock.tick(60)

