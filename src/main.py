from config.player import Player
from config.dice import Dices
from config.main_loop import MainLoop
from config.pygame_initial import Start


def main():
    Start()
    dices = Dices()
    player = Player()

    game = MainLoop(dices, player)
    game.handle_events()


if __name__ == "__main__":
    main()
