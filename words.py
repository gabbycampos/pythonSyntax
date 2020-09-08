def print_upper_words(string):
  """ Will print words in uppercase """
  for char in string:
    print(char.upper())
print(print_upper_words(['I', 'am', 'a', 'list']))


def only_letter_e(words):
  """ Will only print words that start with 'e' """
  for word in words:
    if word.startswith('e') or word.startswith('E'):
      print(word)
print(only_letter_e(['elephant', 'eyes', 'Ears', 'face']))


# this should print "HELLO", "HEY", "YO", and "YES"
# print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
#                   must_start_with={"h", "y"})

def only_these_words(words, must_start_with):
  for word in words:
    for char in must_start_with:
      if word.startswith(char):
          print(word.upper())
print(only_these_words(['hello', 'this', 'is', 'fun'], must_start_with={'h'}))