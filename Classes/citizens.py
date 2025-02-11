from random import randrange
from Data import all_citizens, all_citizens_by_profession

first_name = ['Alphonse', 'Warren', 'Joseph', 'Hugo', 'Rosa', 'Nexerino', 'Jotaro', 'Giuseppe', 'Lucien', "Renato", 'Bruno']
last_name = ['Kensington', 'Musk', 'Buffet', 'Bezos', 'Zuckerberg', 'Gates', "Fanon", "Stalin", "Ventura", 'Maffi']

default_commodities = {"money" : 100}


class Machine:
    def __init__(self, name, idle_rate, active_rate):
        self.name = name
        self.idle_rate = idle_rate # how much out of 100 gets - with 1 hr
        self.active_rate = active_rate
        self.current_functionality = 100
        self.status = "functional"

    def depreciate(self, time_required=1, active=False):
        """Depreciate the machine based on usage or idleness."""
        rate = (self.active_rate + self.idle_rate if active else self.idle_rate) * time_required
        self.current_functionality -= rate
        self.remaining_value = max(0, self.remaining_value - rate)  # Prevents dropping below 0

        if self.remaining_value == 0:
            self.status = "broken"
            print(f"{self.name} has broken down!")

class Citizens():
    def __init__(self, property = {}):
        self.name = first_name[randrange(len(first_name))] + " " + last_name[randrange(len(last_name))]
        self.profession = ""
        if property:
            self.property = property
        else: 
            self.property = default_commodities        
        self.machines = []
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
    for _ in range(int(quantity)):
        new_citizen = Citizens()
        if profession:
            new_citizen.assign_profession(profession)


def assign_commodities_to_pops(citizens_nums = [], quality = "", quantity = 1):
    
    for citizen_num in citizens_nums:
        try:
            all_citizens[citizen_num].commodities[quality] += quantity
        except:
            all_citizens[citizen_num].commodities[quality] = quantity


def assign_machines_to_pops(citizens_nums = [], quality = "", quantity = 1, idle_rate = 0, active_rate = 0):
    for citizen_num in citizens_nums:
        for _ in range(quantity):
            new_machine = Machine(quality, idle_rate, active_rate)
            all_citizens[citizen_num].machines.append(new_machine)