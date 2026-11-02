# conditional test in the while
questions = "\nEnter a pizza topping (or 'quit' to finish): "
topping = ""

while topping != 'quit':
    topping = input(questions)

    if topping != 'quit':
        print(f"I'll add {topping} to your pizza.")
 
 #active variable       
questions = "\nEnter a pizza topping (or 'quit' to finish): "
active = True

while active:
    topping = input(questions)

    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping} to your pizza.")
 
# break statement       
questions = "\nEnter a pizza topping (or 'quit' to finish): "

while True:
    topping = input(questions)

    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")