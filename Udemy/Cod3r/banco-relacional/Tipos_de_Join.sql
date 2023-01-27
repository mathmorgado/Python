select * from cidades;
select * from prefeitos;

-- Inner join: pega a intersecção de duas tabelas.
select * from cidades c inner join prefeitos p on c.id = p.cidade_id;

-- Left join: pega a intersecção e o outer (externo) da tabela à 'esquerda'.
select * from cidades c left join prefeitos p on c.id = p.cidade_id;

-- Right join: pega a intersecção e o outer da tabela à 'direita'.
select * from cidades c right join prefeitos p on c.id = p.cidade_id;

--Full join: Pega tanto a intersecção quanto os outer de ambas as tabelas. (Não suportado pelo SQL)
-- select * from cidades c full join prefeitos p on c.id = p.cidade_id; /Alternativa -> Usar union no right e left join
select * from cidades c left join prefeitos p on c.id = p.cidade_id
union
select * from cidades c right join prefeitos p on c.id = p.cidade_id;