from Nile import get_distance, format_price, SHIPPING_PRICES
from Test import test_function

def calculate_shipping_cost(from_coords, to_coords, shipping_type):
    from_long, from_lat = from_coords
    to_long, to_lat = to_coords
    #distance = get_distance(*from_coords, *to_coords) also unpacks variables and works the same as line below
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    shipping_rate = SHIPPING_PRICES.get(shipping_type)
    price = distance * shipping_rate
    return format_price(price)



print(calculate_shipping_cost([50.8375054, 0.1762299], [53.5586526, 9.6476359], "Ground"))