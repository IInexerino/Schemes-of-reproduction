from random import randrange
from Data import *

first_name = ['Alphonse', 'Warren', 'Joseph', 'Hugo', 'Rosa', 'Nexerino', 'Jotaro', 'Giuseppe', 'Lucien', "Renato", 'Bruno']
last_name = ['Kensington', 'Musk', 'Buffet', 'Bezos', 'Zuckerberg', 'Gates', "Fanon", "Stalin", "Ventura", 'Maffi']

class Citizens():
    def __init__(self):
        self.name = first_name[randrange(len(first_name))] + " " + last_name[randrange(len(last_name))]
        self.property = {
            "money" : 100.0
        }
        all_citizens.append(self)

    def assign_profession(self, profession_input):
        self.profession = profession_input
        try:
            all_citizens_by_profession[profession_input].append(self)
        except:
            all_citizens_by_profession[profession_input] = [self]

    def money_income (self, amount):
        self.property["money"] += amount

    def money_spending (self, amount):
        if self.property["money"] - amount <= 0:
            self.property["money"] -= amount
        else:
            print('This citizen does not have enough money to spend')


# creating a new citizen
def createCitizens():
    while True:
        createCitizens_quantity_input = input('\nHow many citizens would you like to create? Or would you first like to set a profession (p):\n\n> ')
        if createCitizens_quantity_input == "p":
            global profession_choice
            profession_choice = input("\nChoose the profession you would like the citizens to be:\n\n> ")
            continue
        elif (createCitizens_quantity_input.isnumeric() != True) or int(createCitizens_quantity_input) <= 0:
            print("\nEner a valid input.")
            continue
        for _ in range(int(createCitizens_quantity_input)):
            new_citizen = Citizens()
            try:
                new_citizen.assign_profession(profession_choice)
            except:
                ...
        break
