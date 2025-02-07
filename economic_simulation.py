from random import *

from Data import *
from Classes import *
from MarketMechanics import *
from ProductionMechanics import *

day = 0
print('')

# experimental functions
def pass_day():
    day = day + 1
    print(f"day {day}")

# admin functions
def assign_property_to_pops(input, citizens_nums = [], quality = "", quantity = 1):
    if input == "manual":
        print("\n___________________________________________________________________________")
        user_input = input('Enter the following information in the following format and order:\n[citizen nums separated by comma and whitespace]|"quality"|quantity\n\n> ')
        user_input_list = user_input.split("|")
        citizens_nums = (user_input_list[0].strip("[]")).split(", ")
        quality = user_input_list[1]
        quantity = int(user_input_list[2])
    
    for citizen_num in citizens_nums:
        try:
            all_citizens[citizen_num].property[quality] += quantity
        except:
            all_citizens[citizen_num].property[quality] = quantity



# display functions
def display_current_info(what_to_display):
    if what_to_display == "all" or "property":
        print("\n___________________________________________________________________________")
        for a in all_citizens:
            print(f'\n\n> Citiizen {a.name}')
            for x, y in a.property.items():
                print("-" + x, y)
        print("___________________________________________________________________________")
    if what_to_display == "all" or "current marketplace":  
        print("\n___________________________________________________________________________")
        for a in CURRENT_MARKETPLACE:
            print(f"\n{a.quantity} : {a.quality} - {a.seller} | {a.seller.name}")
        print("___________________________________________________________________________")


#run code

createCitizens()


assign_property_to_pops("auto", [0, 4, 9], "flour100g", 100)
assign_property_to_pops("auto", [0, 2, 4], "LP_per_day", 10)



C_P_C(all_citizens[0], 'spaghetti')

display_current_info('all')

put_batch_of_commodities_for_sale(all_citizens[0], 'flour100g', 0.1, 25)
put_batch_of_commodities_for_sale(all_citizens[0], 'LP_per_day', 0.1, 3)


display_current_info('all')


purchase_commodities(all_citizens[1], "flour100g", 20)
purchase_commodities(all_citizens[1], "LP_per_day", 2)


display_current_info('all')


C_P_C(all_citizens[0], 'spaghetti')
C_P_C(all_citizens[1], 'spaghetti', 2)

print('')