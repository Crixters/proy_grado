from bs4 import BeautifulSoup
from datetime import date
import requests
import unidecode 
import re 

url_pregrado_current_year_01 = f"https://www.uac.edu.co/calendario-academico/pregrado-{date.today().year}01"
url_pregrado_current_year_02 = f"https://www.uac.edu.co/calendario-academico/pregrado-{date.today().year}02"
url_pregrado_next_year_01 = f"https://www.uac.edu.co/calendario-academico/pregrado-{date.today().year+1}01"
url_posgrado_current_year_01 = f"https://www.uac.edu.co/calendario-academico/posgrado-{date.today().year}01"
url_posgrado_current_year_02 = f"https://www.uac.edu.co/calendario-academico/posgrado-{date.today().year}02"
url_posgrado_next_year_01 = f"https://www.uac.edu.co/calendario-academico/posgrado-{date.today().year+1}01"

def get_academic_calendar_questions_answers(url_calendar):
    response = requests.get(url_calendar)
    soup_object = BeautifulSoup(response.content,'html.parser')
    calendar_tables = soup_object.find_all('table',{'class':'tabla-calendario'})
    questions_answers_array = []
    studies_type_and_calendar_period = url_calendar.split("/")[-1]
    studies_type = studies_type_and_calendar_period.split("-")[0]
    calendar_period = studies_type_and_calendar_period.split("-")[1]

    for table in calendar_tables:
        if not "tic" in table.find('th').get_text().lower():
            table_registers = table.find_all('tr')
            for table_register in table_registers:
               tables_d = table_register.find_all('td')
               if len(tables_d) == 2:
                    question_answer = []

                    question = "fecha "+tables_d[0].get_text().strip() + " "+studies_type+" "+calendar_period+" "+calendar_period[:-2]+" "+calendar_period[-2:]
                    question = question.lower()
                    question = unidecode.unidecode(question)
                    question = re.sub(r'[^\w]', ' ', question)

                    answer = tables_d[1].get_text().strip()

                    question_answer.append(question)
                    question_answer.append(answer) 
                    questions_answers_array.append(question_answer)

    return questions_answers_array

#get_academic_calendar_questions_answers(url_pregrado_current_year_02)







    