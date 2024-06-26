# File name: app.py
# Description: an app, which allows a user to travel imaginarily to different countries
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
        budget = int(input())

        print("What is your land of residence?")
        land_of_residence = self.select_land()

        traveller = Traveller(name, budget, land_of_residence)

        while True:
            print("Where would you like to travel?")
            destination = self.select_land()
            print(f"you are travelling from {traveller.land.name} to {destination.name}.")
            if traveller.land.name == destination.name:
                print(f"{traveller.name}, you are already in {destination.name}. Enjoy!!!")
            else:
                make_a_trip = Trip(traveller, destination)

            print("Would you like to make another trip? (yes/no)")
            another_trip = input().lower()
            if another_trip != 'yes':
                print(f"Enjoy your time in {destination.name}!")
                break
    
    def select_land(self):
        for i, land in enumerate(data.lands, start=1):
            print(f"{i}. {land.name}")

        choice = int(input("Enter the number of your choice: "))
        return data.lands[choice - 1]


# To run the app
app = AdventuresApp()
app.run()