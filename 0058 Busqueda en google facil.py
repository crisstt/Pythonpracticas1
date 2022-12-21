# programa para realizar busqueda a google basico

from googlesearch import search

google_query= str(input('¡Porfavor!, introduce lo que desea buscar en google:\t'))

for i in search(google_query, start = 0, pause = 2, stop = 10):
    print(i)
