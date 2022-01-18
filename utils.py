import unidecode
import re
import spanishinflector
from nltk import SnowballStemmer

spanish_inflector = spanishinflector.Spanish()
spanish_steemer = SnowballStemmer('spanish')


def adapt_phrase_to_bot(phrase):

    phrase = phrase.lower()
    phrase = re.sub(r'[^\w]', ' ', phrase)
    phrase = phrase.replace('1a', 'primera').replace('2a', 'segunda').replace('3a', 'tercera').replace(
        '4a', 'cuarta').replace('1ª', 'primera').replace('2ª', 'segunda').replace('3ª', 'tercera').replace('4ª', 'cuarta').replace('1°', 'primera').replace('2°', 'segunda').replace('3°', 'tercera').replace('4°', 'cuarta').replace('1º', 'primera').replace('2º', 'segunda').replace('3º', 'tercera').replace('4º', 'cuarta').replace(' 1 ', ' primera ').replace(' 2 ', ' segunda ').replace(' 3 ', ' tercera ').replace(' 4 ', ' cuarta ').replace('evaluaciones', 'examenes')
    print(phrase)
    phrase_splitted = phrase.split()
    phrase_singularized_words = []
    for word in phrase_splitted:
        word = spanish_inflector.singularize(word)
        word = spanish_steemer.stem(word)
        phrase_singularized_words.append(word)
    phrase = ' '.join(phrase_singularized_words)

    phrase = unidecode.unidecode(phrase)

    return phrase
