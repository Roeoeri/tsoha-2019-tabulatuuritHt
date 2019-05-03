# Tietokantakaavio <h1>

![Tietokantakaavio](https://github.com/Roeoeri/tsoha-2019-tabulatuuritHt/blob/master/documentation/tietokantakaavio_hahmotelma.png)

## Create table-lauseet <h2>
~~~~sql
CREATE TABLE account (
        id INTEGER NOT NULL, 
        username VARCHAR(255) NOT NULL, 
        password VARCHAR(255) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (username)
);
CREATE TABLE role (
        id INTEGER NOT NULL, 
        name VARCHAR(80) NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (name)
);
CREATE TABLE genre (
        id INTEGER NOT NULL, 
        genre VARCHAR(150) NOT NULL, 
        PRIMARY KEY (id)
);
CREATE TABLE roles_users (
        user_id INTEGER, 
        role_id INTEGER, 
        FOREIGN KEY(user_id) REFERENCES account (id), 
        FOREIGN KEY(role_id) REFERENCES role (id)
);
CREATE TABLE tab (
        id INTEGER NOT NULL, 
        name VARCHAR(150) NOT NULL, 
        content VARCHAR(12000) NOT NULL, 
        account_id INTEGER NOT NULL, 
        PRIMARY KEY (id), 
        FOREIGN KEY(account_id) REFERENCES account (id)
);
CREATE TABLE genre_tab (
        genre_id INTEGER NOT NULL, 
        tab_id INTEGER NOT NULL, 
        PRIMARY KEY (genre_id, tab_id), 
        FOREIGN KEY(genre_id) REFERENCES genre (id), 
        FOREIGN KEY(tab_id) REFERENCES tab (id)
  ~~~~
  


