from enemy import Troll, Vampyre

ugly_troll = Troll("Pug")
print("Ugly troll - {}".format(ugly_troll))

another_troll = Troll("Ug")
print("Another troll - {}".format(another_troll))

brother = Troll("Urg")
print(brother)

vlad = Vampyre("Vlad")
print(vlad)

ugly_troll.grunt()
another_troll.grunt()
brother.grunt()
brother.take_damage(2)

print("=" * 40)
another_troll.take_damage(30)
print(another_troll)

while vlad.alive:
    vlad.take_damage(1)
    print(vlad)
