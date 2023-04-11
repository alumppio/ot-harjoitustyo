from config.dice import Dices
from config.gui import EventHandler


def main():
    dices = Dices()
    event_handler = EventHandler(dices)

    event_handler.handle_events()


if __name__ == "__main__":
    main()
