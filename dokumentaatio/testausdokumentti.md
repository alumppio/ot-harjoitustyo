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

Testikattavuus raportin saa luotua komentoriviltä komennolla (mikäli poetry shell on käytössä)
```bash
poetry run invoke coverage-report
```
![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/f61adf8e-f8c4-471b-a4de-fc0d4dc59db7)

Testauksen haaraumakattavuus on 76%.

Haaraumakattavuus voisi olla korkeampi, mutta logiikka tiedostojen testaaminen on vaikeaa, sillä miltein jokainen niistä sisältää pitkiä luuppeja. Lisäksi osa näyttöön piirtämisestä vastuussa olevat tiedostot ovat hieman vajaammin testattu, sillä niiden testaus tapahtuu muiden tiedostojen testien yhteydessä. 

## Järjestelmätestaus

Järjestelmätestaus on suoritettu pelaamalla peliä manuaalisesti.

### Toiminnallisuudet

[Käyttöohjeen](dokumentaatio/kayttoohje.md) ja [määrittelydokumentin](dokumentaatio/vaatimusmaarittely.md) asiat on käyty läpi. Toiminnalisuuden testauksessa on myös käsitelty virheellisiä syötteitä. 

## Sovelluksen laatuongelmat

Pelin voittanut pelaaja ei korostu mitenkään, kun peli loppuuu. 
