def tag_bloco(conteudo, *args, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_list(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))

    # parametro* (tuple) torna os parâmentros posicionais inválidos
    print(tag_bloco('classe e inline', 'info', True))

    print(tag_bloco(inline=False, classe='Error', conteudo='Falhou!'))

    # Exatamente o mesmo, porém 1 precisou chamar a função e o outro não
    print(tag_bloco(tag_list('Item 1', 'Item 2'), classe='info'))
    print(tag_bloco(tag_list, 'Item 1', 'Item 2', classe='info'))
