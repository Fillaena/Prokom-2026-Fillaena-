def make_shirt(size, message):
    """Display a summary of the shirt that is going to be made."""
    print(f"The shirt size is {size} and the message is '{message}'.")


# Argumen posisional: urutan harus sama dengan parameter
make_shirt('small', 'Acne Studios STOCKHOLM 1996')

# Argumen keyword: urutan bebas, tapi nama harus sesuai
make_shirt(message='Acne Studios STOCKHOLM 1996', size='small')