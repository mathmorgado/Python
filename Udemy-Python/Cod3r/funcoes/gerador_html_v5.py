bloco_atrs = ('bloco_acesseskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')


def filtrar_atrs(informados, suportados):
    return ' '.join(f'{k.split("_")[-1]}="{v}"'
                    for k, v in informados.items() if k in suportados)


def tag_bloco(conteudo, *args, classe='success', inline=False, **novos_atrs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) \
        else conteudo(*args, **novos_atrs)
    atributos = filtrar_atrs(novos_atrs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


def tag_list(*itens, **novos_atrs):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {filtrar_atrs(novos_atrs,ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('classe e inline', 'info', True))
    print(tag_bloco(inline=False, classe='Error', conteudo='Falhou!'))
    print(tag_bloco(tag_list, 'Item 1', 'Item 2', classe='info'))
    print(tag_bloco(tag_list, 'Item 1', 'Item 2', classe='info',
                    bloco_acesseskey='m', bloco_id='conteudo',
                    ul_style='color:red', ul_blabla='NÃO "SUPORTADO"'))
