from random import randrange
from Data import *

first_name = ['Alphonse', 'Warren', 'Joseph', 'Hugo', 'Rosa', 'Nexerino', 'Jotaro', 'Giuseppe', 'Lucien', "Renato", 'Bruno']
last_name = ['Kensington', 'Musk', 'Buffet', 'Bezos', 'Zuckerberg', 'Gates', "Fanon", "Stalin", "Ventura", 'Maffi']

class Citizens():
    def __init__(self, property = {}):
        self.name = first_name[randrange(len(first_name))] + " " + last_name[randrange(len(last_name))]
        if property:
            self.commodities = property
        else: 
            self.commodities = {
                "money" : 100
            }
        all_citizens.append(self)

    def assign_profession(self, profession_input):
        self.profession = profession_input
        try:
            all_citizens_by_profession[profession_input].append(self)
        except:
            all_citizens_by_profession[profession_input] = [self]

    def money_income (self, amount):
        self.commodities["money"] += amount

    def money_spending (self, amount):
        if self.commodities["money"] - amount <= 0:
            print(f'Citizen {self.name} does not have enough money to spend')
        else:
            self.commodities["money"] -= amount


# admin functions
def createCitizens(quantity = 1, profession = ""):
    while True:
        if input == "manual":
            quantity = input('\nHow many citizens would you like to create? Or would you first like to set a profession (p):\n\n> ')
            if quantity == "p":
                profession = input("\nChoose the profession you would like the citizens to be:\n\n> ")
                continue
            elif (quantity() != True) or int(quantity) <= 0:
                print("\nEner a valid input.")
                continue
        for _ in range(int(quantity)):
            new_citizen = Citizens()
            try:
                new_citizen.assign_profession(profession)
            except:
                ...
        break


def assign_commodities_to_pops(input, citizens_nums = [], quality = "", quantity = 1):
    if input == "manual":
        print("\n___________________________________________________________________________")
        user_input = input('Enter the following information in the following format and order:\n[citizen nums separated by comma and whitespace]|"quality"|quantity\n\n> ')
        user_input_list = user_input.split("|")
        citizens_nums = (user_input_list[0].strip("[]")).split(", ")
        quality = user_input_list[1]
        quantity = int(user_input_list[2])
    
    for citizen_num in citizens_nums:
        try:
            all_citizens[citizen_num].commodities[quality] += quantity
        except:
            all_citizens[citizen_num].commodities[quality] = quantity

