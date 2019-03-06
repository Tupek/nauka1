class Lightsaber:
    def __init__(self, color):
        self.force = None
        self.color = color

    def __str__(self):
        return "Lightsaber: {}, force {}".format(self.color, self.force)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if color in ("niebieski", "zielony", "fioletowy", "czerwony"):
            if color == "czerwony":
                self.force = "ciemna"
            else:
                self.force = "jasna"
            self._color = color
        else:
            raise ValueError("Bad lightsaber color")

l = Lightsaber("zielony")
print(l)
l1 = Lightsaber("czerwony")
print(l1)
l2 = Lightsaber("blabla")
print(l2)