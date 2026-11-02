def make_shirt(size='large', message='I love Python'):
    """Display a summary of the shirt that is going to be made."""
    print(f"The shirt size is {size} and the message is '{message}'.")


# Large dengan pesan default
make_shirt()

# Medium dengan pesan default
make_shirt('medium')

# Ukuran apa saja dengan pesan berbeda
make_shirt('small', 'Acne Studios STOCKHOLM 1996')