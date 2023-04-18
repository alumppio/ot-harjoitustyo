import pygame
from config.dice import Dices
from config.player import Player


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

YATZY_PAPER = pygame.transform.smoothscale(
    pygame.image.load
    ("/home/alumppio/ot-harjoitustyo/dokumentaatio/src/resources/yatzy_paper.png"),
    (580,500)
)
font = pygame.font.SysFont('arial', 12)


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


class DrawYatzy:
    def __init__(self):
        SCREEN.blit(YATZY_PAPER, (5,90))
        tip_1 = font.render('MOUSE1 TO ROLL OR SELECT DICE', True, GRAY, WHITE)
        tip_2 = font.render('MOUSE1 TO SET SCORES', True, GRAY, WHITE)
        tip_3 = font.render('UNDO SELECTION WITH ESCAPE', True, GRAY, WHITE)
        tips = [tip_1, tip_2, tip_3]

        for i in range(3):
            SCREEN.blit(tips[i], pygame.Rect(590,150+30*i,20,30))

    def set_upper_part(self, number, dice, player):
        if player.minutes[number] is None:    
            player.set_upper_part(dice,number)
            points = font.render(str(player.minutes[number]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,170+(number-1)*25,100,25))

    def set_pair(self, dice, player):
        if player.minutes["Pair"] is None:
            player.set_pair(dice)
            points = font.render(str(player.minutes["Pair"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,345,100,25))

    def set_two_pair(self, dice, player):
        if player.minutes["Two Pair"] is None:    
            player.set_two_pair(dice)
            points = font.render(str(player.minutes["Two Pair"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,369,100,25))
        
    def set_3_of_a_kind(self, dice, player):
        if player.minutes["Three of a Kind"] is None:
            player.set_3_of_a_kind(dice)
            points = font.render(str(player.minutes["Three of a Kind"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,393,100,25))

    def set_4_of_a_kind(self, dice, player):
        if player.minutes["Four of a Kind"] is None:
            player.set_4_of_a_kind(dice)
            points = font.render(str(player.minutes["Four of a Kind"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,417,100,25))

    def set_small_straight(self, dice, player):
        if player.minutes["Small Straight"] is None:
            player.set_small_straight(dice)
            points = font.render(str(player.minutes["Small Straight"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,443,100,25))

    def set_large_straight(self, dice, player):
        if player.minutes["Large Straight"] is None:
            player.set_large_straight(dice)
            points = font.render(str(player.minutes["Large Straight"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,467,100,25))

    def set_full_house(self, dice, player):
        if player.minutes["Full House"] is None:
            player.set_full_house(dice)
            points = font.render(str(player.minutes["Full House"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,491,100,25))

    def set_chance(self, dice, player):
        if player.minutes["Chance"] is None:
            player.set_chance(dice)
            points = font.render(str(player.minutes["Chance"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,515,100,25))

    def set_yatzy(self, dice, player):
        if player.minutes["Yatzy"] is None:    
            player.set_yatzy(dice)
            points = font.render(str(player.minutes["Yatzy"]),True, BLACK, WHITE)
            SCREEN.blit(points, pygame.Rect(152,538,100,25))


class EventHandler:
    """Class to handle events in the game """

    def __init__(self, dices: Dices, players : list):
        self.dices = dices
        self.dices_to_hold = []
        self.players = players
        self.dice_drawer = DrawDice(self.dices)
        self.running = True
        self.yatzy_sheet = DrawYatzy()

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
                pygame.draw.rect(SCREEN,WHITE, pygame.Rect(100,0,600,115))

                self.dice_drawer.draw_all()
                self.dices_to_hold = []

    def set_upper_part(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 169<=event.pos[1]<=192:
                self.yatzy_sheet.set_upper_part(1, self.dices, self.players)
                self.next_turn()
            if 193<=event.pos[1]<=216:
                self.yatzy_sheet.set_upper_part(2, self.dices, self.players)
                self.next_turn()
            if 217<=event.pos[1]<=240:
                self.yatzy_sheet.set_upper_part(3, self.dices, self.players)
                self.next_turn()                
            if 241<=event.pos[1]<=264:
                self.yatzy_sheet.set_upper_part(4, self.dices, self.players)
                self.next_turn()
            if 265<=event.pos[1]<=288:
                self.yatzy_sheet.set_upper_part(5, self.dices, self.players)
                self.next_turn()
            if 289<=event.pos[1]<=312:
                self.yatzy_sheet.set_upper_part(6, self.dices, self.players)
                self.next_turn()
    
    def set_pair(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 342<=event.pos[1]<=365:
                self.yatzy_sheet.set_pair(self.dices, self.players)
                self.next_turn()

        
    def set_two_pair(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 366<=event.pos[1]<=389:
                self.yatzy_sheet.set_two_pair(self.dices, self.players)
                self.next_turn()

    def set_3_of_a_kind(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 390<=event.pos[1]<=413:
                self.yatzy_sheet.set_3_of_a_kind(self.dices, self.players)
                self.next_turn()

    def set_4_of_a_kind(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 414<=event.pos[1]<=437:
                self.yatzy_sheet.set_4_of_a_kind(self.dices, self.players)
                self.next_turn()

    def set_small_straight(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 438<=event.pos[1]<=461:
                self.yatzy_sheet.set_small_straight(self.dices, self.players)
                self.next_turn()

    def set_large_straight(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 462<=event.pos[1]<=485:
                self.yatzy_sheet.set_large_straight(self.dices, self.players)
                self.next_turn()

    def set_full_house(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 486<=event.pos[1]<=509:
                self.yatzy_sheet.set_full_house(self.dices, self.players)
                self.next_turn()

    def set_chance(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 510<=event.pos[1]<=533:
                self.yatzy_sheet.set_chance(self.dices, self.players)
                self.next_turn()

    def set_yatzy(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and 122<=event.pos[0]<=199:
            if 534<=event.pos[1]<=557:
                self.yatzy_sheet.set_yatzy(self.dices, self.players)
                self.next_turn()

    def set_lower_part(self, event):
        self.set_pair(event)
        self.set_two_pair(event)
        self.set_3_of_a_kind(event)
        self.set_4_of_a_kind(event)
        self.set_small_straight(event)
        self.set_large_straight(event)
        self.set_full_house(event)
        self.set_chance(event)
        self.set_yatzy(event)

    def set_total(self):
        if self.players.check_total():
            points = 0 
            for item in self.players.minutes:
                if isinstance(self.players.minutes[item], int):
                    points += self.players.minutes[item]
            total_points = font.render(str(points),True, BLACK, LIGHT_RED)
            SCREEN.blit(total_points, pygame.Rect(152,567,100,25))
        else:
            return

    def next_turn(self):
        self.dices.next_turn()
        pygame.draw.rect(SCREEN,WHITE, pygame.Rect(100,0,600,115))
        self.dice_drawer.draw_all()




    def quit(self, event):
        """Method to quit the game"""
        if event.type == pygame.QUIT:
            self.running = False

    def handle_events(self):
        """Check all occurred events"""
        while self.running:
            for event in pygame.event.get():
                TIMER.tick(FPS)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)
                self.dice_drawer.draw_all()
                self.hold_dice(event)
                self.undo_hold_dice(event)
                self.roll_dice(event)
                self.quit(event)
                self.set_upper_part(event)
                self.set_lower_part(event)
                self.set_total()
                pygame.display.flip()