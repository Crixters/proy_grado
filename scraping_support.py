from bs4 import BeautifulSoup
import requests
import unidecode 
import re

def get_support_questions_answers():

    urlSupport= "https://www.uac.edu.co/canales-atencion/"

    questions_answers_array = []

    support_page_response = requests.get(urlSupport)
    support_page_soup_object = BeautifulSoup(support_page_response.content,'html.parser')

    tab_content = support_page_soup_object.find('div',{'class':'tab-content'})
    tab_panels = tab_content.find_all('div',{'role':'tabpanel'})

    for tab_panel in tab_panels:

        question_answer = []

        department_title = tab_panel.find('h5').get_text().strip()
        question = "numero numeros de contacto canales de atencion "+department_title
        question = question.lower()
        question = unidecode.unidecode(question)
        question = re.sub(r'[^\w]', ' ', question)

        contact_text = ""

        support_information_body = tab_panel.find('div',{'class':'card-body'})
        support_information_tables = support_information_body.find_all('table')
        
        if len(support_information_tables) > 0:
            for support_information_table in support_information_tables:
                table_rows = support_information_table.find_all('tr')
                if(len(table_rows[0].find_all('td'))>1):
                    title_table_row_tds = table_rows[0].find_all('td')
                    init_range = 1
                else :
                    title_table_row_tds = table_rows[1].find_all('td')
                    init_range = 2
                for i in range(init_range,len(table_rows)): 
                    table_row_data_cells = table_rows[i].find_all('td')
                    for j in range(0,len(table_row_data_cells)):
                        if table_row_data_cells[j].get_text().strip():
                            contact_text = contact_text + title_table_row_tds[j].get_text().strip()+": " + table_row_data_cells[j].get_text().strip() + "\n\n"
                    contact_text = contact_text + "-------------------------------" + "\n"
        else:
            for br in support_information_body.find_all("br"):
                br.replace_with("\n")
            contact_text = support_information_body.get_text().strip().replace("   ","")

        question_answer.append(question)
        question_answer.append(contact_text)
        questions_answers_array.append(question_answer)
   
    return questions_answers_array


