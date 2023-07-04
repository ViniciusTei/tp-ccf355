-- TABLE
CREATE TABLE friend (
  user_iduser_1 INT NOT NULL,
  user_iduser_2 INT NOT NULL,
  start_date DATE NOT NULL, update_date DATE, status VARCHAR,
  PRIMARY KEY (user_iduser_1, user_iduser_2),
  CONSTRAINT fk_user_has_user_user1
    FOREIGN KEY (user_iduser_1)
    REFERENCES user (iduser)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_user_has_user_user2
    FOREIGN KEY (user_iduser_2)
    REFERENCES user (iduser)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
CREATE TABLE game (
  idgame INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(45) NOT NULL);
CREATE TABLE "lobby" (idlobby INTEGER PRIMARY KEY, name TEXT, game TEXT);
CREATE TABLE lobby_has_user (
  lobby_idlobby INTEGER NOT NULL,
  user_iduser INTEGER NOT NULL,
  PRIMARY KEY (lobby_idlobby, user_iduser),
  CONSTRAINT fk_lobby_has_user_lobby1
    FOREIGN KEY (lobby_idlobby)
    REFERENCES lobby (idlobby)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT fk_lobby_has_user_user1
    FOREIGN KEY (user_iduser)
    REFERENCES user (iduser)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);
CREATE TABLE `match` (
  idmatch INTEGER NOT NULL,
  start_date DATE NOT NULL,
  end_date DATE NULL,
  PRIMARY KEY (idmatch));
CREATE TABLE match_challenge 
(
	match_challenge_id INTEGER PRIMARY KEY,
  	match_id INTEGER NOT NULL,
  	lobby_requester INTEGER not NULL,
  	lobby_challenged INTEGER NOT NULL,
  	situation TEXT,
 	FOREIGN KEY (match_id) REFERENCES `match` (idmatch) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (lobby_requester) REFERENCES lobby (idlobby) ON DELETE CASCADE ON UPDATE CASCADE,
  	FOREIGN KEY (lobby_challenged)REFERENCES lobby (idlobby) ON DELETE CASCADE ON UPDATE CASCADE
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE user (
  iduser INTEGER PRIMARY KEY AUTOINCREMENT,
  username VARCHAR(45) NOT NULL,
  password VARCHAR(45) NOT NULL,
  image VARCHAR(45) NOT NULL DEFAULT 'default.png',
  UNIQUE (username));
 
-- INDEX
CREATE INDEX fk_lobby_has_user_lobby1_idx ON lobby_has_user (lobby_idlobby ASC);
CREATE INDEX fk_lobby_has_user_user1_idx ON lobby_has_user (user_iduser ASC);
CREATE INDEX fk_user_has_user_user1_idx ON friend (user_iduser_1 ASC);
CREATE INDEX fk_user_has_user_user2_idx ON friend (user_iduser_2 ASC);
 
-- TRIGGER
 
-- VIEW
 
