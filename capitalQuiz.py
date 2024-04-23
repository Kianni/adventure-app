# File name: capitalQuiz.py
# Description: Create a quiz to guess the capital of a country
# Author: Kirill Nikolaev

import random
from quiz import Quiz


class CapitalQuiz(Quiz):
    def start(self):
        correct_land = self.set_land()

        incorrect_lands = random.sample([land for land in self.lands if land != correct_land], 3)
        options = [correct_land] + incorrect_lands
        random.shuffle(options)

        print(f"What is the capital of {correct_land.name}?")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option.capital}")

        answer = int(input("Enter the number of your choice: "))
        if options[answer - 1] == correct_land:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is {correct_land.capital}.")
            return False
        
        
if __name__ == "__main__":
    import data

    quiz = CapitalQuiz(data.lands)
    quiz.start()