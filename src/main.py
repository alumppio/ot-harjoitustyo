from config.main_loop import MainLoop
from config.game_setup import Setup
from config.end_game import EndGame


def main():
    '''Main function that runs the game'''
    setup = Setup()
    setup.game_setup()
    game = MainLoop(setup.event_handlers)
    game.handle_events()
    endgame = EndGame(game.players)
    endgame.end_game()


if __name__ == "__main__":
    main()
