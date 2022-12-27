from random import randint


def sortear_numero():
    return randint(1, 7)


for dado in range(1, 7):
    if dado % 2 == 1:
        continue

    if dado == sortear_numero():
        print('Acertou', dado)
        break

else:
    print('Errou rude! Errou feiio!')
# for i in range(1, 11):
#    if i == 6:
#        break
#    print(i)
# else:
#    print('Fim!')
