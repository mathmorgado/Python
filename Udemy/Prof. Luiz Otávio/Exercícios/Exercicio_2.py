while True:
    time = input('Digite o horário atual de acordo com o exemplo a seguir(22:45): ')
    cont = 0

    if ':' in time:
        time = time.split(':', 2)
        
        if time[0].isnumeric() and time[1].isnumeric():

            while True:
                if cont == 0:
                    pass
                else:
                    time = input('Digite o horário atual de acordo com o exemplo a seguir(22:45): ')

                if int(time[0]) > 12 and int(time[0]) < 18:
                    print(f'Boa tarde {time[0]}:{time[1]}')
                    break

                elif int(time[0]) <= 12:
                    print(f'Bom dia {time[0]}:{time[1]}')
                    break

                elif int(time[0]) >= 18 and int(time[0])  < 24:
                    print(f'Boa noite {time[0]}:{time[1]}')
                    break
                
                else:
                    print('ERROR: O horario escolhido é inválido!')
                    cont += 1

        else:
            print('ERROR: Por favor, digite um horário válido!')
        
        break
        
    else:
        print('ERROR: Por favor, utilize o modelo exibido!')

