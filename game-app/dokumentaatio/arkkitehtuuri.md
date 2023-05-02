## Luokkakaavio ##
![Luokkakaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/arkkitehtuuri.png)

## MySokoban-pelin pelisilmukan toiminta ##
Kun ohjelma käynnistetään, *main*-metodi kutsuu luokkaa MySokobaan. Pelin alustuksen jälkeen peli siirtyy *loop*-silmukkaa ja toimii seuraavalla tavalla:

![Sekvenssikaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/MySokoban_sekvenssikaavio.png)
- *loop*-metodi kutsuu *events*-metodia
- *events* kutsuu *event.get*-metodia
- *even.get* palauttaa pelaajan painaman näppäimen arvon *events*-metodille
- *events* kutsuu *move*-metodia *even.get*-metodin palauttamilla nuolinäppäimen y- ja x-arvoilla
- *move*-metodi kutsuu *game_end*-metodia, joka palauttaa *True*, jos peli on valmis, muuten *False*
- jos vastaus on *False*, *move*-metodi kutsuu *find*-metodia, joko palauttaa rivin ja sarakkeen, jossa pelihahmo sijaitsee pelilaudalla
- *move*-metodi tarkistaa, voiko pelihahmo liikkua annettuun suuntaan
- jos liikkuminen on sallittu, *move*-metodi palauttaa uuden arvon *events*-metodille, muutoin arvo pysyy samana
- ohjelma palaa takaisin *loop*-metodiin, jossa seuraavana on vuorossa *display_game*-metodin suoritus
