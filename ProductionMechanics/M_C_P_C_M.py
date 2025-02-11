from Data import PROD_RECIPES
from MarketMechanics import purchase_commodities, offer_commodity_batch_for_sale
from Classes import Machine

def C_P_C(ownerofmop, recipe, iterations=1):
    """Processes a production cycle by consuming inputs, producing outputs, and handling machine outputs."""

    for _ in range(iterations):
        inputs = PROD_RECIPES[recipe]["inputs"]
        outputs = PROD_RECIPES[recipe]["outputs"]
        required_machines = PROD_RECIPES[recipe].get("minputs", [])
        machine_outputs = PROD_RECIPES[recipe].get("moutputs", {})
        time_required = PROD_RECIPES[recipe]["time_required"]

        # Check if the owner has the necessary input commodities
        for commodity, amount in inputs.items():
            if ownerofmop.commodities.get(commodity, 0) < amount:
                print(f"\n{ownerofmop.name} lacks {commodity} to produce {recipe}.")
                return "fail"

        # Check if the owner has the required machines
        machines_used = []
        for machine_type, count_needed in required_machines.items():
            available_machines = sorted(
                [m for m in ownerofmop.owned_machines if m.name == machine_type and m.remaining_value > 0],
                key=lambda m: m.remaining_value, reverse=True
            )

            if len(available_machines) < count_needed:
                print(f"\n{ownerofmop.name} lacks {count_needed} working {machine_type}(s) to produce {recipe}.")
                return "fail"

            machines_used.extend(available_machines[:count_needed])

        # Deduct input commodities
        for commodity, amount in inputs.items():
            ownerofmop.commodities[commodity] -= amount

         # Depreciate the selected machines based on their **active depreciation rate**
        for machine in machines_used:
            depreciation = machine.active_rate * time_required
            if machine.remaining_value >= depreciation:
                machine.remaining_value -= depreciation
            else:
                print(f"\n{machine.name} is too worn out to complete {recipe}.")
                return "fail"

        # Add output commodities
        for commodity, amount in outputs.items():
            ownerofmop.commodities[commodity] = ownerofmop.commodities.get(commodity, 0) + amount

         # Add new machines to owned_machines (machine outputs)
        for machine_type, count in machine_outputs.items():
            for _ in range(count):
                new_machine = Machine(machine_type, initial_value=100)  # Assuming initial lifespan = 100
                ownerofmop.owned_machines.append(new_machine)
                print(f"\n{ownerofmop.name} has produced a new {machine_type}.")


        print(f"\n{ownerofmop.name} successfully produced {recipe}.")

    return "success"
   
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
            offer_commodity_batch_for_sale(owenerofmoney, a, offerprice_unit, b)