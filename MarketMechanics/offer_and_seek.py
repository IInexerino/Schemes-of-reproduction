from Data import *
from Classes import MarketCommodities


def put_batch_of_commodities_for_sale(seller, quality, offer_price_perUnit, quantity):
    if quantity <= 0:
        print(f"Error: quantity ({quantity}) of quality ({quality}) sold by {seller.name}, must be a positive integer.")
        return # invalid quantity of commodities
    
    for a, b in seller.commodities.items(): # Check if seller has enough to sell how much he desires to
        if quality == a and quantity > b:
            print(f'\nCitizen {seller.name} does not have enough of this commodity to put up for sale.')
            return
        elif quality == a and quantity <= b:
            break

    else: # if the loop completes without finding the item
        print(f'\nCitizen {seller.name} does not have enough of this commodity to put up for sale.')
        return
    
    MarketCommodities(seller, quality, offer_price_perUnit, quantity) # If all checks passed, creates an instance of MarketCommodities | assumption that offer price does not change, 
    # not necessarily inherently accompanied by the assumption that the buyer must buy, because in order to buy the 
    # function needs to be run, so that in effect signifies the agreement for an offer price. We will make the assumption 
    # that the buyer takes a given offer price, but this assumption is not made here


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
