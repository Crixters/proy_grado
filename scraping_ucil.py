from bs4 import BeautifulSoup
import requests

url_validation_exams = "https://www.uac.edu.co/ucil/examenes-validacion"
url_ucil_special_leveling_plan_inscriptions = "https://www.uac.edu.co/ucil/plan-especial-de-nivelacion-para-coterminales-y-graduacion-oportuna/inscripciones-cursos-especiales"
url_ucil_special_courses_inscriptions = "https://www.uac.edu.co/ucil/cursos-especiales/inscripciones"
url_ucil_reversals_process = "https://www.uac.edu.co/ucil/proceso-de-reversiones"

def get_ucil_processes_questions_answers(url):

    questions_answers_array = []

    response = requests.get(url)
    soup_object = BeautifulSoup(response.content,'html.parser')

    question = "ucil "+soup_object.find('h2',{"class":"tituloInscripcionesUcil"}).get_text().strip()
    answer = ""

    processStepsPanels = soup_object.find_all('div',{"class":"panel panel-default panelUcil"})
    for processStepPanel in processStepsPanels:
        stepName = "• "+processStepPanel.find("div",{"class":"panel-heading"}).get_text().strip()+":"
        answer = answer+stepName+"\n\n"
        table = processStepPanel.find("div",{"class":"panel-body"}).find("table")
        if table:
            table.decompose()
      
        panelBody = processStepPanel.find("div",{"class":"panel-body"}).get_text().strip()
        answer = answer+panelBody+"\n\n"

    questions_answers_array.append(question)
    questions_answers_array.append(answer)
 
    return questions_answers_array 

get_ucil_processes_questions_answers(url_ucil_reversals_process)