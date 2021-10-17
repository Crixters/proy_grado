import unidecode 
import re 
import spanishinflector

spanish_inflector = spanishinflector.Spanish()

def adapt_phrase_to_bot(phrase):
    
    phrase = phrase.lower()
    phrase = re.sub(r'[^\w]', ' ', phrase)

    phrase_splitted = phrase.split()
    phrase_singularized_words = []
    for word in phrase_splitted:
        word = spanish_inflector.singularize(word)
        phrase_singularized_words.append(word)
    phrase = ' '.join(phrase_singularized_words)

    phrase = unidecode.unidecode(phrase)
    
    return phrase