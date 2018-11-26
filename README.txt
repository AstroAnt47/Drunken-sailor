################################################################################
README is in Finnish.
################################################################################
1. Ohjelma
2. Ajaminen
3. Asetelma



1)
Ohjelma on koodattu Pythonin 2.7-versiolla. Lisäksi koodi käyttää seuraavia
paketteja: random, time, numpy ja matplotlib.pyplot.

Koodi on tiedostossa Random_Walk.py.
Ohjelma tuottaa tiedoston Tracked_Path.txt, johon tallentuu kävelijän kuljettu
reitti. Ohjelma piirtää satunnaiskävelijöiden reitit.


2)
Ohjelma ajetaan komentoriviltä.
>python Random_Walk.py
Ohjelma tulostaa komentoriville tekstiä ja ohjeita. Ohjelma kysyy käyttäjältä
kuinka humalassa seilori on (kyllä tai ei) ja montako seiloria pubista lähtee.

Tulokset näkyvät komentorivillä. Piirretyt reitit näkyvät erillisessä ikkunassa.


3)
Drunken Sailor on satunnaiskävelijä, joka pyrkii pubista (0,0) rantaan (10,y).
Laiva lähtee 10 tunnin kuluttua, joten seilorin on löydettävä ranta ennen tätä.
Seilorilla on 50 vuotta elinaikaa.

Ranta on kymmenen korttelin päässä pubista. Jokainen kortteli on 100m x 100m
neliö. Seilori kävelee risteyksestä risteykseen yhdessä minuutissa. Joka
risteyksessä humalainen seilori valitsee suunnan täysin satunnaisesti - hän voi
jopa kääntyä takaisin tulosuuntaansa.

Käyttäjä valitsee onko seilori hyvin humalassa vai vain vähän humalassa. Hyvin
humalassa seilori ei tunnista risteyksiä, joista on jo kävellyt. Vähemmän
humalassa seilori jättää kulkiessaan tyhjiä rommipulloja risteyksiin. Mikäli
seilori törmää tyhjään pulloon, menettää hän toivonsa ja seuraa pulloja
takaisin pubiin.

Käyttäjä valitsee myös montako seiloria pubista lähtee kohti rantaa. Jos
seilorit ovat hyvin humalassa, saattaa kaikkien reittien laskemiseen kulua
hetki. Vähemmän humalassa olevien reitit ovat yleensä lyhyempiä eli
nopeampia laskea.


y                                Ranta (10,y)
|                               |
|                               |
|                               |
|                               |
| Pubi (0,0)                    |
|#______________________________|________ x
| x=0                           |
|                               |
Jokainen askel on 100 metriä (1 minuutti)
