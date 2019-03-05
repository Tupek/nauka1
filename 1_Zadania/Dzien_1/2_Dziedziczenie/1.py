class Dinosaur:

    def walk(self):
        return "Chodzę!"

    def make_sound(self):
        return "Roar!"

class Bird(Dinosaur):
    def fly(self):
        return 'Latam!'

    def make_sound(self):
        return "Ćwir ćwir!"


if __name__ == "__main__":
    d = Dinosaur()
    print("Dinozaur chodzi:")
    print(d.walk())

    print("Dinozaur wydaje dźwięk:")
    print(d.make_sound())

    b = Bird()
    print("Ptak lata:")
    print(b.fly())

    print("Ptak wydaje wydaje dźwięk:")
    print(b.make_sound())
