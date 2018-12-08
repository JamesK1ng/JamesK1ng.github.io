#Assignment24

usernouns = (input("Enter nouns:"))
words = usernouns.split(" ")
wordnum = words.count("z ")
plurals = usernouns.count("s ")

frac = wordnum / plurals

print("Number of Words: ", wordnum)
print("Fraction of your list that is plural is: " , frac)


