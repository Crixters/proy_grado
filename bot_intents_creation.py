
import scraping_admissions
import scraping_calendars
import scraping_procedures
import scraping_programs
import scraping_support
import json

def create_intents(questions_answers_array, objeto):
    
    for question_answer in questions_answers_array:
        otro_objeto = {}
        otro_objeto["tag"] = question_answer[0]
        otro_objeto["patterns"] = [question_answer[0]]
        otro_objeto["responses"] = [question_answer[1]]
        otro_objeto["context_set"] = ""
        objeto["intents"].append(otro_objeto)

def create_all_intents_and_save():

    intents_object = {}
    intents_object["intents"] = []

    admission_new_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/nuevo-aspirante","proceso de inscripcion - admision estudiante aspirante nuevo")
    admission_external_transfer_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-externa","proceso de inscripcion - admision estudiante aspirante transferencia externa")
    admission_internal_transfer_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-interna","proceso de inscripcion - admision estudiante aspirante transferencia interna")
    admission_reentry_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/pregrado/reingreso","proceso de inscripcion - admision estudiante aspirante a reingreso")
    admission_foreign_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers("https://www.uac.edu.co/admisiones-y-registro/posgrado/extranjero","proceso de inscripcion - admision estudiante extranjero aspirante nacional con estudio fuera del país")
    pregrado_current_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_pregrado_current_year_01)
    pregrado_current_year_02_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_pregrado_current_year_02)
    posgrado_current_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_posgrado_current_year_01)
    posgrado_current_year_02_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_posgrado_current_year_02)
    pregrado_next_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_pregrado_next_year_01)
    posgrado_next_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(scraping_calendars.url_posgrado_next_year_01)
    procedure_additional_charge_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/carga-adicional","procedimiento carga adicional")
    procedure_supplemental_exam_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/examen-supletorio","procedimiento examen supletorio")
    procedure_freezing_refund_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/congelamiento-y-devolucion","procedimiento congelamiento devolucion")
    procedure_cancellation_academic_charge_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/cancelacion-carga-academica","procedimiento cancelacion de carga academica")
    procedure_academic_certificates_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers("https://www.uac.edu.co/admisiones-y-registro/registro-y-control/certificados-academicos","procedimiento certificado academico")
    programs_pregrado_questions_answers_array = scraping_programs.get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/pregrado","programa de pregrado")
    programs_specializations_questions_answers_array = scraping_programs.get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/especializaciones","programa de especializacion")
    programs_masteries_questions_answers_array = scraping_programs.get_uac_programs_questions_answers("https://www.uac.edu.co/oferta-academica/maestrias","programa de maestria")
    tuition_prices_questions_answers_array = scraping_programs.get_uac_tuition_prices_questions_answers()
    support_questions_answers_array = scraping_support.get_support_questions_answers()

    create_intents(admission_new_applicant_questions_answers_array, intents_object)
    create_intents(admission_external_transfer_applicant_questions_answers_array, intents_object)
    create_intents(admission_internal_transfer_applicant_questions_answers_array, intents_object)
    create_intents(admission_reentry_applicant_questions_answers_array, intents_object)
    create_intents(admission_foreign_applicant_questions_answers_array, intents_object)
    create_intents(pregrado_current_year_01_questions_answers_array, intents_object)
    create_intents(pregrado_current_year_02_questions_answers_array, intents_object)
    create_intents(posgrado_current_year_01_questions_answers_array, intents_object)
    create_intents(posgrado_current_year_02_questions_answers_array, intents_object)
    create_intents(pregrado_next_year_01_questions_answers_array, intents_object)
    create_intents(posgrado_next_year_01_questions_answers_array, intents_object)
    create_intents(procedure_academic_certificates_questions_answers_array, intents_object)
    create_intents(procedure_additional_charge_questions_answers_array, intents_object)
    create_intents(procedure_cancellation_academic_charge_questions_answers_array, intents_object)
    create_intents(procedure_freezing_refund_questions_answers_array, intents_object)
    create_intents(procedure_supplemental_exam_questions_answers_array, intents_object)
    create_intents(programs_masteries_questions_answers_array, intents_object)
    create_intents(programs_pregrado_questions_answers_array, intents_object)
    create_intents(programs_specializations_questions_answers_array, intents_object)
    create_intents(tuition_prices_questions_answers_array, intents_object)
    create_intents(support_questions_answers_array, intents_object)

    with open('intents.json','w') as fp:
        json.dump(intents_object,fp,indent=4)