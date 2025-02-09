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


# display functions
def display_current_info(what_to_display = "all"):
    if what_to_display == "all" or "commodities":
        print("\n___________________________________________________________________________")
        for a in all_citizens:
            print(f'\n\n> Citiizen {a.name}\n{a}\n')
            for x, y in a.commodities.items():
                print("-" + x, y)
        print("___________________________________________________________________________")
    if what_to_display == "all" or "current marketplace":  
        print("\n___________________________________________________________________________")
        for a in CURRENT_MARKETPLACE:
            print(f"\n{a.quantity}  - ${a.offer_price_perUnit}/unit : {a.quality} - {a.seller} | {a.seller.name}")
        print("___________________________________________________________________________")


def display_current_info_in_ui(what_to_display = "all"):
    result = ""
    if what_to_display == "all" or "commodities":
        result += ("\n___________________________________________________")
        for a in all_citizens:
            result += (f'\n\n> Citiizen {a.name}\n{a}\nProfession: {a.profession}\n')
            for x, y in a.commodities.items():
                result += (f"\n- {x} {y}")
            result += "\n"
        result += ("\n___________________________________________________")
    if what_to_display == "all" or "current marketplace": 
        if CURRENT_MARKETPLACE: 
            result += ("\n___________________________________________________________________________")
            for a in CURRENT_MARKETPLACE:
                result += (f"\n{a.quantity} - ${a.offer_price_perUnit}: {a.quality} - {a.seller} | {a.seller.name}")
            result += ("\n___________________________________________________________________________")

    return result


#run code
createCitizens(5)

assign_commodities_to_pops("auto", [0, 4], "flour100g", 100)
assign_commodities_to_pops("auto", [0, 2, 4], "LP_per_day", 10)

display_current_info('all')

put_batch_of_commodities_for_sale(all_citizens[0], 'flour100g', 1, 25)
put_batch_of_commodities_for_sale(all_citizens[4], 'flour100g', 1, 25)
put_batch_of_commodities_for_sale(all_citizens[0], 'LP_per_day', 1, 7)


display_current_info('all')


purchase_commodities(all_citizens[1], "flour100g", 20)
purchase_commodities(all_citizens[1], "LP_per_day", 2)


display_current_info('all')

C_P_C(all_citizens[1], 'spaghetti', 2)


M_C_P_C_M(all_citizens[0], 'spaghetti', 1, 3)

display_current_info('all')

print('')