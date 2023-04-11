import game
import gui

def main():
    dices = game.Dices()
    event_handler = gui.EventHandler(dices)

    event_handler.handle_events()
if __name__ == "__main__":
    main()
