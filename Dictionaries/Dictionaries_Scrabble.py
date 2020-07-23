letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def score_word(word, dictionary):
    score = 0
    word = word.upper()
    for letter in word:
        score += dictionary.get(letter, 0)
        #print("Letter: " + letter + " = " + str(dictionary.get(letter, 0)) + " points")
    #print("Word: " + word + " = " + str(score) + " points")
    return score

def play_word(player, word):
    word.upper()
    player_to_words[player].append(word)


letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
print(letter_to_points)
brownie_points = score_word("brownie", letter_to_points)
print(brownie_points)

player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"], "wordNerd": ["EARTH", "EYES", "MACHINE"],
 "Lexi Con": ["ERASER", "BELLY", "HUSKY"], "Prof Reader": ["ZAP", "COMA", "PERIOD"]}
player_to_points = {}

for player, words in player_to_words.items():
    player_points = 0
    for word in words:
        player_points += score_word(word, letter_to_points)
    player_to_points[player] = player_points

print(player_to_points)
play_word("wordNerd", "brownie")
print(player_to_words)