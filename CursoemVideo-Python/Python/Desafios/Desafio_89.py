lista = []
nome = []
notas = []

while True:
    print('\n', 15*'-=')
    nome.append(str(input('Nome: ')))
    notas.append(float(input('1º nota: ')))
    notas.append(float(input('2º nota: ')))

    nome.append(notas[:])
    lista.append(nome[:])

    notas.clear()
    nome.clear()

    resp = str(input('Deseja continuar[S/N]? '))
    print(15*'-=')
    if resp in 'Nn':
        break

print('\nNo.   Nome', 13 * ' ', 'MÉDIA')
print(33*'-')

for c, n in enumerate(lista):
    x = 18 - len(lista[c][0])
    print(f'{c}     {lista[c][0]}', x*' ', f'{sum(lista[c][1])/2:.1f}')

while True:
    aluno = int(input('\nMostrar as notas de qual aluno? (999 interrompe): '))
    print(f'As notas de {lista[aluno][0]} são {lista[aluno][1]}!')
    if aluno == 999:
        break
