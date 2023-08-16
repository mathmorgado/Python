import PySimpleGUI as sg


# Criando o layout
def criar_janela_inicial():
    sg.theme('DarkBlue4')
    linha = [
        [sg.Checkbox(''), sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tasks', layout=linha, key='container')],
        [sg.Button('add task'), sg.Button('Reset')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)


# Criar janela
window = criar_janela_inicial()

# Eventos
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

    elif event == 'add task':
        window.extend_layout(
            window['container'], [[sg.Checkbox(''), sg.Input('')]]
            )
    elif event == 'Reset':
        window.close()
        window = criar_janela_inicial()
