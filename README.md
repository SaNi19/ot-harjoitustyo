# Ohjelmistotekniikka, harjoitustyö

## MySokoban
MySokoban on pelisovellus, jota voi pelata yksi pelaaja kerrallaan. Peliä pelataan siirtämällä pelihahmoa nuolinäppäimien avulla. Pelin tavoitteena on siirtää käytävillä olevat pallot varastoon. Pelin voi läpäistä usealla eri tavalla. Peli päättyy, kun kaikki pallot on saatu varastoon merkityille paikoille, tai kun pelaaja sulkee pelin.


## Dokumentaatio

- [Käyttöohje](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/käyttöohje.md)

- [Vaatimusmäärittely](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/vaatimusmaarittely.md)

- [Changelog](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/changelog.md)

- [Tuntikirjanpito](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/tuntikirjanpito.md)

- [Arkkitehturi](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/arkkitehtuuri.md)

## Käyttöohje
Laataa ohjelman [releasen](https://github.com/SaNi19/ot-harjoitustyo/releases/tag/Viikko6) lähdekoodi ja siirry kansioon **Game-app.**
## Ohjelman käynnistäminen

### Ohjelma alustetaan komennolla:
```poetry install```

### Ohjelma käynnistetään komennolla:
```poetry run invoke start```

Ohjelman käynnistys avaa näytölle pelilaudan, jossa peliä pelataan nuolinäppäimine avulla. Pelin tavoitteena on siirtää pelihahmon avulla kaikki siniset pallot varastoon punaisilla rasteilla merkityille paikoille. Pallot muuttuvat keltaiksi silloin, kun ne ovat oikeilla paikolla. Pelihahmoa tai palloa ei voi liikuttaa seinän läpi. Pelihahmo voi liikuttaa vain yhtä palloa kerrallaan. Peli päättyy, kun kaikki pallot on saatu varastoon. Pelilaudan alareunassa näkyy pelissä käytetyt askeleet. Uuden peli voi aloittaa **New game** -painikkeella ja pelin voi sulkea **Guit** -painikkeesta.

### Pelin aloitusnäkymä
![MySokoban](https://github.com/SaNi19/ot-harjoitustyo/blob/master/MySokoban_star.png)

### Pelin päättymisnäkymä
![MySokoban](https://github.com/SaNi19/ot-harjoitustyo/blob/master/MySokoban_end.png)


### Ohjelman testit suoritetaan komennlla:
```poetry run invoke test```

### Ohjelman testikattavuusraportin voi muodostaa komennolla:
```poetry run invoke coverage-report```
- Komento luo HTML-muotoinen raportin projektin juurihakemistossa sijaitsevaan **htmlcov**-hakemistoon.

### Koodin laadun voi tarkistaa komennolla:
```poetry run invoke lint```

