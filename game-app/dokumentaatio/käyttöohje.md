## Käyttöohje
Laataa ohjelman [releasen](https://github.com/SaNi19/ot-harjoitustyo/releases/tag/Loppupalautus) lähdekoodi ja siirry kansioon **Game-app.**
## Ohjelman käynnistäminen

### Ohjelma alustetaan komennolla:
```poetry install```

### Ohjelma käynnistetään komennolla:
```poetry run invoke start```

Ohjelman käynnistys avaa näytölle pelilaudan, jossa peliä pelataan nuolinäppäimine avulla. Pelin tavoitteena on siirtää pelihahmon avulla kaikki siniset pallot varastoon punaisilla rasteilla merkityille paikoille. Pallot muuttuvat keltaiksi silloin, kun ne ovat oikeilla paikolla. Pelihahmoa tai palloa ei voi liikuttaa seinän läpi. Pelihahmo voi liikuttaa vain yhtä palloa kerrallaan. Peli päättyy, kun kaikki pallot on saatu varastoon. Pelilaudan alareunassa näkyy pelissä käytetyt askeleet ja paras pelitulos. Uuden peli voi aloittaa **New game** -painikkeella ja pelin voi sulkea **Guit** -painikkeesta.

### Pelin aloitusnäkymä
![MySokoban](https://github.com/SaNi19/ot-harjoitustyo/blob/master/MySokoban_star.png)

### Pelin päättymisnäkymä
![MySokoban](https://github.com/SaNi19/ot-harjoitustyo/blob/master/MySokoban_end.png)
