# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter from the keyboard or initialize
# a string variable with the string

text = input("Please enter some text: ")

# vowels = "aeiouAEIOU"
# nonVowels = set()
#
# for char in text:
#     if char not in vowels:
#         nonVowels.add(char)
#
# sortedNonVowels = sorted(nonVowels)
# print(sortedNonVowels)

vowels = frozenset("aeiouAEIOU")
finalSet = set(text).difference(vowels)
sortedFinalList = sorted(finalSet)
print(", ".join(sortedFinalList))
