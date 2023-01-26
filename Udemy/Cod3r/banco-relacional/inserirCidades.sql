INSERT INTO cidades (nome, area, estado_id)
VALUES ('Campinas', 795, 35)

INSERT INTO cidades (nome, area, estado_id)
VALUES ('Niterói', 133.9, 29)

INSERT INTO cidades 
    (nome, area, estado_id)
VALUES (
    'Caruaru',
    133.9,
    (SELECT id FROM estados WHERE sigla = 'PE')
)

INSERT INTO cidades 
    (nome, area, estado_id)
VALUES (
    'Juanzeiro do Norte',
    248.2,
    (SELECT id FROM estados WHERE sigla = 'CE')
)

SELECT * FROM cidades