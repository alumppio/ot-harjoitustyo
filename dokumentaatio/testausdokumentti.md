# Testausdokumentti 

Ohjelmaan on testattu manuaalisin testein koko ohjelman teon ajan. Tämän lisäksi ohjelmaa on testattu automaattisten unittestien avulla, joissa käsitellään mahdollisia pelin tapahtumia. 

## Automaattiset testit

Sovelluslogiikka on jakautunut useampaan tiedostoon ja jokaisessa tests-kansion tiedostossa testataan jonkin tiedoston logiikkaa. 

'end_test.py'-tiedosto testaa tiedoston 'end_game.py' luokkaa 'EndGame' hyödyntäen tiedostojen 'gui.py', 'dice.py' ja 'player.py' vastaavia luokkia 'EventHandler', 'Dices' ja 'Player'. Testitiedosto myöskin hyödyntää 'connection'-tiedoston tietokantaan liittyvää 'CONNECTION'-oliota.

'game_setup_test.py'-tiedosto testaa tiedoston 'game_setup.py' luokkaa 'Setup' hyödyntäen 'player.py'-tiedoston luokkaa 'Player'.

'game_test.py'-tiedosto testaa tiedostojen 'dice.py' ja 'player.py' luokkia 'Dices' ja 'Player'.  

'gui_test.py'-tiedosto testaa tiedoston 'gui.py' luokkaa 'EventHandler' hyödyntäen tähän tiedostojen 'dice.py' ja 'player.py' luokkia 'Dices' ja 'Player'. Tiedosto samalla käyttää 'constants.py'-tiedoston vakioita tuomalla niitä testitiedostoon.

'main_loop_test.py'-tiedosto testaa tiedoston 'main_loop.py' luokkaa 'MainLoop' hyödyntäen tiedostojen 'dice.py', 'player.py' ja 'gui.py' luokkia 'Dices', 'Player' ja 'EventHandler'.

## Testikattavuus
