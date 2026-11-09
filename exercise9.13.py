from random import randint


class Die:

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        print(randint(1, self.sides), end=' ')


d6 = Die()
d10 = Die(10)
d20 = Die(20)

for die in (d6, d10, d20):
    print(f"Rolling a {die.sides}-sided die 10 times:")
    for _ in range(10):
        die.roll_die()
    print("\n")