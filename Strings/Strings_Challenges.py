letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4