class Lightsaber:
    def __init__(self, color):
        self.force = None
        self.color = color

    def __str__(self):
        return "Lightsaber: {}, force {}".format(self.color, self.force)

    def force_side(self, color):
        if color == "czerwony":
            self.force = "dark"
        else:
            self.force = "light"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color in ("niebieski", "zielony", "fioletowy", "czerwony"):
            self._color = color
        else:
            raise ValueError("Bad lightsaber color")

l = Lightsaber("zielony")
print(l)
l1 = Lightsaber("czerwony")
print(l1)
#l2 = Lightsaber("blabla")
#print(l2)

# Tutaj nie wyświetla force, nie wiem co to właśność wirtualna - do nauki