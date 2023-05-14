# Ohjelmistotekniikka, harjoitustyö

## MySokoban
MySokoban on pelisovellus, jota voi pelata yksi pelaaja kerrallaan. Peliä pelataan siirtämällä pelihahmoa nuolinäppäimien avulla. Pelin tavoitteena on siirtää käytävillä olevat pallot varastoon. Pelin voi läpäistä usealla eri tavalla. Peli päättyy, kun kaikki pallot on saatu varastoon merkityille paikoille, tai kun pelaaja sulkee pelin.


## Dokumentaatio

- [Käyttöohje](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/käyttöohje.md)

- [Vaatimusmäärittely](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/changelog.md)

- [Tuntikirjanpito](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/tuntikirjanpito.md)

- [Arkkitehturi](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/arkkitehtuuri.md)

- [Testikattavuusraportti](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/testaus.md)


## Komentorivitoiminnot

### Ohjelman testit suoritetaan komennlla:
```poetry run invoke test```

### Ohjelman testikattavuusraportin voi muodostaa komennolla:
```poetry run invoke coverage-report```
- Komento luo HTML-muotoisen raportin projektin juurihakemistossa sijaitsevaan **htmlcov**-hakemistoon.

### Koodin laadun voi tarkistaa komennolla:
```poetry run invoke lint```

