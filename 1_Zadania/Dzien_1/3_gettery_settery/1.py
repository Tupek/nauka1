class Lightsaber:
    def __init__(self, color):
        self._color = color

    def __str__(self):
        if self._color in ("niebieski", "zielony", "fioletowy"):
            self.force = "jasna"
        elif self._color == "czerwony":
            self.force = "ciemna"
        return "Lightsaber: {}, force {}".format(self._color, self.force)

l = Lightsaber("zielony")
print(l)