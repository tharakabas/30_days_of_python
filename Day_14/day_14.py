# Sorting string into alphabetic order

my_str = input("Enter your Phrase here:")

words = my_str.split()

words.sort()

print("The sorted words are:")
for word in words:
   print(word)