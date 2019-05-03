# Asennusohje <h1>

## Kuinka sovellus asennetaan paikallisesti <h2>

- Kloonaa repositorio
- Navigoi projektin juureen ja asenna riippuvuudet komennolla `pip install -r requirements.txt`
- Ota käyttöön virtuaaliympäristö komennoilla:
`python3 -m venv venv` ja 
`source venv/bin/activate`

- Ennen ensimmäistä käynnistystä, käy määrittelemässä projektin juureen .env tiedostoon haluttu admin-tilin tunnus
ja salasana muodossa `USERNAME=tunnus` ja `PASSWORD=salasana`
- Käynnista sovellus komennolla `python3 run.py`
- Sovellusta voi nyt käyttää selaimesta osoitteesta http://localhost:5000/

## Kuinka sovellus asennetaan herokuun <h2>

- Aja komento `heroku create <haluamasi_nimi>`
- Lisää paikalliseen versionhallintaan herokun etärepositorio komennolla
  `git remote add heroku https://git.heroku.com/<äsken_määrittämäsi_nimi>.git`
- Lisää sovellukselle mahdollisuus tietää olevansa herokussa komennolla `heroku config:set HEROKU=1`
- Määrittele haluttu admin-tunnus ja salasana komenoilla `heroku config:set USERNAME=tunnus` ja `heroku config:set PASSWORD=salasana`
- Pushaa projekti herokuun komennolla `git push heroku master`



