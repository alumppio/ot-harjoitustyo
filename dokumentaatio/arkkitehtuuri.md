# Arkkitehtuurikuvaus


## Rakenne
Ohjelma koostuu useammasta tiedostosta ja pääpelilooppi suoritetaan tiedostossa main_loop.py. Itse pelikäynnistetään main.py tiedostolla. Kansiossa repositories on tiedosto constants.py, joka sisältää peliin liittyviä vakioita.

```mermaid
    classDiagram
        main .. config
        repositories .. config : Vakioita
        repositories .. visual : Vakioita
        resources .. repositories : Pelissä käytettäviä kuvia
        config .. visual
        services .. config
        services .. visual

        class config{
            dice.py
            end_game.py
            gui.py
            main_loop.py
            player.py
            folder : visual
        }

        class visual{
            draw_dice.py
            draw_yatzy.py
            draw_end_game.py
        }

        class repositories{
            contants.py
            delay_time.py
        }

        class resources{
            peliin liittyviä kuvia...
        }
        
        class services{
            build.py
            connection.py
            high_scores.db
        }

```

## Sovelluslogiikka

Sovelluslogiikkaan liittyvät tiedostot löytyvät config-kansiosta. 

Kansion tiedosto dice.py sisältää luokan Dices, jotka vastaavat jatsipelin viittä noppaa.

Tiedosto gui.py käsittelee pelin graafisessa käyttöliittymässä tapahtuvat tapahtumat luokassa EventHandler. Luokka käyttää tiedoston dice.py luokkaa Dices noppien luomiseen ja tiedoston player.py luokkaa Player jatsipelin tulospaperin luomiseen.

Tiedosto main_loop.py on nimensä mukaan pelin pääluuppi, joka tarkastelee tapahtuneet tapahtumat, ja tähän main_loop.py käyttää gui.py luokkaa EventHandler.

Tiedostoa player.py käytetään jatsipelissä tarvittavan tulospaperin luomiseen. Tiedoston luokka Player luo tulospaperin ja sisältää metodit pisteiden listaamiseen. player.py käyttää tiedoston dice.py luokkaa Dices noppien luomiseen

Tiedosto pygame_initial.py alustaa pygamen.

Kansiossa **visual** on pelin ruudun piirtämiseen liittyvät tiedostot

Kansion tiedosto draw_dice.py piirtää jatsipelin nopat ja käyttää noppien luomiseen config-kansion tiedoston dice.py Dices luokkaa. Tiedosto käyttää myös repositories-kansion constant.py tiedostoa, joka sisältää peliin liittyviä vakioita. 

Tiedosto draw_yatzy.py pirtää pelin jatsipaperin ja piirtää paperiin pisteet. draw_yatzy.py käyttää repositories-kansion constants.py tiedoston vakioita.



## Toiminta

Kun ohjelma main.py suoritetaan, niin ensiksi suoritetaan pelin alustus Setup-luokan olioilla, joka toimii yksinkertaisesti sekvenssikaavion mukaisesti.

```mermaid
sequenceDiagram
    main()-->setup : Setup(), pelin alustamiseen käytettävä luokka
    main()-->setup : setup.game_setup(), aloittaa pelin alustuksen luupin, kuinka monta pelaajaa ja pelaajien nimet 
    main()-->game : MainLoop(setup.event_handlers), alustaa MainLoop-luokan olion EventHandler-luokan olioilla. MainLoop-luokan olio nimensä mukaan käsittelee pelin tapahtumia luupissa.
    main()-->game : handle_events(), käsittelee pelaamiseen liittyvät tapahtumat
    main()-->endgame : EndGame(game.players), alustaa EndGame-luokan olion, joka käsittelee pelin lopetuksen. EndGame-luokan olio alustetaan Player-luokan olioilla, joka kuvastaa jatsin tulospaperia.
    main()-->endgame : end_game(), lopettaa pelin piirtää korkeimmat pisteet taululle 
```

Tarkastellaan vielä yksityiskohtaisemmin näitä luokkia. Setup-luokan olio toimii kutakuinkin kaavion mukaisesti

```mermaid
sequenceDiagram
    main()-->setup : Setup(), pelin alustamiseen käytettävä luokka
    constants-->setup : Tarvittavia vakioita ja pygame.init()
    main()-->setup : setup.game_setup(), aloittaa pelin alustuksen luupin, kuinka monta pelaajaa ja pelaajien nimet 
    setup-->setup : game_setup(), luupissa valitaan pelaajien määrä ja nimet
    setup-->setup : amount_setup()
    loop while self.running
        setup-->setup : amount_of_players_loop(), valitaan pelajaien määrä
        setup-->setup : draw_amount_setup(number), piirtää pelaajien määrän liittyvät asiat 
    end 
    setup-->setup : name_setup(int(players_amount)), valitaan haluttujen pelaajien nimet ja lisätään nimettyjen pelaajien Player-luokka olioit setup.players listaan.
    player-->setup : Player(), Player-luokan olio, joka vastaa jatsipelin pistetaulukkoa ja sen käsittelyyn liittyviä toimintoja.
    loop while self.running : kaikille pelaajille erikseen for-luupilla
        setup-->setup : name_setup_loop(), valitaan pelaajan nimi 
    end
    setup-->setup : convert_to_event_handlers(), jokaiselle pelaajalle
    dices-->setup : Dices(), jatsipelin noppia vastaavat oliot
    gui-->setup : EventHandler(Dices(), player, pelaajan_numero), alustetaan Player-luokan oliosta EventHandler-luokan olio mainlooppia varten. Tämä luokka käsittelee pelin käyttäjän aiheuttamat tapahtumat eli hiiren klikkaukset-
    setup-->main() : setup.event_handlers
    
    
```
Tämän jälkeen main tiedostossa luodaan pelin pääluuppiin liittyvä MainLoop-luokan olio, jota käytetään kaavion mukaisesti

```mermaid
sequenceDiagram
    main()-->game : MainLoop(setup.event_handlers)
    game-->game : draw_names(), piirtää pelaajien nimet
    main()-->game : game.handle_events()
    game-->game : handle_events()
    loop while self.running : jokaiselle pelaajalle erikseen
        game-->game : event_hande_loop(EventHandler), luuppi pelaamiseen liittyvien tapahtumien tarkasteluun.
        game-->game : check_if_done(), tarkistaan onko peli pelattu loppuun
    end
```

Tässä pääluupissa tapahtuneet tapahtumat tarkastellaan event_handle_loop-metodissa, jossa käytetään EventHandler-luokan oliota. Metodi even_handle_loop toimii kutakuinkin kaavan mukaisesti

```mermaid
sequenceDiagram
    game-->game : event_handle_loop(EventHandler)
    loop while EventHandler.running : jokaiselle pelaajalle erikseen
        game-->gui : EventHandler.draw_all() 
        gui-->dice_drawer : draw_all(), tämä metodi piirtää nopat näytölle
        game-->gui : hold_dice(event), tarkastellaan pygamen kautta, onko pelaaja valinnut noppia
        game-->gui : undo_hold_dice(event), tarkastellaan pygamen kautta, onko päättänyt sittenkin olla valitsematta noppia
        game-->gui : roll_dice(event), tarkastellaan pygamen kautta, onko pelaaja halunnut heittää nopat uudelleen
        game-->gui : set_upper_part(event), tarkastelee pygamen kautta, onko pelaaja halunnut asettaa jatsipaperin yläosaan pisteitä
        game-->gui : set_lower_part(event), tarkastelee pygamen kautta, onko pelaaja halunnut asettaa jatsipaperin alaosaan pisteitä
        game-->gui : set_total(), tarkastaa onko pelaajalla jatsipaperi täynnä ja mikäli on se piirtää pisteet näytölle
        game-->gui : quit(event), tarkastaa onko pelaaja halunnut lopettaa pelin kesken
    end
```

Kun peli on pelattu loppuun, niin MainLoop-luokan olion handle_events()-metodi pysäyttää luupin. Tämän jälkeen main.py tiedostossa alustetaan EndGame-luokan olio, joka käsittelee pelin lopetuksen kaavion mukaisesti

```mermaid
sequenceDiagram
    main()-->endgame : EndGame(game.players), alustetaan olio Player-luokan olioilla, jotka kuvastavat pelaajien tulospapereita
    main()-->endgame : end_game(), lopettaa pelin
    endgame-->endgame : set_high_scores(), asettaa lopulliset tulokset tietokantaan
    endgame-->endgame : show_high_scores(), piirtää viisi parhainta pistettä tietokannasta taululle
```

## Heikkoudet

Peliä pelatessa täytyy olla tarkka klikkausten suhteen, sillä jatsipaperin ruudukot ovat todella pieniä. Pelin myöskin loppuu niin, että selvää voittajaa ei kokematon pelaaja tiedä. Korkeimmat pisteet saanut pelaaja voittaa, mutta tätä ei korosteta pelissä mitenkään. Tätä hämmennystä voi lisätä se, että lopussa nähdään viisi korkeinta pistemäärää huippupistetaulukossa, mutta pelatun pelin voittajaa ei mainita. 
