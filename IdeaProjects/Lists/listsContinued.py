# list_1 = []
# list_2 = list()
#
# print("List 1: {}".format(list_1))
# print("List 2: {}".format(list_2))
#
# if list_1 == list_2:
#     print("The lists are equal")
#
# print(list("The lists are equal"))

even = [2, 4, 6, 8]

# another_even = even
# another_even = list(even)
another_even = sorted(even, reverse=True)
print(another_even is even)

another_even.sort(reverse=True)
print(even)
print(another_even)