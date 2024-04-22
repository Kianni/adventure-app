# File name: fiDescription.py
# Description: This file contains the grammatical description of the phrase in Finnish
# Author: Kirill Nikolaev

from desription import Phrase


class Translation(Phrase):
    def __init__(self, phrase, verb_form, adverb = None, object = None):
        super().__init__(phrase, verb_form, adverb, object)

    def what_kind_of_future(self):
        pass