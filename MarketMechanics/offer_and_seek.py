from Data import CURRENT_MARKETPLACE
from Classes import MarketCommodities, Machine


# ===================== SELL FUNCTIONS ===================== #

def offer_commodity_batch_for_sale(seller, quality, offer_price_perUnit, quantity):
    """Puts a batch of commodities up for sale, assuming all are identical."""
    if quantity <= 0:
        print(f"Error: quantity ({quantity}) of quality ({quality}) sold by {seller.name}, must be a positive integer.")
        return  # Invalid quantity of commodities
    
    if seller.commodities.get(quality, 0) < quantity:
        print(f'\nCitizen {seller.name} does not have enough of this commodity to put up for sale.')
        return
    
    MarketCommodities(seller, quality, offer_price_perUnit, quantity) # If all checks passed, creates an instance of MarketCommodities | assumption that offer price does not change, 
    # not necessarily inherently accompanied by the assumption that the buyer must buy, because in order to buy the 
    # function needs to be run, so that in effect signifies the agreement for an offer price. We will make the assumption 
    # that the buyer takes a given offer price, but this assumption is not made here


def offer_1machine_for_sale(seller, machine, offer_price, quantity):
    """Put a machine up for sale. Each machine is unique."""
    if machine.remaining_value <= 0:
        print(f"Error: {seller.name} is trying to sell a broken {machine.name}.")
        return  

    MarketCommodities(seller, machine, offer_price, 1)


def purchase_commodities(buyer, quality, quantity, dry_run = False): # M-C / C-M
    shopping_cart = []
    prices_per_unit = []
    quantities = []

    sorted_selected_marketplace = sorted(
        [a for a in CURRENT_MARKETPLACE if a.quality == quality and a.quantity > 0],
        key=lambda x: x.offer_price_perUnit
    )

    # making a shopping cart and checking if there is enough to buy, and if you can afford
    if not sorted_selected_marketplace:
        print(f'\nCitizen {buyer.name} is attempting to buy commodity {quality} that does not exist on the market.')
        return "fail"
    for a in sorted_selected_marketplace:
        if a.quantity > 0: # check if there is more than one of this kind of good

            if sum(quantities) + a.quantity > quantity: # check if with the addition of this next batch of commodities, we would get more than we need
                shopping_cart.append(a)
                prices_per_unit.append(a.offer_price_perUnit)
                quantity_potentially_overexchanged = ((sum(quantities) + a.quantity) - quantity)
                quantity_of_this_batch_required = a.quantity -  quantity_potentially_overexchanged
                quantities.append(quantity_of_this_batch_required)
                break

            elif sum(quantities) < quantity: # check if we dont have enough commodities to satisfy us yet
                shopping_cart.append(a)
                prices_per_unit.append(a.offer_price_perUnit)
                quantities.append(a.quantity)

    if sum(quantities) < quantity: # check if after going through every commodity on the market we are still not at satisfaction
        print(f"\nThere isn't enough on the market for citizen {buyer.name} to buy how much he desires.")
        return "fail"
    
    else: # otherwise if we are at a quantity of satisfaction
        if sum(a * b for a, b in zip(prices_per_unit, quantities)) > buyer.commodities["money"]: # checks if buyer has too little money
            print(f"\nCitizen {buyer.name} does not have enough money to afford this commodity.")
            return "fail"
        elif dry_run:
                return "success" 
        
        else: # buyer has enough or more than enough money
            for (a, b, c) in zip(shopping_cart, prices_per_unit, quantities):
                buyer.money_spending(round(b * c, 2))  # Deduct the rounded cost
                try:
                    buyer.commodities[a.quality] += c  # Add the purchased quantity to buyer's commodities
                except KeyError:
                    buyer.commodities[a.quality] = c
                a.seller.money_income(round(b * c, 2))  # Add the rounded cost to seller's money
                a.quantity -= c  # Reduce the commodity quantity
                if a.quantity == 0:  # Remove item from the marketplace if sold out
                    CURRENT_MARKETPLACE.remove(a)

            return "success"


def purchase_machine(buyer, machine_type, dry_run=False):

    available_machines = sorted(
        [a for a in CURRENT_MARKETPLACE if isinstance(a.quality, Machine) and a.quality.name == machine_type and a.quantity > 0],
        key=lambda x: x.offer_price_perUnit / max(1, x.quality.current_functionality)  
    )

    if not available_machines:
        print(f"\n{buyer.name} wants to buy a {machine_type}, but none are available.")
        return "fail"

    best_machine = available_machines[0]  

    if best_machine.offer_price_perUnit > buyer.commodities["money"]:
        print(f"\n{buyer.name} does not have enough money to buy {machine_type}.")
        return "fail"

    if dry_run:
        return "success"

    buyer.money_spending(best_machine.offer_price_perUnit)
    best_machine.seller.money_income(best_machine.offer_price_perUnit)
    buyer.owned_machines.append(best_machine.quality)  
    CURRENT_MARKETPLACE.remove(best_machine)  

    return "success"