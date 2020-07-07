premium_ground_shipping = 125

def ground_shipping_cost(weight):
    flat_charge = 20
    if weight >= 10:
        shipping_cost = (4.75 * weight) + flat_charge
    elif weight >= 6:
        shipping_cost = (4 * weight) + flat_charge
    elif weight >= 2:
        shipping_cost = (3 * weight) + flat_charge
    else:
        shipping_cost = (1.5 * weight) + flat_charge
    return shipping_cost

def drone_shipping_cost(weight):
    if weight >= 10:
        cost_by_drone = (14.25 * weight)
    elif weight >= 6:
        cost_by_drone = (12 * weight)
    elif weight >= 2:
        cost_by_drone = (9 * weight)
    else:
        cost_by_drone = (4.5 * weight)
    return cost_by_drone

def best_shipping_method(weight):
    cost_by_drone = drone_shipping_cost(weight)
    cost_by_ground = ground_shipping_cost(weight)
    if premium_ground_shipping < cost_by_ground and premium_ground_shipping < cost_by_drone:
        print("The cheapest shipping method is Premium Shipping")
        print("Cost of shipping: €" + str(premium_ground_shipping))
    elif cost_by_ground < premium_ground_shipping and cost_by_ground < cost_by_drone:
        print("The cheapest shipping method is Ground Shipping")
        print("Cost of shipping: €" + str(cost_by_ground))
    else:
        print("The cheapest shipping method is Drone Shipping")
        print("Cost of shipping: €" + str(drone_shipping_cost))

package_weight = input("Please enter the weight of your package in pounds ")

print(ground_shipping_cost(float(package_weight)))
print(drone_shipping_cost(float(package_weight)))
best_shipping_method(float(package_weight))