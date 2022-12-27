import csv

with open('pessoas.csv') as entrada:
    for pessoa in csv.reander(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))
