select * from estados

select 
    sigla, 
    nome as 'Nome dos Estados' 
from estados
where regiao = 'Sul'

select 
    nome, 
    regiao 
from estados
where populacao >= 10
order by populacao desc
