# Jatsipeli

Jatsi on noppapeli, jota voi pelata kahdestaan tai suuremassa ryhmässä. Pelissä kerätään pisteitä [jatsin sääntöjen](https://fi.wikipedia.org/wiki/Yatzy) mukaisesti, ja eniten pisteitä pelannut pelaaja/joukkue voittaa.

# Dokumentaatio

- [Vaatimusmäärittely](dokumentaatio/vaatimusmaarittely.md)
- [Työaikakirjanpito](dokumentaatio/tyoaikakirja.txt)
- [Changelog](dokumentaatio/changelog.md)


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

