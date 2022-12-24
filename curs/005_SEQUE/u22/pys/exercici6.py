def conv_anglesi(text):
  say = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    # Create the pig latin word and add it to the list
    say = say + word[1:len(word)] + word[0] + "ay "
    # Turn the list back into a phrase
  return say
print(conv_anglesi("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(conv_anglesi("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"