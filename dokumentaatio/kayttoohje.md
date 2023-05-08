# Käyttöohje

Lataa jatsipelin viimeisin [release](https://github.com/alumppio/ot-harjoitustyo/releases) ja pura paketti.

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

Aluksi jatsipelissä valitaan pelaajalle oma nimi kirjoittamalla näppäimistöllä haluama merkkiyhdistelmä (max 8. merkkiä). Painamalla enter lukiset nimen ja voit aloittaa jatsipelin pelaamisen.

![image](https://user-images.githubusercontent.com/98692578/235775875-9d716002-9347-497b-b3d7-349ba30ed464.png)

Peliä pelataan hiiren klikkausten avulla. Mikäli klikkaa jatsipaperin kohtia asettaa pisteen, asettaa kohtaan pisteen tai ruksaa sen yli, jos tähän ei voi asettaa mitään. 

![image](https://user-images.githubusercontent.com/98692578/235776423-7d9065d6-e048-40ed-a4ef-cb0a8585bea3.png)

Noppia voi heittää kaksi kertaa uudestaan ja halutessaan osia nopista voi pitää samana klikkaamalla niitä

![image](https://user-images.githubusercontent.com/98692578/235776647-2e3c3a8b-3bc9-4244-8027-bba175cf0671.png)

Peli loppuu siihen, kun kaikki kohdat on saatu täytettyä pisteillä tai rukseilla. Lopulliset pisteet näkyvät viimeisessä sarakkeessa. Peli itsessään ei lopu sillä pelin teko on vielä vaiheessa, joten jos pelin haluaa sulkea täytyy painaa ikkunan raksia.

![image](https://user-images.githubusercontent.com/98692578/235777274-a0c1105d-cacd-4730-95e5-c29c17172da0.png)
