## Luokkakaavio ##
![Luokkakaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/arkkitehtuuri.png)

## MySokoban-pelin pelisilmukan toiminta ##
Kun ohjelma käynnistetään, *main*-metodi kutsuu luokkaa MySokobaan. Pelin alustuksen jälkeen peli siirtyy *loop*-silmukkaa ja toimii seuraavalla tavalla:

![Sekvenssikaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/MySokoban_sekvenssikaavio.png)
- *loop*-metodi kutsuu *events*-metodia
- *events* kutsuu *event.get*-metodia
- *even.get* palauttaa pelaajan painaman näppäimen arvon *events*-metodille
- *events* kutsuu *move*-metodia *even.get*-metodin palauttamilla y- ja x-arvoilla
- *move*-metodi kutsuu *find*-metodia, joko palauttaa rivin ja sarakkeen, jossa pelihahmo sijaitsee pelilaudalla
- *move*-metodi palauttaa arvon *events*-metodille
- ohjelma palaa takaisin *loop*-metodiin, jossa seuraavana on vuorossa *display_game*-metodin suoritus
