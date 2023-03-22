from functions import read_data, split, reduce, silhouette

fichero = 'winequality.csv'
l =read_data(fichero)
#print(l)

split_llamada, split_llamada2 = split(l)
#print(split_llamada2)
llamada = reduce(split_llamada2, 'alcohol')
print(llamada)
llamada_2 = reduce(split_llamada2, 'quality')
print(llamada_2)

llamada_silhouette = silhouette(llamada, llamada_2)



