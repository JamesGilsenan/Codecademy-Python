gamers = []

def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)
    return gamers_list

kimberly = {"name": "Kimberly Warner", "availability": ["Mondays", "Tuesdays", "Firdays"]}
print(add_gamer(kimberly, gamers))