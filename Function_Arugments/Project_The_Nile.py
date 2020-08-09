from Nile import get_distance, format_price, SHIPPING_PRICES
from Test import test_function

def calculate_shipping_cost(from_coords, to_coords, shipping_type):
    from_long, from_lat = from_coords
    to_long, to_lat = to_coords
    #distance = get_distance(*from_coords, *to_coords) also unpacks variables and works the same as line below
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    print(distance)



calculate_shipping_cost([1.147865, 4.578456], [1.56843, 2.84384], "Steam")