CREATE DATABASE odd;
use odd;

CREATE TABLE mois_saison (
  mois VARCHAR(20),
  saison VARCHAR(10)
);

INSERT INTO mois_saison
  (mois, saison)
VALUES
  ('Aout', 'ete'),
  ('janvier', 'hiver');
