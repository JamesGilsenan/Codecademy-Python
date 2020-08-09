from Nile import get_distance, format_price, SHIPPING_PRICES
from Test import test_function
from Test import Driver

def calculate_shipping_cost(from_coords, to_coords, shipping_type="Overnight"):
    from_long, from_lat = from_coords
    to_long, to_lat = to_coords
    #distance = get_distance(*from_coords, *to_coords) also unpacks variables and works the same as line below
    distance = get_distance(from_lat, from_long, to_lat, to_long)
    shipping_rate = SHIPPING_PRICES.get(shipping_type)
    price = distance * shipping_rate
    return format_price(price)

def calculate_driver_cost(distance, *drivers):
    cheapest_driver = None
    cheapest_driver_price = None
    for driver in drivers:
        driver_time = driver.speed * distance
        price_for_driver = driver.salary * driver_time
        if cheapest_driver is None:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
        elif price_for_driver < cheapest_driver_price:
            cheapest_driver = driver
            cheapest_driver_price = price_for_driver
    return cheapest_driver_price, cheapest_driver


#print(calculate_shipping_cost([50.8375054, 0.1762299], [53.5586526, 9.6476359], "Ground"))
test_function(calculate_shipping_cost)
driver1 = Driver(2, 10)
driver2 = Driver(7, 20)
driver3 = Driver(5, 18)
print(calculate_driver_cost(100, driver1, driver2, driver3))
test_function(calculate_driver_cost)