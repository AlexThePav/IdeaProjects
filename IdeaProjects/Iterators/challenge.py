# Create a list of items (you may use strings or numbers in the list),
# then create an iterator using the iter() function
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item
#
# hint: use the len() function rather than counting the number of items in the list.

listOfItems = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
n = len(listOfItems)
listIterator = iter(listOfItems)

for i in range(0, n):
    print(next(listIterator))
