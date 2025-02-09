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
        y = y * itterations
        if purchase_commodities(ownerofmoney, x, y, dry_run=True) == "fail":
            print(f"\n{ownerofmoney.name} cannot afford or find enough {x} to buy the goods needed to produce {recipe}.")
            return "fail"

    # If all purchases are possible, execute them
    for x, y in inputs.items():
        y = y * itterations
        purchase_commodities(ownerofmoney, x, y)

    print(f"Citizen {ownerofmoney} sucessfully bought commodities for x{itterations} production of {recipe}")
    # Proceed with production (C-P-C)
    C_P_C(ownerofmoney, recipe, itterations)
    return "success"
    

def M_C_P_C_M(owenerofmoney, recipe, offerprice_unit, itterations = 1):
    outputs = PROD_RECIPES[recipe]['outputs']

    # check if M_C_P_C can be done and the commodity can be aquired
    M_C_P_C_status = M_C_P_C(owenerofmoney, recipe, itterations)

    if M_C_P_C_status == "fail":
        print(f"\nCitizen {owenerofmoney.name} {owenerofmoney} for some reason failed to purchase the commodities necessary to produce the specified recipe, aborting without proceeding with sale as the commodity to be sold was not produced.")
        return "fail"
    
    # sell the specified amount of that commodity
    if M_C_P_C_status == "success":
        for a, b in outputs.items():
            b = b * itterations
            put_batch_of_commodities_for_sale(owenerofmoney, a, offerprice_unit, b)