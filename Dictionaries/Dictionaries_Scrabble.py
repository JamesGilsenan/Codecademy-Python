letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def score_word(word, dictionary):
    score = 0
    word = word.upper()
    for letter in word:
        score += dictionary[letter]
        #print("Letter: " + letter + " = " + str(dictionary[letter]) + " points")
    #print("Word: " + word + " = " + str(score) + " points")
    return score

letter_to_points = {key:value for key, value in zip(letters, points)}
letter_to_points[" "] = 0
print(letter_to_points)
print(score_word("hello", letter_to_points))