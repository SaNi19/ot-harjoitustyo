# Testausdokumentti #

Ohjelman testikattavuus jäi hyvin pieneksi. Testit testaavat pääasiassa pelilaudan rakennetta. 
Lukemattomista yrityksistä huolimatta en saanut yhtään toimivaa testiä, joka olisi testanuut pelihahmon tai pallon liikkumista. 

## Testikattavuusraportti ##

![Testikattavuusraportti](https://github.com/SaNi19/ot-harjoitustyo/blob/master/Testikattavuusraportti.png)

## Ohjelman toiminnallisuus ##
Ohjelmaa on testattu paljon pelaamalla. Käytössä on ollut myös pienempi pelilauta, joka helpottaa testaamista. Ohjelma on toiminut hyvin ja läpäisty peli tuottaa toivotun lopputuloksen lopputeksteineen. Tietokaantatallennus toimii ja paras tulos päivittyy oikein.

## Asennus ja käyttöohje ##
Ohjelma on ladattu ja asennettu käyttöohjeen mukaisesti ja ohjelma toimii hyvin.

## Sovellukseen jääneet puutteet ja virheet ##
- Ohjelma voi kaatua virheeseen, jos tietokanta on tyhjä.
- Testikattavuus on vielä aivan liian alhainen.
- Pylin-virheitä on vielä aika paljon, joista suurin osa tulee koodin Docstring-kommenteista.
- Ohjelma ei tulosta virheviestiä, jos käyttäjä painaa jotakin muuta, kuin ohjelmaan määriteltyjä toimintanäppäimiä.
- Luokat voisivat olla omissa kansioissa.
- `MySokoban`-luokka on vielä aivan liian suuri, vaikka pelihahmon liikkumiselle on lisätty oma `MovePlayer`-luokka.
