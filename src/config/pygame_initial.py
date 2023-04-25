import pygame
from repositories.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE


class Start:
    def __init__(self):
        pygame.init()

        global SCREEN
        global font
        SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        SCREEN.fill(WHITE)
        pygame.display.set_caption("Yatzy")
        font = pygame.font.SysFont('arial', 12)


Start()
