# File name: quiz.py
# Description: Create a parent class for Quizes
# Author: Kirill Nikolaev

import random

class Quiz:
    def __init__(self, lands, initial_land=None):
        self.lands = lands
        self.initial_land = initial_land

    def set_land(self):
        if self.initial_land:
            quiz_land = self.initial_land
            self.initial_land = None  # Reset initial_land after the first quiz
        else:
            quiz_land = random.choice(self.lands)
        return quiz_land