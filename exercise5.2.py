# Kesamaan dan ketidaksamaan string
car = 'ferrari'
print("car == 'ferrari':", car == 'ferrari')    # True
print("car == 'mercedes':", car == 'mercedes')  # False
print("car != 'mercedes':", car != 'mercedes')          # True
print("car != 'ferrari':", car != 'ferrari')      # False

# Lower()
name = 'fillaena'
print("name.lower() == 'fillaena':", name.lower() == 'fillaena')    # True
print("name.lower() == 'Fillaena':", name.lower() == 'Fillaena')    # False

# Numerik Test
age = 19
print("age == 19:", age == 19)    # True
print("age == 20:", age == 20)    # False
print("age != 20:", age != 20)    # True
print("age != 19:", age != 19)    # False
print("age > 18:", age > 18)      # True
print("age > 19:", age > 19)      # False
print("age < 20:", age < 20)      # True
print("age < 19:", age < 19)      # False
print("age >= 19:", age >= 19)    # True
print("age >= 20:", age >= 20)    # False
print("age <= 19:", age <= 19)    # True
print("age <= 18:", age <= 18)    # False

print("age >= 17 and age <= 25:", age >= 17 and age <= 25)    # True
print("age > 20 and age < 30:", age > 20 and age < 30)        # False
print("age < 10 or age > 15:", age < 10 or age > 15)          # True
print("age < 10 or age > 30:", age < 10 or age > 30)          # False

# Item di dalam list / tidak di dalam list
pizzas = ['pepperoni', 'margherita', 'meat lovers']
print("'pepperoni' in pizzas:", 'pepperoni' in pizzas)            # True
print("'tuna melt' in pizzas:", 'tuna melt' in pizzas)            # False
print("'tuna melt' not in pizzas:", 'tuna melt' not in pizzas)    # True
print("'pepperoni' not in pizzas:", 'pepperoni' not in pizzas)    # False