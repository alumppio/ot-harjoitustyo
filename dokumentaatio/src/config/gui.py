import pygame
from config.dice import Dices


# Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (180, 180, 180)
RED = (200, 0, 0)
FPS = 60
TIMER = pygame.time.Clock()
DICE_A = 60  # Dice width
DICE_X = 200  # Dice x-coordinate
DICE_Y = 10  # Dice y-coordinate
DICE_GAP = 10

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
SCREEN.fill(WHITE)
pygame.display.set_caption("Yatzy")
DICE_ROLLER = pygame.transform.smoothscale(pygame.image.load
("/home/alumppio/ot-harjoitustyo/dokumentaatio/src/resources/istockphoto-936431366-1024x1024.jpg"),
                                           (150, 80))
ROLL_TEXT = pygame.transform.smoothscale(
    pygame.image.load
    ("/home/alumppio/ot-harjoitustyo/dokumentaatio/src/resources/roll_text_picture.png"),
    (150, 20))


class DrawDice:
    """Class to draw dices to the plane"""

    def __init__(self, dices: Dices):
        self.dices = dices

    def dice_side_1(self, dice_number):
        """Defining dice side 1"""
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                                                    DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/2 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)

    def dice_side_2(self, dice_number):
        """Defining dice side 2"""
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                                                    DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)

    def dice_side_3(self, dice_number):
        """Defining dice side 3"""
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                                                    DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/2
                                           + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)

    def dice_side_4(self, dice_number):
        """Defining dice side 4"""
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number +
                                                    DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number + 3*DICE_A/4
                                           + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)

    def dice_side_5(self, dice_number):
        """Defining dice side 5"""
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(DICE_X + DICE_GAP*dice_number
            + DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/2 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           3*DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           3*DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)

    def dice_side_6(self, dice_number):
        """Defining dice side 6"""
        pygame.draw.rect(SCREEN, BLACK, pygame.Rect(DICE_X +
                            DICE_GAP*dice_number + DICE_A*dice_number, DICE_Y, DICE_A, DICE_A), 2)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           3*DICE_A/4 + dice_number*DICE_A, DICE_Y + 3*DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           3*DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/2), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)
        pygame.draw.circle(SCREEN, BLACK, (DICE_X + DICE_GAP*dice_number +
                                           3*DICE_A/4 + dice_number*DICE_A, DICE_Y + DICE_A/4), 5)

    def draw_dices(self):
        """Draw dices according to earlier methods"""
        for i in range(5):
            if self.dices.dice[i] == 1:
                self.dice_side_1(i)

            elif self.dices.dice[i] == 2:
                self.dice_side_2(i)

            elif self.dices.dice[i] == 3:
                self.dice_side_3(i)

            elif self.dices.dice[i] == 4:
                self.dice_side_4(i)

            elif self.dices.dice[i] == 5:
                self.dice_side_5(i)

            elif self.dices.dice[i] == 6:
                self.dice_side_6(i)

    def draw_dice_roller(self):
        """Draw an object that can roll the dice with a click """
        SCREEN.blit(DICE_ROLLER, (550, 5))
        SCREEN.blit(ROLL_TEXT, (550, 90))
        pygame.draw.rect(SCREEN, GRAY, pygame.Rect(548, 3, 154, 110), 2)

    def draw_all(self):
        """Draw all objects"""
        self.draw_dice_roller()
        self.draw_dices()


class EventHandler:
    """Class to handle events in the game """

    def __init__(self, dices: Dices):
        self.dices = dices
        self.dices_to_hold = []
        self.dice_drawer = DrawDice(self.dices)
        self.running = True

    def select_dice(self, dice_number):
        """Method to select the dice"""
        pygame.draw.rect(SCREEN, RED, pygame.Rect(DICE_X + DICE_GAP*(dice_number-1)
                         + DICE_A*(dice_number-1)-4, DICE_Y-4, DICE_A+8, DICE_A+8), 2)
        self.dices_to_hold.append(dice_number-1)

    def unselect_dice(self):
        """Method to unselect the dice"""
        for dice_number in range(5):
            pygame.draw.rect(SCREEN, WHITE, pygame.Rect(DICE_X +
                                                        DICE_GAP *
                                                        (dice_number) + DICE_A *
                                                        (dice_number) -
                                                        4, DICE_Y-4,
                                                        DICE_A+8, DICE_A+8), 2)
        self.dices_to_hold = []

    def hold_dice(self, event):
        """Check if dices were selected"""
        if event.type == pygame.MOUSEBUTTONDOWN and DICE_Y <= event.pos[1] <= DICE_Y+DICE_A:
            if DICE_X <= event.pos[0] <= DICE_X+DICE_A:
                self.select_dice(1)
            elif DICE_X + DICE_GAP + DICE_A <= event.pos[0] <= DICE_X + DICE_GAP + DICE_A*2:
                self.select_dice(2)
            elif DICE_X + DICE_GAP*2 + DICE_A*2 <= event.pos[0] <= DICE_X + DICE_GAP*2 + DICE_A*3:
                self.select_dice(3)
            elif DICE_X + DICE_GAP*3 + DICE_A*3 <= event.pos[0] <= DICE_X + DICE_GAP*3 + DICE_A*4:
                self.select_dice(4)
            elif DICE_X + DICE_GAP*4 + DICE_A*4 <= event.pos[0] <= DICE_X + DICE_GAP*4 + DICE_A*5:
                self.select_dice(5)

    def undo_hold_dice(self, event):
        """Check if user changed his/her mind"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.unselect_dice()

    def roll_dice(self, event):
        """Check if the dice roller was clicked"""
        if event.type == pygame.MOUSEBUTTONDOWN and 3 <= event.pos[1] <= 113:
            if 548 <= event.pos[0] <= 702:
                self.dices.roll_dice(self.dices_to_hold)
                SCREEN.fill(WHITE)

                self.dice_drawer.draw_all()

    def quit(self, event):
        """Method to quit the game"""
        if event.type == pygame.QUIT:
            self.running = False

    def handle_events(self):
        """Check all occurred events"""
        for event in pygame.event.get():
            self.dice_drawer.draw_all()
            self.hold_dice(event)
            self.undo_hold_dice(event)
            self.roll_dice(event)
            self.quit(event)


d = Dices()
e = EventHandler(d)

pygame.display.flip()

while e.running:
    TIMER.tick(FPS)

    e.handle_events()
    pygame.display.flip()
