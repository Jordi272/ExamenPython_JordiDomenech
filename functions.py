import csv
fichero = 'winequality.csv'
def read_data(fichero):
    dicc={}
    contador =1
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])
            dicc["dato"+ str(contador)]={
                'type' : row[0],
                'fixed acidity':row[1],
                'volatile acidity': row[2],
                'residual sugar': row[3],
                'chlorides': row[4],
                'free sulfur'

            }
            contador+=1

    #print(dicc)

read_data(fichero)