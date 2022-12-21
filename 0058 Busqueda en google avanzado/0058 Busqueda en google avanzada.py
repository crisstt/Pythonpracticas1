# programa para realizar busqueda a google avanzado
from googlesearch import search
#capturar busqueda
google_query= str(input('¡Porfavor!, introduce lo que desea buscar en google:\t'))
#metodo serch realizar las busquedas
#                                      Desde cero, cadacuanto,cuantos,detener
google_terms = []
google_terms_youtube= []

for i in search(google_query,tld = 'com.mx', start = 0, pause = 1, num = 10, stop = 20):
    print(i)
    google_terms.append(i)
    


for x in search(' "login form" youtube',tld = 'com.mx', start = 0, pause = 1, num = 10, stop = 20):
    print(x)
    google_terms_youtube.append(x)

# crear archivo y ponerlo modo escritura
archivo = open('google_search.txt', '+a', encoding = 'utf - 8')
archivo.write('\n Tu frase a buscar es: {} \n'. format(google_query))
for element in google_terms:
    archivo.write(element + '\n')

archivo_youtube = open('google_search_youtube.txt', '+a', encoding = 'utf - 8')
archivo_youtube.write('\n Tu frase a Buscar en Youtube es: {} \n'. format(google_query))
for element in google_terms_youtube:
    archivo_youtube.write(element + '\n')

archivo.close()
archivo_youtube.close()
