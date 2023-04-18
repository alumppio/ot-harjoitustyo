from config.player import Player
from config.dice import Dices
from config.gui import EventHandler


def main():
    dices = Dices()
    player = Player()
    event_handler = EventHandler(dices, player)
    event_handler.handle_events()

if __name__ == "__main__":
    main()
