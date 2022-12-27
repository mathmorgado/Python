def tag(tag, *args, **kargs):
    atributos = str(kargs.values())[14:-3]
    conteudo = str(args)[2:-3]

    if atributos != '':
        return f'<{tag} class="{atributos}">{conteudo}</{tag}>'
    else:
        return f'<{tag} >{conteudo}</{tag}>'


if __name__ == '__main__':
    print(tag('p',
                tag('span', 'Curso de Python 3, por '),
                tag('strong', 'Juracy Filho', id='jf'),
                tag('span', 'e'),
                tag('strong', 'Leonardo Leitão', id='ll'),
                tag('span', '.'),
                html_class='alert'))
