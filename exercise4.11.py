pizzas = ['pepperoni', 'margherita', 'meat lovers']

friend_pizzas = pizzas[:]

pizzas.append('hawaiian')
friend_pizzas.append('tuna melt')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)