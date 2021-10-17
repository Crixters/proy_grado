from bs4 import BeautifulSoup
import requests
import re
import unidecode 

def get_admission_process_questions_answers(url, question):

    question = question.lower()
    question = unidecode.unidecode(question)
    question = re.sub(r'[^\w]', ' ', question)

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

#get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/nuevo-aspirante","proceso de inscripcion - admision aspirantes nuevos")
#get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-externa","proceso de inscripcion - admision aspirantes transferencia externa")
#get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-interna","proceso de inscripcion - admision aspirantes transferencia interna")
#get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/reingreso","proceso de inscripcion - admision aspirantes a reingreso")
#get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/posgrado/extranjero","proceso de inscripcion - admision aspirantes nacionales o extranjeros")