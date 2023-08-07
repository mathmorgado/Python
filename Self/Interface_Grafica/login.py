import PySimpleGUI as sg

# Criar layout
sg.theme('Default1')
layout = [
    [sg.Text('Usuário'), sg.Input('', key='usuario')],
    [sg.Text('Senha'), sg.Input('', key='senha')],
    [sg.Checkbox('Lembrar login')],
    [sg.Button('Entrar')],
]

# Criar janela
janela = sg.Window('Tela de Login', layout=layout)

# Eventos
while True:
    evento, valores = janela.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == 'Entrar':
        if valores['usuario'] == 'Matt' and valores['senha'] == 'Teteu18':
            print('Passou no login!')
        else:
            print('Não passou no login')
