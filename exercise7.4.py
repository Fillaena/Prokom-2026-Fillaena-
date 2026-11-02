questions = "\nEnter a pizza topping (or 'quit' to finish): "

while True:
    topping = input(questions)

    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")