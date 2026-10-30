my_foods = ['pizza', 'soto', 'chicken wings']
friend_foods = my_foods[:]

my_foods.append('kwetiau')
friend_foods.append('martabak')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)