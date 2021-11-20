from bs4 import BeautifulSoup
import requests
import re
import utils

def get_procedures_requests_questions_answers(url, question):

    question = question.lower()
    question = utils.adapt_phrase_to_bot(question)

    response = requests.get(url)
    soup_object = BeautifulSoup(response.content,'html.parser')
    questions_answers_array = []
    question_answer = []
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
    
    question_answer.append(question)
    question_answer.append(answer)
    questions_answers_array.append(question_answer)

    return questions_answers_array

#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/carga-adicional","procedimiento carga adicional")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/examen-supletorio","procedimiento examen supletorio")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/congelamiento-y-devolucion","procedimiento congelamiento devolucion")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/cancelacion-carga-academica","procedimiento cancelacion de carga academica")
#get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/certificados-academicos","procedimiento certificados academicos")