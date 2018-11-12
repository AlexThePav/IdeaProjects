from player import Player

pav = Player("Pav")

print(pav.name)
print(pav.lives)
pav.lives -= 1
print(pav)

pav.lives -= 1
print(pav)

pav.lives -= 1
print(pav)

pav.level += 3
print(pav)

pav.level -= 1
print(pav)

pav.level -= 1
print(pav)

pav.level -= 1
print(pav)

pav.level -= 1
print(pav)
