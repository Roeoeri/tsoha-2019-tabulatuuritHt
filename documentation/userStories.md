# User Stories <h1>
  
  - Käyttäjän on mahdollista nähdä kaikki sivustolle talletetut tabulatuurit listana.
  ~~~~sql
  Totetuttava lause: 
  
  Select * from tab;
  ~~~~
  - Käyttäjän on mahdollista rekisteröityä sivustolle.
  ~~~~sql
  Toteuttava lause:
  
  Käyttäjän lisääminen käyttäjätauluun:
  
  Insert into account (username, password) Values (käyttäjäntunnus, salasana);
  
  Käyttäjän roolin id:n hakeminen:
  
  Select id from role where role.name = rooli;
  
  Roolin ja käyttäjän yhdistäminen liitostauluun
  
  Insert into roles_users (user_id, role_id), Values(kayttajaId, rooliId);
  ~~~~
  - Käyttäjän on mahdollista kirjautua sivustolle.
  ~~~~sql
  Toteuttava lause: 
  
  Itse kirjatumislogiikka hoidetaan ohjelmallisesti, mutta käyttäjän tiedot (mukaanlukien hashshattu salasana) haetaan seuraavasti:
  
  Select * from account Where account.username = haettavaKäyttäjä;
  ~~~~
  - Kirjautuneen käyttäjän on mahdollista muokata yksittäistä sivustolleen lisäämää tabulatuuria.
   ~~~~sql
   Toteuttava lause:
   Kirjatuneen käyttäjän oikeus muokata/poistaa tabulatuuria tarkistetaan ohjelmmallisesti vertaamalla käyttäjän tarkasteleman tabulatuurin viiteavavainta käyttäjän id:seen:
   
   Tabulatuurin viiteavaimen saa esimerkiksi näin:
   
   Select account_id from tab where tab.id = haettavanTabulatuurinId
   
   Kirjautuneella käyttäjällä on puolestaan aina tieto omasta id:stään joten vertailu on helppoa.
   
   Itse muokkaus:
   
   Update tab 
      Set tab.name= uusinimi, tab.content=uusisisältö
      Where tab.id = tabulatuurinId;
   ~~~~
  
  - Kirjautuneen käyttäjän on mahdollista lisätä sivustolle tabulatuureja.
  ~~~~sql
  Toteuttavat lauseet:
  
  Tabin lisääminen:
  Insert into tab(name, content, account_id) Values(nimi,sisältö,tilinId);
  
  Tabin ja genren yhdistäminen liitostaulussa:
  Insert into genre_tab(genre_id, tab_id) Values (tabinId, tilinId);
  ~~~~
  
  - Kirjautuneen käyttäjän on mahdollista poistaa lisäämänsä tabulatuuri.
  ~~~~sql
  Toteuttava lause:
  
  Delete from tab Where tab.id = poistettavanTabinId;
  ~~~~
  - Kirjautuneen käyttäjän on mahdollista lisätä sivustolle genrejä.
  ~~~~sql
  Toteuttava lause:
  Insert into genre(genre) Values(lisattavaGenre)
  ~~~~
  - Admin-käyttäjä voi poistaa tai muokata kaikkia sivustolla olevia tabulatuureja.
  ~~~~sql
  Toteuttava lause:
  
  Käyttäjän adminoikeus tarkistetaan ohjelmallisesti, tarkistamalla onko käyttäjän rooleissa admin nimistä roolia.
  Tarkistettava lista saadaan suunnilleen näin 
  
  Select role.name from role 
  Join roles_users On role.id = roles_user.role_id
  Join account on account.id = roles_users.account_id
  Where account.id = haettavaKayttaja
  
  Muuten poistaminen luonnistuu kuin muillakin käyttäjillä.
  ~~~~
  - Admin-käyttäjän on mahdollista poistaa ja muokata genrejä.
  ~~~~sql
  Toteuttavat lauseet:
  
  Poisto:
  
  Delete from genre where id = poistettavanId
  
  Muokkaus 
  
  Update genre
  Set genre = uusiGenre
  Where genre.id = muokattavaId
  
  ~~~~
  - Käyttäjän on mahdollista nähdä statistiikkaa siitä, kuinka paljon tabulatuureja kussakin genressä on.
  ~~~~sql
  Toteuttava lause:
  
  Select genre.genre, count(*) 
  From genre_tab 
  Join genre on genre.id = genre_tab.genre_id
  Group by genre.genre

  ~~~~
  - Käyttäjän on mahdollista hakea tabulatuureja kappaleiden genrejen perusteella.
  ~~~~sql
  Toteuttava lause: 
  
  Select tab.name, tab.id from genre 
  Join genre_tab on genre.id = genre_tab.genre_id 
  Join tab on tab.id = genre_tab.tab_id
  Where genre.id = haettavanGenrenId
  ~~~~
  
  - Käyttäjän on mahdollista hakea yksittäistä tabulatuuria sivustolta kappaleen nimen perusteella.
  ~~~~sql
  Toteuttava lause:
  
  Select * from tab
  Where tab.name Like %hakusana% 
  ~~~~
  - Käyttäjän on mahdollista hakea tabulatuureja tabulatuurin kirjoittaneen käyttäjän perusteella.
  ~~~~sql
  Toteuttava lause:
  Select * from tab 
  Where tab.account_id = haettavanKäyttäjänId
  ~~~~
  
  
  - Käyttäjän on mahdollista nähdä "Hall of fame", jossa näytetään kolme sivustolle eniten tabulatuureja lisännyttä käyttäjää.
   ~~~~sql
  Toteuttava lause:
  Select account.id,  account.username, Count(*) As amount  
  From account 
  Join tab on tab.account_id = account.id 
  Group by account.id,  account.username 
  Order by amount desc 
  limit 3;"
  ~~~~
  
 
  
  
  
