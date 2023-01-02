from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Pt- br
setlocale(LC_ALL, 'pt_BR')

# Separados
indices_31 = filter(lambda mes: mdays[mes] if mdays[mes] == 31 else '', range(1, 13))
meses_nome = map(lambda mes: month_name[mes], indices_31)
meses_31 = reduce(lambda todos, nome_mes: f'{todos}\n- {nome_mes}', meses_nome, '\nMeses com 31 dias:')

print(meses_31)

# Juntos
print(
    reduce(
        lambda todos, nome_mes: f'{todos}\n- {nome_mes}',
        map(
            lambda mes: month_name[mes],
            filter(
                lambda mes: mdays[mes] if mdays[mes] == 31 else '', range(1, 13)
            )
        ), f'\nMeses com 31 dias:'
    )
)
