letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques

def count_char_x(word, x):
  count_x = 0
  for i in range(len(word)):
    if word[i] == x:
      count_x += 1
  return count_x

def count_multi_char_x(word, x):
  splits = word.split(x)
  return(len(splits)-1)

def substring_between_letters(word, start, end):
  if start in word and end in word:
    start_index = word.find(start)
    end_index = word.find(end)
    return word[start_index + 1: end_index]
  else:
    return word

def x_length_words(sentence, x):
  words = sentence.split()
  print(words)
  for word in words:
    if len(word) >= x:
      return True
    else:
      return False

def check_for_name(sentence, name):
  words = sentence.split()
  print(words)
  for word in words:
    if name.upper() in sentence.upper() or name.lower() in sentence.lower():
      return True
    else:
      return False

def every_other_letter(word):
  every_other = ""
  for i in range(0, len(word), 2):
    every_other += word[i]
  return every_other

def reverse_string(word):
  word_reversed = ""
  for i in range(len(word)):
    word_reversed += word[len(word) - i - 1]
  return word_reversed

def make_spoonerism(word1, word2):
  char1 = word1[0]
  char2 = word2[0]
  word1 = word1.replace(word1[0], char2)
  word2 = word2.replace(word2[0], char1)
  spoonerism = word1 + " " + word2
  return spoonerism

def add_exclamation(word):
  if len(word) >= 20:
    return word
  else:
    while len(word) < 20:
      word += "!"
  return word

#print(unique_english_letters("mississippi"))
# should print 4
#print(unique_english_letters("Apple"))
# should print 4

#print(count_char_x("mississippi", "s"))
# should print 4
#print(count_char_x("mississippi", "m"))
# should print 1

#print(count_multi_char_x("mississippi", "iss"))
# should print 2
#print(count_multi_char_x("apple", "pp"))
# should print 1

#print(substring_between_letters("apple", "p", "e"))
# should print "pl"
#print(substring_between_letters("apple", "p", "c"))
# should print "apple"

#print(x_length_words("i like apples", 2))
# should print False
#print(x_length_words("he likes apples", 2))
# should print True

#print(check_for_name("My name is Jamie", "Jamie"))
# should print True
#print(check_for_name("My name is jamie", "Jamie"))
# should print True
#print(check_for_name("My name is Samantha", "Jamie"))
# should print False

#print(every_other_letter("Codecademy"))
# should print Cdcdm
#print(every_other_letter("Hello world!"))
# should print Hlowrd
#print(every_other_letter(""))
# should print 

#print(reverse_string("Codecademy"))
# should print ymedacedoC
#print(reverse_string("Hello world!"))
# should print !dlrow olleH
#print(reverse_string(""))
# should print

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a