# File name: greeting.py
# Description: This file contains the greeting message
# Author: Kirill Nikolaev


import random

class GreetingQuiz:
    def __init__(self, lands, initial_land=None):
        self.lands = lands
        self.initial_land = initial_land

    def start(self):
        # Select the initial land for the first quiz, then a random land for subsequent quizzes
        if self.initial_land:
            quiz_land = self.initial_land
            self.initial_land = None  # Reset initial_land after the first quiz
        else:
            quiz_land = random.choice(self.lands)

        # Prepare the correct and incorrect answers
        correct_answer = quiz_land["greeting"]["response"]
        incorrect_answers = [land["greeting"]["response"] for land in self.lands if land != quiz_land]
        random.shuffle(incorrect_answers)

        # Select three incorrect answers
        incorrect_answers = incorrect_answers[:3]

        # Combine correct and incorrect answers and shuffle them
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        # Present the quiz to the user
        print(f"Question: How would you respond to the greeting '{quiz_land['greeting']['phrase']}' in {quiz_land['name']}?")
        for i, answer in enumerate(answers, start=1):
            print(f"{i}. {answer}")

        # Get the user's answer
        user_answer = int(input("Enter the number of your answer: "))

        # Check if the user's answer is correct
        if answers[user_answer - 1] == correct_answer:
            return True
        else:
            return False

if __name__ == "__main__":
    import data
    
    quiz = GreetingQuiz(data.lands)
    quiz.start()