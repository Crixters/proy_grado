from bs4 import BeautifulSoup
import requests
import re 
import utils

def get_uac_tuition_prices_questions_answers():
    url_tuition_prices = "https://www.uac.edu.co/programas/valores-de-matricula"

    question_answers_array = []

    response = requests.get(url_tuition_prices)
    soup_object = BeautifulSoup(response.content,'html.parser')

    div_content_tables_prices = soup_object.find('div',{'class':'contentTablevaloresM'})

    prices_tables = div_content_tables_prices.find_all('table')

    for price_table in prices_tables:
        tbody = price_table.find('tbody',{'class':'intercaladas'})
        trs = tbody.find_all('tr')
        for tr in trs:
            question_answer = []
            first_td = tr.find('td',{'class':'first'})
            question = "valor de matricula "+first_td.get_text(strip=True).split("-")[0]
            question = utils.adapt_phrase_to_bot(question)

            first_td.extract()
            tds = tr.find_all('td')
            answer = ""
            for td in tds:
                answer = answer + td['data-label'] + " " + td.get_text(strip=True) + "\n"

            question_answer.append(question)
            question_answer.append(answer)
            question_answers_array.append(question_answer)

    return question_answers_array

def get_uac_programs_questions_answers(url, question):

    question = utils.adapt_phrase_to_bot(question)
    
    questions_answers_array = []
    question_answer = []

    answer = ""

    response = requests.get(url)
    soup_object = BeautifulSoup(response.content,'html.parser')
    
    div_programs = soup_object.find('div',{'class':'row programasEspecializaciones'})
    program_name_links = div_programs.find_all('a')

    for program_name_link in program_name_links:
        answer = answer + program_name_link.get_text(strip=True)+"\n"

    question_answer.append(question)
    question_answer.append(answer)
    questions_answers_array.append(question_answer)

    return questions_answers_array

#get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/pregrado","¿Cúales son los programas de pregrado de la universidad autónoma del caribe?")
#get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/especializaciones","¿Cúales son los programas de especializaciones de la universidad autónoma del caribe?")
#get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/maestrias","¿Cúales son los programas de maestria de la universidad autónoma del caribe?")

