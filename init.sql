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

CREATE VIEW ViewVideos AS
SELECT id, video, km_ini, km_final
FROM Videos;

CREATE VIEW ViewRodovias AS
SELECT id, rodovia, km_ini, km_final
FROM Rodovias;

CREATE VIEW ViewResults AS
SELECT id, name, km, distance, highway, item
FROM Results;
