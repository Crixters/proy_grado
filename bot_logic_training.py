
import scraping_admissions
import scraping_calendars
import scraping_procedures_requests
import scraping_programs
import scraping_support
import scraping_ucil

admission_new_candidat_questions_answers = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/nuevo-aspirante","proceso de inscripcion - admision aspirantes nuevos")
admission_external_transfer_candidate_questions_answers = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-externa","proceso de inscripcion - admision aspirantes transferencia externa")
admission_internal_transfeR_candidate_questions_answers = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-interna","proceso de inscripcion - admision aspirantes transferencia interna")
admisions_re_admission_candidate_questions_answers = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/reingreso","proceso de inscripcion - admision aspirantes a reingreso")
admissions_foreign_candidates_questions_answers = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/posgrado/extranjero","proceso de inscripcion - admision aspirantes nacionales o extranjeros")

calendar_pregrado_01_questions_answers = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_pregrado_current_year_01)
calendar_pregrado_02_questions_answers = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_pregrado_current_year_02)
calendar_pregrado_next_year_01_questions_answers = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_pregrado_next_year_01)
calendar_posgrado_01_questions_answers = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_posgrado_current_year_01)
calendar_posgrado_02_questions_answers = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_posgrado_current_year_02)
calendar_postgrado_next_year_01_questions_answers = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_posgrado_next_year_01)

procedimiento_carga_adicional_questions_answers = scraping_procedures_requests.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/carga-adicional","procedimiento carga adicional")
procedimiento_examen_supletorio_questions_answers = scraping_procedures_requests.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/examen-supletorio","procedimiento examen supletorio")
procedimiento_congelamiento_devolucion_questions_answers = scraping_procedures_requests.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/congelamiento-y-devolucion","procedimiento congelamiento devolucion")
procedimiento_congelacion_carga_academica_questions_answers = scraping_procedures_requests.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/cancelacion-carga-academica","procedimiento congelacion de carga academica")
procedimiento_certificados_academicos_questions_answers = scraping_procedures_requests.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/certificados-academicos","procedimiento certificados academicos")

valores_matricula_questions_answers = scraping_programs.get_uac_tuition_prices_questions_answers()

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
          response(list2[i], list1[i].lower().split(" "))

    #Response-------------------------------------------------------------------------------------
    #response('del 01 de octubre del 2020 hasta el 22 de febrero 2021', ['fecha','inscripcion','ingreso', 'por', 'primera', 'vez'])

    createResponsesDependingScrapingData(admission_new_candidat_questions_answers[0], admission_new_candidat_questions_answers[1])
    createResponsesDependingScrapingData(admission_external_transfer_candidate_questions_answers[0], admission_external_transfer_candidate_questions_answers[1])
    createResponsesDependingScrapingData(admission_internal_transfeR_candidate_questions_answers[0], admission_internal_transfeR_candidate_questions_answers[1])
    createResponsesDependingScrapingData(admisions_re_admission_candidate_questions_answers[0], admisions_re_admission_candidate_questions_answers[1])
    createResponsesDependingScrapingData(calendar_pregrado_01_questions_answers[0], calendar_pregrado_01_questions_answers[1])
    createResponsesDependingScrapingData(calendar_pregrado_02_questions_answers[0], calendar_pregrado_02_questions_answers[1])
    createResponsesDependingScrapingData(calendar_pregrado_next_year_01_questions_answers[0], calendar_pregrado_next_year_01_questions_answers[1])
    createResponsesDependingScrapingData(calendar_posgrado_01_questions_answers[0], calendar_posgrado_01_questions_answers[1])
    createResponsesDependingScrapingData(calendar_posgrado_02_questions_answers[0], calendar_posgrado_02_questions_answers[1])
    createResponsesDependingScrapingData(calendar_postgrado_next_year_01_questions_answers[0], calendar_postgrado_next_year_01_questions_answers[1])
    createResponsesDependingScrapingData(procedimiento_carga_adicional_questions_answers[0], procedimiento_carga_adicional_questions_answers[1])
    createResponsesDependingScrapingData(procedimiento_examen_supletorio_questions_answers[0], procedimiento_examen_supletorio_questions_answers[1])
    createResponsesDependingScrapingData(procedimiento_congelamiento_devolucion_questions_answers[0], procedimiento_congelamiento_devolucion_questions_answers[1])
    createResponsesDependingScrapingData(procedimiento_congelacion_carga_academica_questions_answers[0], procedimiento_congelacion_carga_academica_questions_answers[1])
    createResponsesDependingScrapingData(procedimiento_certificados_academicos_questions_answers[0], procedimiento_certificados_academicos_questions_answers[1])
    createResponsesDependingScrapingData(valores_matricula_questions_answers[0], valores_matricula_questions_answers[1])



    best_match = max(highest_prob_list, key=highest_prob_list.get)
    
    

    return unknown() if highest_prob_list[best_match] < 1 else best_match
    

def get_response(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

#Testing the response system
while True:
    print('UAC-Bot: ' + get_response(input('Tú: ')))
