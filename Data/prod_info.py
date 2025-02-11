PROD_RECIPES = {
    'plank1' : {
        'inputs' : { # simple commodities
            "wood1" : 2,
            "LP_per_day" : 1
        },
        'minputs' : { # machine input name : how many times depreciate for this recipe
            "electric_saw" : 1
        },
        'outputs' : { # simple commodities
            "plank1" : 2
        },
        'time_required' : 2
    },
    'flour' : {
        'inputs' : { # simple commodities
            "LP_per_day" : 1
        },
        'minputs' : {
            'mill' : 1
        },
        'outputs' : { # simple commodities
            "flour100g" : 10
        },
        'time_required' : 2
    },
    'spaghetti' : {
        'inputs' : {
            "LP_per_day" : 1,
            "flour100g" : 10
        },
        'outputs' : {
            "spaghetti100g" : 10
        },
        'time_required' : 2
    }
}