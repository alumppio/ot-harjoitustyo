import os
import pygame

pygame.init()
# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (200, 0, 0)
LIGHT_RED = pygame.Color('#f4cccc')
LIGHT_BLUE = pygame.Color('#c9daf8')
FPS = 60
TIMER = pygame.time.Clock()
DICE_A = 60  # Dice width
DICE_X = 200  # Dice x-coordinate
DICE_Y = 10  # Dice y-coordinate
DICE_GAP = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
FONT = pygame.font.SysFont('arial', 12)
START_FONT = pygame.font.SysFont('arial', 30)
END_FONT = pygame.font.SysFont('arial', 28)
TIP_FONT = pygame.font.SysFont('arial', 17)

START_TIP_AMOUNT = TIP_FONT.render(
    '(Type with keyboard how many players will play from 1 to 6)', True, GRAY, WHITE)
START_TIP_NAMES = TIP_FONT.render(
    '(Type your name using the keyboard)', True, GRAY, WHITE)
START_TEXT_PLAYERS = START_FONT.render(
    'How many players (Max 6):', True, BLACK, WHITE)
START_TEXT_NAME = START_FONT.render(
    'Choose your name (Max 8 char.):', True, BLACK, WHITE)
END_TEXT = START_FONT.render(
    'High Scores (Top 5 points):', True, RED, WHITE)
END_TIP = TIP_FONT.render(
    'The game will close shortly. Displaying top 5 scores (if there is that many)', True, GRAY, WHITE
)

DIRNAME = os.path.dirname(__file__)
DATA_FILE_PATH1 = os.path.join(
    DIRNAME, "../resources/istockphoto-936431366-1024x1024.jpg")
DATA_FILE_PATH2 = os.path.join(DIRNAME, "../resources/roll_text_picture.png")
DATA_FILE_PATH3 = os.path.join(DIRNAME, "../resources/yatzy_paper2.png")

DICE_ROLLER = pygame.transform.smoothscale(
    pygame.image.load(DATA_FILE_PATH1), (150, 80))
ROLL_TEXT = pygame.transform.smoothscale(
    pygame.image.load(DATA_FILE_PATH2), (150, 20))
YATZY_PAPER = pygame.transform.smoothscale(
    pygame.image.load(DATA_FILE_PATH3), (580, 500))
