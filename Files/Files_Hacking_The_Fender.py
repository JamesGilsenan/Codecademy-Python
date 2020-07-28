import csv
import json

compromised_users = []
with open("passwords.csv") as password_file:
    password_csv = csv.DictReader(password_file)
    for password_row in password_csv:
        compromised_users.append(password_row["Username"])
    print(compromised_users)

with open("compromised_users", "w") as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user)

with open("boss_message.json", "w") as boss_message:
    boss_message_dict = {"recipient": "The Boss", "message": "Mission Success"}
    json.dump(boss_message_dict, boss_message)