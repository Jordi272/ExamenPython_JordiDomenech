import csv
fichero = 'winequality.csv'
def read_data(fichero):
    dicc={}
    contador =1
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            dicc["dato" + str(contador)]= row
            contador +=1
            print(row)

read_data(fichero)