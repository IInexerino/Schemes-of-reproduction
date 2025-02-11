from Data import CURRENT_MARKETPLACE

class MarketCommodities():
    def __init__(self, seller, quality, offer_price_perUnit, quantity):
        """Creates a market listing for either a commodity or a machine."""

        # If it's a commodity, deduct from seller's inventory
        if quality in seller.commodities:
            seller.commodities[quality] -= quantity  

        # If it's a machine, remove from seller's machine list
        elif quality in [m.name for m in seller.machines]:  
            machines_to_sell = [m for m in seller.machines if m.name == quality][:quantity]
            for machine in machines_to_sell:
                seller.machines.remove(machine)
                
        self.seller = seller
        self.quality = quality
        self.quantity = quantity
        self.offer_price_perUnit = offer_price_perUnit
        CURRENT_MARKETPLACE.append(self)