from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')

#Equipos

equiposHTML = soup.find_all('span', class_='nombre-equipo')
puntosHTML = soup.find_all('td', class_='destacado')

equiposNombres = list()
equiposPuntos = list()

count = 0

for i in range(0,len(equiposHTML)):
    if count < 20:
        equiposPuntos.append( puntosHTML[i].text )
        equiposNombres.append( equiposHTML[i].text )
    else:
        break
    count += 1

print(equiposPuntos)
print(equiposNombres)

#DATAFRAME

df = pd.DataFrame( {'Nombre': equiposNombres, 'Puntos': equiposPuntos}, index=list(range(1,21)) )
print(df)

#df.to_csv('Clasificacion.csv', index=False)

