from config.player import Player
from config.dice import Dices
from config.main_loop import MainLoop
from config.game_setup import Setup


def main():
    '''Main function that runs the game'''
    dices = Dices()
    player = Player()
    setup = Setup()

    # Soon adding the option for multiple players
    setup.game_setup(player)
    game = MainLoop(dices, player)
    game.handle_events()


if __name__ == "__main__":
    main()
