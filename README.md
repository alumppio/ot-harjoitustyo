# Jatsipeli

Jatsi on noppapeli, jota voi pelata kahdestaan tai suuremassa ryhmässä. Pelissä kerätään pisteitä [jatsin sääntöjen](https://fi.wikipedia.org/wiki/Yatzy) mukaisesti, ja eniten pisteitä pelannut pelaaja/joukkue voittaa.

- [Release 1](https://github.com/alumppio/ot-harjoitustyo/releases/tag/viikko5)
- [Release 2](https://github.com/alumppio/ot-harjoitustyo/releases/tag/viikko6)

# Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirja.md)
- [Changelog](dokumentaatio/changelog.md)
- [Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](dokumentaatio/kayttoohje.md)
- [Testausdokumentti](dokumentaatio/testausdokumentti.md)

# Komentorivitoiminnot 

### _Ennen suoritusta:_

Alusta huippupistetaulukko komennolla:
```bash
poetry run invoke build
```

## Ohjelman suoritus
Suorita ohjelma komentoriviltä komennolla:
```bash
poetry run invoke start
```

## Ohjelman testaus

Ohjelman testit voidaan suorittaa komentoriviltä komennolla:
```bash
poetry run invoke test
```

ja näistä voidaan luoda testikattavuusraportti komentoriviltä komennolla:
```bash
poetry run invoke coverage-report
```

## Pylint 

Ohjelman koodin staattisen laadun voi tarkistaa pylint-testeillä, jotka voidaan suorittaa komentoriviltä komennolla:
```bash
poetry run invoke lint
```

