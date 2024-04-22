# File name: original.py
# Description: This file contains the grammatical description of the phrase in Russian
# Author: Kirill Nikolaev

from description import Phrase


class Original(Phrase):
    def __init__(self, phrase, verb_form, aspect, adverb = None, object = None):
        super().__init__(phrase, verb_form, adverb, object)
        self.aspect = aspect
        self.translation = None

    def what_kind_of_future(self):
        pass