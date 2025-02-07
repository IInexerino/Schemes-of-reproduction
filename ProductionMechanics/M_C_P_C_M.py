from Data import *

def C_P_C(ownerofmop, recipe, itterations = 1): # C - P - C
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
