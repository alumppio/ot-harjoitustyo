# Jatsipeli

Jatsi on noppapeli, jota voi pelata kahdestaan tai suuremassa ryhmässä. Pelissä kerätään pisteitä [jatsin sääntöjen](https://fi.wikipedia.org/wiki/Yatzy) mukaisesti, ja eniten pisteitä pelannut pelaaja/joukkue voittaa.

# Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/dokumentit/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/dokumentit/tyoaikakirja.md)
- [Changelog](dokumentaatio/dokumentit/changelog.md)
- [Arkkitehtuurikuvaus](dokumentaatio/dokumentit/arkkitehtuuri.md)

# Komentorivitoiminnot 

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
poetry run invoke pylint
```

