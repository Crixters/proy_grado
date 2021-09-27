from bs4 import BeautifulSoup
import requests
import re

def get_procedures_requests_questions_answers(url, question):

    response = requests.get(url)
    soup_object = BeautifulSoup(response.content,'html.parser')
    questions_answers_array = []
    questions = []
    answers = []
    answer = ""

    steps_divs = soup_object.find_all('div',{'class':'content_pasos_texto'})
    
    for step_div in steps_divs:
        line_div = step_div.find('div',{'class':'content_pasos_line'})
        step_title_div = step_div.find('div',{'class':'titlle_texto_pasos'})
        step_title =    "• " + step_title_div.get_text(strip=True)
        step_title_div.extract()
        line_div.extract()
        step_description = re.sub(r'\n\s*\n', r'\n\n', step_div.find('div').get_text().strip(), flags=re.M).replace("  ","")
        answer = answer + step_title + "\n\n" + step_description + "\n\n"

    questions.append(question)
    answers.append(answer)
    questions_answers_array.append(questions)
    questions_answers_array.append(answers)

    return questions_answers_array

#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/carga-adicional","procedimiento carga adicional")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/examen-supletorio","procedimiento examen supletorio")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/congelamiento-y-devolucion","procedimiento congelamiento devolucion")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/cancelacion-carga-academica","procedimiento congelacion de carga academica")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/certificados-academicos","procedimiento certificados academicos")