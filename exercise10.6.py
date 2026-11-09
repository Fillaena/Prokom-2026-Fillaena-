try:
    first_number = int(input("First Number: "))
    second_number = int(input("Second Number: "))
except ValueError:
    print("Sorry, you must enter a number, not text.")
else:
    print(f"The result: {first_number + second_number}")