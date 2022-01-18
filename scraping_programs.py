from bs4 import BeautifulSoup
import requests
import re
import utils


def get_uac_tuition_prices_questions_answers():
    url_tuition_prices = "https://www.uac.edu.co/programas/valores-de-matricula"

    question_answers_array = []

    response = requests.get(url_tuition_prices)
    soup_object = BeautifulSoup(response.content, 'html.parser')

    div_content_tables_prices = soup_object.find(
        'div', {'class': 'contentTablevaloresM'})

    prices_tables = div_content_tables_prices.find_all('table')

    for price_table in prices_tables:
        tbody = price_table.find('tbody', {'class': 'intercaladas'})
        trs = tbody.find_all('tr')
        for tr in trs:
            questions_answer = []
            questions = []
            first_td = tr.find('td', {'class': 'first'})
            first_td.extract()
            tds = tr.find_all('td')
            answer = ""
            for td in tds:
                answer = answer + td['data-label'] + \
                    " " + td.get_text(strip=True) + "\n"

            questions.append(utils.adapt_phrase_to_bot(
                "valor de matricula "+first_td.get_text(strip=True).split("-")[0]))
            questions.append(utils.adapt_phrase_to_bot(
                "costo de matricula "+first_td.get_text(strip=True).split("-")[0]))
            questions.append(utils.adapt_phrase_to_bot(
                "precio de matricula "+first_td.get_text(strip=True).split("-")[0]))
            questions.append(utils.adapt_phrase_to_bot(
                "monto de matricula "+first_td.get_text(strip=True).split("-")[0]))
            questions.append(utils.adapt_phrase_to_bot(
                "suma total costo de matricula "+first_td.get_text(strip=True).split("-")[0]))
            questions_answer.append(
                "• Costo de matrícula "+first_td.get_text(strip=True).split("-")[0]+":\n\n" + answer)
            question_answers_array.append(questions_answer)

    return question_answers_array


def get_uac_programs_questions_answers(url, question):

    questions_answers_array = []
    questions_answer = []
    questions = []

    answer = ""

    response = requests.get(url)
    soup_object = BeautifulSoup(response.content, 'html.parser')

    div_programs = soup_object.find(
        'div', {'class': 'row programasEspecializaciones'})
    program_name_links = div_programs.find_all('a')

    for program_name_link in program_name_links:
        answer = answer + program_name_link.get_text(strip=True)+"\n\n"

    questions.append(utils.adapt_phrase_to_bot(question))
    questions.append(utils.adapt_phrase_to_bot("lista total de programas"))
    questions.append(utils.adapt_phrase_to_bot("cuales son los "+question))
    questions.append(utils.adapt_phrase_to_bot("lista de "+question))
    questions.append(utils.adapt_phrase_to_bot("lista "+question))
    questions.append(utils.adapt_phrase_to_bot("lista de todos los "+question))
    questions_answer.append(questions)
    questions_answer.append("• "+question+":\n"+answer)
    questions_answers_array.append(questions_answer)

    return questions_answers_array

#get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/pregrado","¿Cúales son los programas de pregrado de la universidad autónoma del caribe?")
#get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/especializaciones","¿Cúales son los programas de especializaciones de la universidad autónoma del caribe?")
#get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/maestrias","¿Cúales son los programas de maestria de la universidad autónoma del caribe?")
