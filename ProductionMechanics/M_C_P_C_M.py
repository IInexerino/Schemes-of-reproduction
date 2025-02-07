from Data import *
from MarketMechanics import *

def C_P_C(ownerofmop, recipe, itterations = 1): # C - P - C
    for _ in range(itterations):
        # creates reference variables to PROD_RECIPES input/output sub-dicts
        inputs = PROD_RECIPES[recipe]["inputs"]
        outputs = PROD_RECIPES[recipe]["outputs"]
        
        for a, b in inputs.items():
            # checks if the producer has enough commodities to mobilize for this recipe
            if ownerofmop.commodities.get(a, 0) >= b:
                continue
            else:
                print(f"\n{ownerofmop.name} does not have enough {a} to produce {recipe}.")
                return "fail"
        for a, b in inputs.items():
            ownerofmop.commodities[a] -= b

        for a, b in outputs.items():
            ownerofmop.commodities[a] = ownerofmop.commodities.get(a, 0) + b
        print(f"\n{ownerofmop.name} successfully produced {recipe}.")


def M_C_P_C(ownerofmoney, recipe, itterations = 1):
    inputs = PROD_RECIPES[recipe]["inputs"]

    # Check if ALL required purchases can be made
    for x, y in inputs.items():
        if purchase_commodities(ownerofmoney, x, y, dry_run=True) == "fail":
            print(f"\n{ownerofmoney.name} cannot afford or find enough {x} to produce {recipe}.")
            return  # Abort if any single purchase fails.

    # If all purchases are possible, execute them
    for x, y in inputs.items():
        purchase_commodities(ownerofmoney, x, y)

    # Proceed with production (C-P-C)
    C_P_C(ownerofmoney, recipe)