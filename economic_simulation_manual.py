from random import *

from Data import *
from Classes import *
from MarketMechanics import *
from ProductionMechanics import *

day = 0
print('')

# experimental functions
#def pass_day():
#    day = day + 1
#    print(f"day {day}")


#create some citizens and do some things
createCitizens(5)

assign_commodities_to_pops("auto", [0, 4], "flour100g", 100)
assign_commodities_to_pops("auto", [0, 2, 4], "LP_per_day", 10)

offer_commodity_batch_for_sale(all_citizens[0], 'flour100g', 1, 25)
offer_commodity_batch_for_sale(all_citizens[4], 'flour100g', 1, 25)
offer_commodity_batch_for_sale(all_citizens[0], 'LP_per_day', 1, 7)


purchase_commodities(all_citizens[1], "flour100g", 20)
purchase_commodities(all_citizens[1], "LP_per_day", 2)

C_P_C(all_citizens[1], 'spaghetti', 2)


M_C_P_C_M(all_citizens[0], 'spaghetti', 1, 3)

print('')