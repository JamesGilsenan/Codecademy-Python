class Menu:
    
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self):
        return "The {} is available from {} to {}".format(self.name, self.start_time, self.end_time)

brunch = Menu("Brunch Menu", {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}
, "11am", "4pm")
early_bird = Menu("Early Bird Menu", {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 
'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}, "3pm", "6pm")
kids = Menu("Kids Menu", {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}, "11am", "9pm")

print(brunch)
print(early_bird)
print(kids)