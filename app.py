# File name: app.py
# Description: an app, which allows to feed original and translation phrases and check the statistics of how to translate future
# Author: Kirill Nikolaev

from original import Original
from translation import Translation

class PhraseApp:
    def __init__(self):
        pass

    def run(self):
        print("Welcome!")

        while True:
            print("\nWhat would you like to do?")
            print("1. Feed original phrase")
            print("2. Feed translation phrase")
            print("3. Check the statistics of how to translate future")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.feed_original_phrase()
            elif choice == '2':
                self.feed_translation_phrase()
            elif choice == '3':
                # Here you can add the code to check the statistics of how to translate future
                pass
            elif choice == '4':
                break
            else:
                print("Invalid choice. Please try again.")

    def feed_original_phrase(self):
        phrase = input("Enter the original phrase: ")
        verb_form = input("Enter the verb form: ")
        aspect = input("Enter the aspect: ")
        adverb = input("Enter the adverb (optional): ")
        object = input("Enter the object (optional): ")
        original = Original(phrase, verb_form, aspect, adverb, object)

    def feed_translation_phrase(self):
        phrase = input("Enter the translation phrase: ")
        verb_form = input("Enter the verb form: ")
        adverb = input("Enter the adverb (optional): ")
        object = input("Enter the object (optional): ")
        translation = Translation(phrase, verb_form, adverb, object)

# To run the app
app = PhraseApp()
app.run()