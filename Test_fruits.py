import price_info as price

def test_total():
    price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }
    quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 3}
    result = price.total_cost_shopping()
    assert (result == 46.75)

def test_cost():
    result = price.cost_of_fruits("orange",5)
    assert(result == 7.0)