import csv
fichero = 'winequality.csv'
def read_data(fichero):
    dicc={}
    contador =1
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            
            print(row.index)

            dicc["dato"+ str(contador)]={
                'type' : row[0],
                'fixed acidity':row[1],
                'volatile acidity': row[2],
                'citric acid':row[3],
                'residual sugar': row[4],
                'chlorides': row[5],
                'free sulfur': row[6],
                'totl sulfur dioxide': row[7],
                'density': row[8],
                'PH': row[9],
                'sulphates': row[10],
                'alcohol':row[11],
                'quality':row[12]

            }
            contador+=1

    

read_data(fichero)