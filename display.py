from Data import all_citizens, CURRENT_MARKETPLACE

# display functions in UI
def display_current_citizens_ui():
    citizens_info = ""
    citizens_info += "\n___________________________________________________"
    for a in all_citizens:
        citizens_info += f'\n\n> Citiizen {a.name}\n{a}\n'
        if a.profession:
            citizens_info += f"Profession: {a.profession}\n"
        for x, y in a.commodities.items():
            citizens_info += (f"\n- {x} {y}")
        citizens_info += "\n"
    citizens_info += "\n___________________________________________________"
            

    return citizens_info

def display_current_marketplace_ui():
    marketplace_info = ""
    marketplace_info += "\n_______________________________________________________________________________________"
    for a in CURRENT_MARKETPLACE:
        marketplace_info += f"\n{a.quantity} - ${a.offer_price_perUnit}: {a.quality} - {a.seller} | {a.seller.name}"
    marketplace_info += "\n_______________________________________________________________________________________"

    return marketplace_info


def display_all_current_info_ui(what_to_display = "all"):
    all_current_info = ""
    if what_to_display == "all" or "commodities":
        if all_citizens:
            all_current_info += display_current_citizens_ui()
    if what_to_display == "all" or "current marketplace": 
        if CURRENT_MARKETPLACE:
            all_current_info += display_current_marketplace_ui()

    return all_current_info


# display functions
#def display_current_info(what_to_display = "all"):
#    if what_to_display == "all" or "commodities":
#        print("\n___________________________________________________________________________")
#        for a in all_citizens:
#           print(f'\n\n> Citiizen {a.name}\n{a}\n')
#           for x, y in a.commodities.items():
#               print("-" + x, y)
#       print("___________________________________________________________________________")
#   if what_to_display == "all" or "current marketplace":  
#        print("\n___________________________________________________________________________")
#        for a in CURRENT_MARKETPLACE:
#            print(f"\n{a.quantity}  - ${a.offer_price_perUnit}/unit : {a.quality} - {a.seller} | {a.seller.name}")
#       print("___________________________________________________________________________")