import data
from greeting import GreetingQuiz

class Trip:
    def __init__(self, traveller, destination):
        self.traveller = traveller
        self.destination = destination

        if self.traveller.land == self.destination:
            print(f"{self.traveller.name} is already in {self.destination['name']}. Enjoy!!!")

        self.start()

    def check_budget_and_travel(self):
        if self.traveller.budget >= 100:  # Assume travel cost is 100
            print(f"Welcome to {self.destination['name']}, {self.traveller.name}!")
            self.traveller.budget -= 100  # Decrease budget by travel cost
            return True
        else:
            print(f"{self.traveller.name} does not have enough budget to travel.")
            return False

    def start_quiz(self):
        print(f"{self.traveller.name}, would you like to take a quiz to increase your budget?")
        answer = input()
        if answer.lower() == "yes":
            quiz = GreetingQuiz(data.lands, self.destination)
            quiz_result = False

            while not quiz_result:
                quiz_result = quiz.start()
                if quiz_result:
                    print("You've won the quiz! Your budget has been increased by 100.")
                    self.traveller.budget += 100
                else:
                    print("You've lost the quiz. Would you like to try again? (yes/no)")
                    try_again = input().lower()
                    if try_again != 'yes':
                        break
        else:
            print("Goodbye!")
            exit()

    def start(self):
        if not self.check_budget_and_travel():
            self.start_quiz()
            self.check_budget_and_travel()
