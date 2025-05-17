import spacy # for sentence level tokenisation 
from textblob import TextBlob # spelling coreection 

nlp = spacy.load("en_core_web_sm") #load en language model 

def auto_corrector(paragraph):
    # processing paragraph with spacy into splitted sentences
    doc = nlp(paragraph)
    corrected_sentences = []

    for sent in doc.sents:
        # use textblob to correct spelling in each sentences and punctation.
        corrected = str(TextBlob(sent.text).correct())
        corrected_text = str(corrected).capitalize()
        corrected_sentences.append(corrected)
    # Join corrected sentences back into full paragraph
    corrected_paragraph = ' '.join(corrected_sentences)
    return corrected_paragraph

#user_input 
user_input = input("Enter the mistaken sentence:\n")
corrected_output = auto_corrector(user_input)
print("\ncorrected paragraph :\n", corrected_output)