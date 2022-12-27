def tag_bloco(conteudo, classe='success', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{conteudo}</{tag}>'


def tag_list(*itens):
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco('bloco'))
    print(tag_bloco('classe e inline', 'info', True))
    print(tag_bloco(inline=False, classe='Error', conteudo='Falhou!'))
    print(tag_bloco(tag_list('Item 1', 'Item 2'), classe='info'))
