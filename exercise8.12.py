def make_sandwich(*items):
    """Print a summary of the sandwich being ordered."""
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"    - {item}")


make_sandwich('tuna')
make_sandwich('egg', 'cheese')
make_sandwich('chicken', 'lettuce', 'tomato', 'mayo')