# Käyttöohje

Lataa jatsipelin viimeisin [release](https://github.com/alumppio/ot-harjoitustyo/releases) ja pura paketti. Pelin pisteet lasketaan [jatsipelin sääntöjen](https://fi.wikipedia.org/wiki/Yatzy#P%C3%B6yt%C3%A4kirja) mukaisesti

## Ohjelman käynnistys
Ennen käynnistämistä täytyy poetry alustaa
```bash
poetry install
```
Tämän jälkeen täytyy alustaa pelin huippupistetaulukko komennolla

```bash
poetry run invoke build
```

Tämän jälkeen ohjelman voi käynnistää komennolla
```bash
poetry run invoke start
```

## Pelaaminen

Kun peli käynnistetään, niin peli kysyy kuinka monta pelaajaa pelaa. Tässä valinta tehdään kirjoittamalla haluama pelaajamäärä ja painetaan enter jatkaakseen. Askelpalauttimella voi kumittaa halutun määrän ja valita uudestaan.
![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/13422da1-6689-416d-a261-2dead0c25692)

Tämän jälkeen valitaan pelaajien nimet. Nimet valitaan kirjoittamalla nimi näppäimistöllä ja painamalla enter. Askelpalauttimella voi kumittaa vääriä merkkejä.

![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/bc5aae6e-df5b-4792-b839-a2812e9ca313)

Peliä pelataan hiiren klikkausten avulla. Mikäli klikkaa jatsipaperin kohtia asettaa pisteen, asettaa kohtaan pisteen tai ruksaa sen yli, jos tähän ei voi asettaa mitään. Punaisella nuolella nähdään kenen pelaajan vuoro on käynnissä.

![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/a5f1be44-9655-4ec0-955a-f9297707742b)


Noppia voi heittää kaksi kertaa uudestaan ja halutessaan osia nopista voi pitää samana klikkaamalla niitä

![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/a1b03ac7-65b4-4db5-b22f-604e3e4ef43d)

Peli loppuu siihen, kun kaikki kohdat on saatu täytettyä pisteillä tai rukseilla. Lopulliset pisteet näkyvät viimeisessä sarakkeessa. Peli ei korosta kuka on voittanut pelin, mutta korkeimmat pisteet kerännyt pelaaja voittaa. Peli jää hetkeksi aikaa paikoilleen, jotta voidaan nähdä kuka on voittanut.

![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/27980852-3976-41e8-aa33-0c1403ed0575)

Tämän jälkeen peli on lopunnut, mutta lopuksi vielä näytetään tietokannan korkeimmat pisteet. Peli jälleen jää paikoilleen hetkeksi aikaa, jotta voidaan nähdä kuka on saanut korkeimmat pisteet.
![image](https://github.com/alumppio/ot-harjoitustyo/assets/98692578/ba29071a-5056-4ca7-b41a-2f0aed17766b)

