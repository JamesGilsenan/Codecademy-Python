gamers = []

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer missing critical information")

def build_daily_frequency_table():
    frequency_table = {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0,}
    return frequency_table

def calculate_availability(gamers_list, availability_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            availability_frequency[day] += 1
    return availability_frequency

def find_best_night(availability_table):
    best_availability = float("-inf")
    availability_table
    for day, availability in availability_table.items():
        if availability > best_availability:
            best_availability = availability
            best_day = day
    return best_day



kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
(add_gamer(kimberly, gamers))
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)
#print(gamers)

count_availability = build_daily_frequency_table()
count_availability = calculate_availability(gamers, count_availability)
print(count_availability)

print(find_best_night(count_availability))