# File name: description.py
# Description: This file contains the basic grammatical description of the phrase
# Author: Kirill Nikolaev

class Phrase:
    def __init__(self, phrase, verb_form, adverb = None, object = None):
        self.phrase = phrase
        self.verb_form = verb_form
        self.adverb = adverb
        self.object = object
