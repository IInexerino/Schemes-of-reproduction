from Data import CURRENT_MARKETPLACE

class MarketCommodities():
    def __init__(self, seller, quality, offer_price_perUnit, quantity):
        seller.commodities[quality] -= quantity
        self.seller = seller
        self.quality = quality
        self.quantity = quantity
        self.offer_price_perUnit = offer_price_perUnit
        CURRENT_MARKETPLACE.append(self)