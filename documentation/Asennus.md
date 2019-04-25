# Asennusohje <h1>

## Kuinka sovellus asennetaan paikallisesti <h2>

- Kloonaa repositorio
- Navigoi projektin juureen ja asenna riippuvuudet komennolla `pip install -r requirements.txt`
- Käynnista sovellus komennolla `python3 run.py`
- Sovellusta voi nyt käyttää selaimesta osoitteesta http://localhost:5000/

## Kuinka sovellus asennetaan herokuun <h2>

- Aja komento `heroku create <haluamasi_nimi>`
- Lisää paikalliseen versionhallintaan herokun etärepositorio komennolla
  `git remote add heroku https://git.heroku.com/<äsken_määrittämäsi_nimi>.git`
- Pushaa projekti herokuun komennolla `git push heroku master`



