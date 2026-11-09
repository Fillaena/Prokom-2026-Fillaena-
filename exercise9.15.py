from random import sample

pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

my_ticket = [3, 7, 'b', 'e']

attempts = 0
while True:
    attempts += 1
    winning_ticket = sample(pool, 4)
    if set(winning_ticket) == set(my_ticket):
        break

print(f"My ticket: {my_ticket}")
print(f"Winning ticket: {winning_ticket}")
print(f"It took {attempts} tries to win.")