from bs4 import BeautifulSoup
import pandas as pd
import requests
from datetime import date 

urlsCalendarioPregrado = [
    f"https://www.uac.edu.co/calendario-academico/pregrado-{date.today().year}01",
    f"https://www.uac.edu.co/calendario-academico/pregrado-{date.today().year}02",
]

urlsCalendarioPosgrado = [
    f"https://www.uac.edu.co/calendario-academico/posgrado-{date.today().year}01",
    f"https://www.uac.edu.co/calendario-academico/posgrado-{date.today().year}02"
]

pageCalendarioPregrado01 = requests.get(urlsCalendarioPregrado[0])
#pageCalendarioPregrado02 = requests.get(urlsCalendarioPregrado[1])
#pageCalendarioPosgrado01 = requests.get(urlsCalendarioPosgrado[0])
#pageCalendarioPosgrado02 = requests.get(urlsCalendarioPosgrado[1])

soupPregrado01 = BeautifulSoup(pageCalendarioPregrado01.content,'html.parser')
#soupPregrado02 = BeautifulSoup(pageCalendarioPregrado02.content,'html.parser')
#soupPosgrado01 = BeautifulSoup(pageCalendarioPosgrado01.content,'html.parser')
#soupPosgrado02 = BeautifulSoup(pageCalendarioPosgrado02.content,'html.parser')

calendarioPregrado01RegistrosHTML = soupPregrado01.find_all('td')
#calendarioPregrado02RegistrosHTML = soupPregrado02.find_all('td')
#calendarioPosgrado01RegistrosHTML = soupPosgrado01.find_all('td')
#calendarioPosgrado02RegistrosHTML = soupPosgrado02.find_all('td')

especificacionesCalendarioPregrado01 = list()
fechasEjecucionCalendarioPregrado01 = list()

for i in range(0,len(calendarioPregrado01RegistrosHTML)):
    if(i % 2 == 0):
        especificacionesCalendarioPregrado01.append( calendarioPregrado01RegistrosHTML[i].text.lower() )
    else:
        fechasEjecucionCalendarioPregrado01.append( calendarioPregrado01RegistrosHTML[i].text.lower() )

#especificacionesCalendarioPregrado02 = list()
#fechasEjecucionCalendarioPregrado02 = list()

#count = 0

#for i in range(0,len(calendarioPregrado02RegistrosHTML)):
#    if "ciclo" in calendarioPregrado02RegistrosHTML[i].text.lower():
#       break
#    if(count % 2 == 0):
#        especificacionesCalendarioPregrado02.append( calendarioPregrado02RegistrosHTML[i].text )
#    else:
#        fechasEjecucionCalendarioPregrado02.append( calendarioPregrado02RegistrosHTML[i].text )
#    count += 1

#if( len(fechasEjecucionCalendarioPregrado02) != len(especificacionesCalendarioPregrado02) ):
#    diferencia = abs( len(fechasEjecucionCalendarioPregrado02) - len(especificacionesCalendarioPregrado02) )
#    for i in range(0,diferencia):
#        if(len(fechasEjecucionCalendarioPregrado02) > len(especificacionesCalendarioPregrado02)):
#            especificacionesCalendarioPregrado02.append("")
#        else:
#            fechasEjecucionCalendarioPregrado02.append("")


#especificacionesCalendarioPosgrado01 = list()
#fechasEjecucionCalendarioPosgrado01 = list()

#count = 0

#for i in range(0,len(calendarioPosgrado01RegistrosHTML)):
#    if(count % 2 == 0):
#        especificacionesCalendarioPosgrado01.append( calendarioPosgrado01RegistrosHTML[i].text )
#    else:
#        fechasEjecucionCalendarioPosgrado01.append( calendarioPosgrado01RegistrosHTML[i].text )
#    count += 1

#especificacionesCalendarioPosgrado02 = list()
#fechasEjecucionCalendarioPosgrado02 = list()

#count = 0

#for i in range(0,len(calendarioPosgrado02RegistrosHTML)):
#    if(count % 2 == 0):
#        especificacionesCalendarioPosgrado02.append( calendarioPosgrado02RegistrosHTML[i].text )
#    else:
#        fechasEjecucionCalendarioPosgrado02.append( calendarioPosgrado02RegistrosHTML[i].text )
#    count += 1

#dfCalendarioPregrado01 = pd.DataFrame( {'Especificacion': especificacionesCalendarioPregrado01, 'Fechas de Ejecucion': fechasEjecucionCalendarioPregrado01}, index=list(range(1,len(especificacionesCalendarioPregrado01)+1)) ) 
#dfCalendarioPregrado02 = pd.DataFrame( {'Especificacion': especificacionesCalendarioPregrado02, 'Fechas de Ejecucion': fechasEjecucionCalendarioPregrado02}, index=list(range(1,len(especificacionesCalendarioPregrado02)+1)) ) 
#dfCalendarioPosgrado01 = pd.DataFrame( {'Especificacion': especificacionesCalendarioPosgrado01, 'Fechas de Ejecucion': fechasEjecucionCalendarioPosgrado01}, index=list(range(1,len(especificacionesCalendarioPosgrado01)+1)) ) 
#dfCalendarioPosgrado02 = pd.DataFrame( {'Especificacion': especificacionesCalendarioPosgrado02, 'Fechas de Ejecucion': fechasEjecucionCalendarioPosgrado02}, index=list(range(1,len(especificacionesCalendarioPosgrado02)+1)) ) 

#print(dfCalendarioPregrado01)
#print(dfCalendarioPregrado02)
#print(dfCalendarioPosgrado01)
#print(dfCalendarioPosgrado02)


# AQUI EMPIEZA LA CREACIÓN DEL BOT 

import re
import random


def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True 

    #Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    #Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float( len(recognised_words) )

    #Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break
    
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0


def unknown():
    response = [ '¿Podrías repetirlo?',
    "...", "No entiendo bien", "¿Qué significa eso?" ][random.randrange(4)]
    return response


def check_all_messages(message):
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    def createResponsesDependingScrapingData(list1, list2):
        for i in range(0, len(list1) ):
          response(list2[i], list1[i].split(" "))

    #Response-------------------------------------------------------------------------------------
    #response('del 01 de octubre del 2020 hasta el 22 de febrero 2021', ['fecha','inscripcion','ingreso', 'por', 'primera', 'vez'])


    createResponsesDependingScrapingData(especificacionesCalendarioPregrado01, fechasEjecucionCalendarioPregrado01)

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    

    return unknown() if highest_prob_list[best_match] < 1 else best_match
    

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
while True:
    print('UAC-Bot: ' + get_response(input('Tú: ')))