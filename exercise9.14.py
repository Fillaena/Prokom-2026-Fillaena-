from random import sample

pool = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

winning_ticket = sample(pool, 4)

print(f"Any ticket matching these 4 numbers or letters wins a prize: {winning_ticket}")