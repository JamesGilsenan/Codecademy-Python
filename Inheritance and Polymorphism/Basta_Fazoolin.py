class Franchise():
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def available_menus(self, time):
        available_menus = []
        for menu in self.menus:
            if time >= menu.start_time:
                available_menus.append(menu)
        return available_menus


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
            if item in self.items:
                total += self.items[item]
        return "Your total bill for {} is: €{}".format(self.name, total)


brunch = Menu("Brunch", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
, 1100, 1600)
early_bird = Menu("Early Bird", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, 1500, 1800)
dinner = Menu("Dinner", {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 
'coffee': 2.00, 'espresso': 3.00,}, 1700, 2300)
kids = Menu("Kids", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, 1100, 2100)
menus = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

#print(brunch)
#print(early_bird)
#print(kids)
#print(brunch.calcculate_bill(["pancakes", "home fries", "coffee"]))
#print(early_bird.calcculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

print(flagship_store)
print(flagship_store.available_menus(1200))