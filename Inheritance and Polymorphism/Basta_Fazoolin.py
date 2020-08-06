class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {} Menu is available from {} to {}".format(self.name, self.start_time, self.end_time)

    def calcculate_bill(self, purchased_items):
        total = 0
        for item in purchased_items:
            total += self.items[item]
        return "Your total bill for {} is: €{}".format(self.name, total)


class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus


brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
, "11am", "4pm")
early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, "3pm", "6pm")
dinner = ("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 
'coffee': 2.00, 'espresso': 3.00,}, "5pm", "11pm")
kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11am", "9pm")

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])

print(brunch)
print(early_bird)
print(kids)
print(brunch.calcculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calcculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))