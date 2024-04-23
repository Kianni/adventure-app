# File name: traveller.py
# Description: This file contains the grammatical description of the phrase in Russian
# Author: Kirill Nikolaev

class Traveller:
    def __init__(self, name, budget = 250, land = "Finland"):
        self.name = name
        self.budget = budget
        self.land = land

    def greet(self, land):
        greeting = land["greeting"]["phrase"]
        response = land["greeting"]["response"]
        print(f"{self.name} says: '{greeting}'")
        print(f"Local responds: '{response}'")

    def work(self):
        print(f"{self.name} is working to increase the budget.")
        self.budget += 100  # Increase budget by 100

    def travel(self, land):
        if self.budget >= 100:  # Assume travel cost is 100
            print(f"{self.name} is travelling to {land['name']}.")
            self.budget -= 100  # Decrease budget by travel cost
        else:
            print(f"{self.name} does not have enough budget to travel.")