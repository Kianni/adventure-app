# File name: traveller.py
# Description: Create a class called Traveller
# Author: Kirill Nikolaev

class Traveller:
    def __init__(self, name, budget = 250, land = "Finland"):
        self.name = name
        self.budget = budget
        self.land = land

if __name__ == "__main__":
    traveller = Traveller("Alice")
    print(traveller.name)
    print(traveller.budget)
    print(traveller.land)