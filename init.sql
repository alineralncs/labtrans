CREATE TABLE Videos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  video TEXT UNIQUE,
  km_ini REAL,
  km_final REAL
);

CREATE TABLE Rodovias (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  rodovia INTEGER UNIQUE,
  km_ini REAL,
  km_final REAL
);

CREATE TABLE Results (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  km REAL,
  distance REAL,
  highway INTEGER,
  item TEXT
);
