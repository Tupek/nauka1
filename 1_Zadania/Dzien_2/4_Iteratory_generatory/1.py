import random

class Dice:
    dice_type = 0

    def __init__(self, dice_type):
        __dice_type = (3, 4, 6, 8, 10, 12, 20, 100)
        if dice_type in __dice_type:
            self.dice_type = dice_type
        else:
            raise ValueError ("Dozwolone: 3, 4, 6, 8, 10, 12, 20, 100)")

    def roll(self):
        return random.randint(1, self.dice_type)

    def roll_generator(self):
        for i in range(0, 10):
            yield self.roll()


d = Dice(6)
print(d.roll())

for i in d.roll_generator():
    print(i)