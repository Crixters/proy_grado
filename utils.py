import unidecode
import re
import spanishinflector
from nltk import SnowballStemmer

spanish_inflector = spanishinflector.Spanish()
spanish_steemer = SnowballStemmer('spanish')

words_numbers = {}

def adapt_phrase_to_bot(phrase):

    phrase = phrase.lower()
    phrase = unidecode.unidecode(phrase)
    phrase = re.sub(r'[^\w]', ' ', phrase)
    phrase = phrase.replace(' 1a ', ' primera ').replace(' 2a ', ' segunda ').replace(' 3a ', ' tercera ').replace(' 4a ', ' cuarta ').replace(
        ' 1ª ', ' primera ').replace(' 2ª ', ' segunda ').replace(' 3ª ', ' tercera ').replace(' 4ª ', ' cuarta ').replace(
            ' 1° ', ' primera ').replace(' 2° ', ' segunda ').replace(' 3° ', ' tercera ').replace(' 4° ', ' cuarta ').replace(
                ' 1º ', ' primera ').replace(' 2º ', ' segunda ').replace(' 3º ', ' tercera ').replace(' 4º ', ' cuarta ').replace(
                    ' 1deg ', ' primera ').replace(' 2deg ', ' segunda ').replace(' 3deg ', ' tercera ').replace(' 4deg ', ' cuarta ').replace(
                    ' 1o ', ' primera ').replace(' 2o ', ' segunda ').replace(' 3o ', ' tercera ').replace(' 4o ', ' cuarta ').replace(
                    ' 1 era ', ' primera ').replace(' 2 da ', ' segunda ').replace(' 3 era ', ' tercera ').replace(' 4 ta ', ' cuarta ').replace(
            ' evaluaciones ', ' evaluacion examen ').replace(' examenes ',' evaluaciones examenes ').replace(' examen ',' evaluacion examen ').replace(' evaluacion ',' evaluacion examen ').replace(' evaluacion ',' evaluacion examen ').replace(
                'cion','').replace('inicia','inician comienzan empiezan ').replace(' finaliza ',' finaliza fin termina ').replace(' ia ','')

    phrase_splitted = phrase.split()
    phrase_no_repeated = " ".join(sorted(set(phrase_splitted), key=phrase_splitted.index))
    phrase_splitted_no_repeated = phrase_no_repeated.split()
    phrase_singularized_words = []
    for word in phrase_splitted_no_repeated:
        word = spanish_inflector.singularize(word)
        word = spanish_steemer.stem(word)
        phrase_singularized_words.append(word)
    phrase = ' '.join(phrase_singularized_words)

    phrase = unidecode.unidecode(phrase)

    print(phrase)
    return phrase
