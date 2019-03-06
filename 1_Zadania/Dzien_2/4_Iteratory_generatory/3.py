def gen():
    m = """Wlazł kotek na płotek
i mruga,
ładna to piosenka,
nie długa.
Nie długa, nie krótka,
lecz w sam raz,
zaśpiewaj koteczku,
jeszcze raz."""
    m = m.splitlines()
    for i in m:
        yield i

for i in gen():
    print (i)
    