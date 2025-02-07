from random import *

from Data import *
from Classes import *
from MarketMechanics import *

print('')

day = 0
PROD_RECIPES = {
    'flour' : {
        'inputs' : {
            "LP_per_day" : 1
        },
        'outputs' : {
            "flour100g" : 10
        }
    },
    'spaghetti' : {
        'inputs' : {
            "LP_per_day" : 1,
            "flour100g" : 10
        },
        'outputs' : {
            "spaghetti100g" : 10
        }
    }
}


def produce(ownerofmop, recipe, itterations = 1): # C - P - C
    for _ in range(itterations):
        # creates reference variables to PROD_RECIPES input/output sub-dicts
        inputs = PROD_RECIPES[recipe]["inputs"]
        outputs = PROD_RECIPES[recipe]["outputs"]
        
        for a, b in inputs.items():
            # checks if the producer has enough commodities to mobilize for this recipe
            if ownerofmop.property.get(a, 0) >= b:
                continue
            else:
                print(f"\n{ownerofmop.name} does not have enough {a} to produce {recipe}.")
                return
        for a, b in inputs.items():
            ownerofmop.property[a] -= b

        for a, b in outputs.items():
            ownerofmop.property[a] = ownerofmop.property.get(a, 0) + b
        print(f"\n{ownerofmop.name} successfully produced {recipe}.")














def pass_day():
    day = day + 1
    print(f"day {day}")


def printProperty():
    for a in all_citizens:
        print(f'\n> Citiizen {a.name}')
        for x, y in a.property.items():
            print(x, y)
        print(f'${a.money}\n')


createCitizens()

#initially assign property to capitalist
all_citizens[0].property["flour100g"] = 100
all_citizens[0].property["LP_per_day"] = 10


produce(all_citizens[0], 'spaghetti')

printProperty()

put_batch_of_commodities_for_sale(all_citizens[0], 'flour100g', 0.1, 25)
put_batch_of_commodities_for_sale(all_citizens[0], 'LP_per_day', 0.1, 3)


print(CURRENT_MARKETPLACE)

printProperty()


purchase_commodities(all_citizens[1], "flour100g", 20)
purchase_commodities(all_citizens[1], "LP_per_day", 2)


print(CURRENT_MARKETPLACE)


printProperty()


produce(all_citizens[0], 'spaghetti')
produce(all_citizens[1], 'spaghetti', 2)

for a in CURRENT_MARKETPLACE:
    print(f"{a.quantity} : {a.quality} - {a.seller} | {a.seller.name}")
print('')