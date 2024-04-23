# File name: app.py
# Description: an app, which allows to feed original and translation phrases and check the statistics of how to translate future
# Author: Kirill Nikolaev

from trip import Trip
from traveller import Traveller
import data

class AdventuresApp:
    def __init__(self):
        pass

    def run(self):
        print("Hello, stranger! What is your name?")
        name = input()
        print("What is your budget?")
        budget = input()

        print("What is your land of residence?")
        land_of_residence = self.select_land()

        traveller = Traveller(name, budget, land_of_residence)

        print("Where would you like to travel?")
        destination = self.select_land()
        make_a_trip = Trip (traveller, destination)
        # traveller.travel(destination)
        # traveller.greet(destination)
        # traveller.work()
    
    def select_land(self):
        for i, land in enumerate(data.lands, start=1):
            print(f"{i}. {land['name']}")

        choice = int(input("Enter the number of your choice: "))
        return data.lands[choice - 1]


# To run the app
app = AdventuresApp()
app.run()