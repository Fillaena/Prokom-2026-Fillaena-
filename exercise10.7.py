print("Ketik 'q' kapan saja untuk keluar.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break

    second_number = input("Second number: ")
    if second_number == 'q':
        break

    try:
        total = int(first_number) + int(second_number)
    except ValueError:
        print("Sorry, you must enter a number, not text.")
    else:
        print(f"The result: {total}")