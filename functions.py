import csv


def read_data(fichero):
    dicc={}
    contador =1
    with open(fichero, 'r') as file:
        reader = csv.reader(file)
        for elemento in reader:
            if '' in elemento:
                contador = contador
            else:
                dicc["dato"+ str(contador)]={
                    'type' : elemento[0],
                    'fixed acidity':elemento[1],
                    'volatile acidity': elemento[2],
                    'citric acid':elemento[3],
                    'residual sugar': elemento[4],
                    'chlorides': elemento[5],
                    'free sulfur': elemento[6],
                    'totl sulfur dioxide': elemento[7],
                    'density': elemento[8],
                    'PH': elemento[9],
                    'sulphates': elemento[10],
                    'alcohol':elemento[11],
                    'quality':elemento[12]

                    }
                contador+=1
    if len(dicc) > 10:
        return dicc
    else:
        return ValueError("El diccionario tiene menos de 10 muestras")
    
def split(dicc):
    diccWhite = {}
    diccRed = {}
    contadorWhite = 1
    contadorRed = 1
    for elemento in dicc.values():
        x = elemento['type']
        if x == "white":      
            diccWhite["dato"+ str(contadorWhite)]={
                    'fixed acidity':elemento['fixed acidity'],
                    'volatile acidity': elemento['volatile acidity'],
                    'citric acid':elemento['citric acid'],
                    'residual sugar': elemento['residual sugar'],
                    'chlorides': elemento['chlorides'],
                    'free sulfur': elemento['free sulfur'],
                    'totl sulfur dioxide': elemento['totl sulfur dioxide'],
                    'density': elemento['density'],
                    'PH': elemento['PH'],
                    'sulphates': elemento['sulphates'],
                    'alcohol':elemento['alcohol'],
                    'quality':elemento['quality']
                }
            contadorWhite+=1
        else:
            diccRed["dato"+ str(contadorRed)]={
                    'fixed acidity':elemento['fixed acidity'],
                    'volatile acidity': elemento['volatile acidity'],
                    'citric acid':elemento['citric acid'],
                    'residual sugar': elemento['residual sugar'],
                    'chlorides': elemento['chlorides'],
                    'free sulfur': elemento['free sulfur'],
                    'totl sulfur dioxide': elemento['totl sulfur dioxide'],
                    'density': elemento['density'],
                    'PH': elemento['PH'],
                    'sulphates': elemento['sulphates'],
                    'alcohol':elemento['alcohol'],
                    'quality':elemento['quality']
                }
            contadorRed+=1
    return(diccWhite, diccRed)

def reduce(dicc, nombreAtriburto):
    lista = []
    for diccionario in dicc.values():

        lista.append(diccionario[nombreAtriburto]) 


    return lista

def silhouette(lista1, lista2):
    #for lis in range(len(lista1)):
       # Si = lista2[]
    return 





    


        
        




   
