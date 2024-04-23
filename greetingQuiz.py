# File name: greeting.py
# Description: This file contains the greeting message
# Author: Kirill Nikolaev


import random
from quiz import Quiz

class GreetingQuiz(Quiz):
    def start(self):
        quiz_land = self.set_land()

        correct_answer = quiz_land["greeting"]["response"]
        incorrect_answers = [land["greeting"]["response"] for land in self.lands if land != quiz_land]
        random.shuffle(incorrect_answers)

        incorrect_answers = incorrect_answers[:3]
        answers = [correct_answer] + incorrect_answers
        random.shuffle(answers)

        print(f"Question: How would you respond to the greeting '{quiz_land['greeting']['phrase']}' in {quiz_land['name']}?")
        for i, answer in enumerate(answers, start=1):
            print(f"{i}. {answer}")

        user_answer = int(input("Enter the number of your answer: "))
        if answers[user_answer - 1] == correct_answer:
            print("Correct!")
            return True
        else:
            print(f"Wrong! The correct answer is '{correct_answer}'.")
            return False

if __name__ == "__main__":
    import data
    
    quiz = GreetingQuiz(data.lands)
    quiz.start()