## Luokkakaavio ##
Sovelluksen luokkia ovat `MySokoban`, `GameServices` ja `MovePlayer`. Lisäksi sovelluksessa on **images**-kansio kuville ja sqlite-tietokantaa käyttävä **resultlist.db**. 
- `MySokoban`-luokka toteuttaa pelin luomisen, tapahtumien käsittelyn ja tulostuksen.
- `MovePlayer`-luokka vastaa pelihamon ja pallon sijaintien y- ja x-arvojen asettamisesta.
- `GameServices`-luokan tehtävänä on hoitaa tiedon tallennus tietokantaan ja tiedon hakeminen tietokannasta.
- **images**-kansiossa on pelilaudan kuvat jotka tallennetaan *imageset*-taulukkoon.
- **resultlist.db** on sqliteä käyttävä tietokantataulu, johon tallennetaan pelin tulos ja josta haetaan kaikkien pelattujen pelien paras tulos.

![Luokkakaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/Luokkakaavio.png)

## MySokoban-pelin pelisilmukan toiminta ##
Kun ohjelma käynnistetään, *main*-metodi kutsuu luokkaa `MySokobaan`. Pelin alustuksen jälkeen peli siirtyy *loop*-silmukkaa ja toimii seuraavalla tavalla:

![Sekvenssikaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/game-app/dokumentaatio/MySokoban_sekvenssikaavio.png)
- *loop*-metodi kutsuu *events*-metodia
- *events* kutsuu *event.get*-metodia
- *even.get* palauttaa pelaajan painaman näppäimen arvon *events*-metodille
- *events* kutsuu `MovePlayer`luokan *move*-metodia *even.get*-metodin palauttamilla nuolinäppäimen y- ja x-arvoilla
- *move*-metodi kutsuu `MySokoban`-luokan *game_end*-metodia, joka palauttaa *True*, jos peli on valmis, muuten *False*
- jos vastaus on *False*, *move*-metodi kutsuu `MySokoban`luokan *find*-metodia, joko palauttaa rivin ja sarakkeen, jossa pelihahmo sijaitsee pelilaudalla
- *move*-metodi tarkistaa, voiko pelihahmo liikkua annettuun suuntaan
- jos liikkuminen on sallittu, *move*-metodi palauttaa uuden arvon `MySokoban`-luokan *events*-metodille, muutoin arvo pysyy samana
- ohjelma palaa takaisin `MySokoban`-luokan *loop*-metodiin, jossa seuraavana on vuorossa *display_game*-metodin suoritus

## MySokoban-pelin tietokannan toiminta ##

![GameServices-sekvenssikaavio](https://github.com/SaNi19/ot-harjoitustyo/blob/master/GameServices%20sekvenssikaavio.png)
- `GameServices`-luokan *add_game_result*-metodi saa `MySokoban`-lukoan *game_end*-metodilta pelissä käytetyt askeleet ja tallentaa ne tietokantaan
- `GameServices`luokan *best_result*-metodi saa `MySokoban`-luokan *event*-metodilta pyynnön ja palauttaa tietokannasta pienimmän askelmäärän
- jos tietokanassa ei ole yhtään tulosta, palauttaa viestin "*No results yet!*

## Ohjelman rakeenteelliset ongelmat ##

Ohjelman tietokanta on toteutettu ja käytetty ennen parhaan tuloksen tulostuksen toteutusta. Jos alustetaan uusi tietokanta ja yhtään peliä ei ole pelattu, kaatuu ohjelma virheeseen. Ongelman tuottaa `GameServices`-luokan *best_result*-metodi, joka yrittää hakea parhaan tuloksen tyhjästä tietokannasta. Yritin kiertää ongelman lisäämällä heti pelin alussa yhden tuloksen tietokantaan ennen pelisilmukan käynnistymistä.
