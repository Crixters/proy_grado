
import scraping_admissions
import scraping_calendars
import scraping_procedures
import scraping_programs
import scraping_support
import json


def create_intents(questions_answers_array, objeto):

    for questions_answer in questions_answers_array:
        questions = questions_answer[0]
        otro_objeto = {}
        otro_objeto["tag"] = questions_answer[0][0]
        otro_objeto["patterns"] = []
        otro_objeto["responses"] = [questions_answer[1]]
        otro_objeto["context_set"] = ""
        for question in questions:
            otro_objeto["patterns"].append(question)
        objeto["intents"].append(otro_objeto)


def create_all_intents_and_save():

    intents_object = {}
    intents_object["intents"] = []

    admission_new_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/pregrado/nuevo-aspirante", ["procedimiento de inscripcion  estudiante nuevo", "proceso de inscripcion  estudiante nuevo", "procedimiento de admisión  estudiante nuevo", "proceso de admisión  estudiante nuevo", "procedimiento de inscripcion  aspirante nuevo", "proceso de inscripción  aspirante nuevo", "procedimiento de admisión  aspirante nuevo", "proceso de admisión  aspirante nuevo", "proceso entrada o inscripción aspirante nuevo", "proceso entrada o inscripción estudiante nuevo",       "procedimiento de inscripcion", "proceso de inscripcion", "procedimiento de admisión", "proceso de admisión", "procedimiento de inscripcion", "proceso de inscripción", "procedimiento de admisión", "proceso de admisión", "proceso entrada o inscripción", "proceso entrada o inscripción"])
    admission_external_transfer_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-externa", ["procedimiento de inscripcion  estudiante transferencia externa", "proceso de inscripcion  estudiante transferencia externa", "procedimiento de admisión  estudiante transferencia externa", "proceso de admisión  estudiante transferencia externa", "procedimiento de inscripcion  aspirante transferencia externa", "proceso de inscripción aspirante  transferencia externa", "procedimiento de admisión  aspirante transferencia externa", "proceso de admisión  aspirante transferencia externa", "quiero como es proceso entrada  aspirante transferencia externa"])
    admission_internal_transfer_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/pregrado/aspirante-transferencia-interna", ["procedimiento de inscripcion  estudiante transferencia interna", "proceso de inscripcion  estudiante transferencia interna", "procedimiento de admisión  estudiante transferencia interna", "proceso de admisión  estudiante transferencia interna", "procedimiento de inscripcion  aspirante transferencia interna", "proceso de inscripción  aspirante transferencia interna", "procedimiento de admisión  aspirante transferencia interna", "proceso de admisión  aspirante transferencia interna", "quiero como es proceso entrada  aspirante transferencia interna"])
    admission_reentry_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/pregrado/reingreso", ["procedimiento de inscripcion  estudiante reingreso", "proceso de inscripcion  estudiante reingreso", "procedimiento de admisión  estudiante reingreso", "proceso de admisión  estudiante reingreso", "procedimiento de inscripcion  aspirante reingreso", "proceso de inscripción  aspirante reingreso", "procedimiento de admisión  aspirante reingreso", "proceso de admisión  aspirante reingreso", "quiero como es proceso entrada  aspirante reingreso"])
    admission_foreign_applicant_questions_answers_array = scraping_admissions.get_admission_process_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/posgrado/extranjero", ["procedimiento de inscripcion  estudiante extranjero", "proceso de inscripcion  estudiante extranjero", "procedimiento de admisión  estudiante extranjero", "proceso de admisión  estudiante extranjero", "procedimiento de inscripcion  aspirante extranjero", "proceso de inscripción  aspirante extranjero", "procedimiento de admisión  aspirante extranjero", "proceso de admisión  aspirante extranjero", "quiero como es proceso entrada  aspirante extranjero"])
    pregrado_current_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(
        scraping_calendars.url_pregrado_current_year_01)
    pregrado_current_year_02_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(
        scraping_calendars.url_pregrado_current_year_02)
    posgrado_current_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(
        scraping_calendars.url_posgrado_current_year_01)
    posgrado_current_year_02_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(
        scraping_calendars.url_posgrado_current_year_02)
    pregrado_next_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(
        scraping_calendars.url_pregrado_next_year_01)
    posgrado_next_year_01_questions_answers_array = scraping_calendars.get_academic_calendar_questions_answers(
        scraping_calendars.url_posgrado_next_year_01)
    procedure_additional_charge_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/registro-y-control/carga-adicional", ["procedimiento radicar carga adicional", "proceso radicar carga adicional", "trámite radicar carga adicional"])
    procedure_supplemental_exam_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/registro-y-control/examen-supletorio", ["procedimiento examen evaluacion supletorio materia asignatura", "proceso examen evaluacion supletorio materia asignatura", "trámite examen evaluacion supletorio materia asignatura", "procedimiento examen evaluacion diferido", "proceso examen evaluacion diferido materia asignatura", "trámite examen evaluacion diferido materia asignatura", "procedimiento examen evaluacion diferido materia asignatura", "proceso examen evaluacion diferido", "trámite examen evaluacion diferido", "procedimiento examen evaluacion habilitacion materia asignatura", "proceso examen evaluacion habilitacion materia asignatura", "trámite examen evaluacion habilitacion materia asignatura"])
    procedure_freezing_refund_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/registro-y-control/congelamiento-y-devolucion", ["procedimiento congelamiento devolucion", "proceso congelamiento devolucion", "trámite congelamiento devolucion"])
    procedure_cancellation_academic_charge_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/registro-y-control/cancelacion-carga-academica", ["procedimiento cancelacion de carga academica", "proceso cancelacion de carga academica", "trámite cancelacion de carga academica"])
    procedure_academic_certificates_questions_answers_array = scraping_procedures.get_procedures_requests_questions_answers(
        "https://www.uac.edu.co/admisiones-y-registro/registro-y-control/certificados-academicos", ["procedimiento certificado academico", "proceso certificado academico", "trámite certificado academico", "radicacion certificado academico"])
    programs_pregrado_questions_answers_array = scraping_programs.get_uac_programs_questions_answers(
        "https://www.uac.edu.co/oferta-academica/pregrado", "programas de pregrado")
    programs_specializations_questions_answers_array = scraping_programs.get_uac_programs_questions_answers(
        "https://www.uac.edu.co/oferta-academica/especializaciones", "programas de especializacion")
    programs_masteries_questions_answers_array = scraping_programs.get_uac_programs_questions_answers(
        "https://www.uac.edu.co/oferta-academica/maestrias", "programas de maestria")
    tuition_prices_questions_answers_array = scraping_programs.get_uac_tuition_prices_questions_answers()
    support_questions_answers_array = scraping_support.get_support_questions_answers()

    create_intents(
        admission_new_applicant_questions_answers_array, intents_object)
    create_intents(
        admission_external_transfer_applicant_questions_answers_array, intents_object)
    create_intents(
        admission_internal_transfer_applicant_questions_answers_array, intents_object)
    create_intents(
        admission_reentry_applicant_questions_answers_array, intents_object)
    create_intents(
        admission_foreign_applicant_questions_answers_array, intents_object)
    create_intents(
        pregrado_current_year_01_questions_answers_array, intents_object)
    create_intents(
        pregrado_current_year_02_questions_answers_array, intents_object)
    create_intents(
        posgrado_current_year_01_questions_answers_array, intents_object)
    create_intents(
        posgrado_current_year_02_questions_answers_array, intents_object)
    create_intents(
        pregrado_next_year_01_questions_answers_array, intents_object)
    create_intents(
        posgrado_next_year_01_questions_answers_array, intents_object)
    create_intents(
        procedure_academic_certificates_questions_answers_array, intents_object)
    create_intents(
        procedure_additional_charge_questions_answers_array, intents_object)
    create_intents(
        procedure_cancellation_academic_charge_questions_answers_array, intents_object)
    create_intents(
        procedure_freezing_refund_questions_answers_array, intents_object)
    create_intents(
        procedure_supplemental_exam_questions_answers_array, intents_object)
    create_intents(programs_masteries_questions_answers_array, intents_object)
    create_intents(programs_pregrado_questions_answers_array, intents_object)
    create_intents(
        programs_specializations_questions_answers_array, intents_object)
    create_intents(tuition_prices_questions_answers_array, intents_object)
    create_intents(support_questions_answers_array, intents_object)

    with open('intents.json', 'w') as fp:
        json.dump(intents_object, fp, indent=4)
