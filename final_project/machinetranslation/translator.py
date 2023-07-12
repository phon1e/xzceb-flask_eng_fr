

""" using MyMemoryTranslator in deep_translator python library for translate text """
from deep_translator import MyMemoryTranslator


def english_to_french(english_text):
    """ This function take english text as input and translated to france as output"""
    return MyMemoryTranslator(source='english', target='french canada').translate(english_text)

def french_to_english(french_text):
    """ This function take french text as input and translated to english as output"""
    return MyMemoryTranslator(source='french canada', target='english').translate(french_text)
