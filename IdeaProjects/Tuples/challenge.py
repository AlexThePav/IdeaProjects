# Given the tuple below that represents the Imelda May track "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
    (1, "Pulling the Rug"),
    (2, "Psycho"),
    (3, "Mayhem"),
    (4, "Kentish Town Waltz")
)

title, artist, year, tracks = imelda
print("{}, {}, {}".format(title, artist, year))
for track in tracks:
    songNum, song = track
    print("\t", "{}, {}".format(songNum, song))
