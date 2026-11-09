class Restaurant:
    """Model sederhana sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant serving {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open. Come on in!")


class IceCreamStand(Restaurant):
    """A specific kind of restaurant that sells ice cream."""

    def __init__(self, restaurant_name, cuisine_type="ice cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        """Display the flavors available."""
        print(f"\n{self.restaurant_name} has the following flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")


stand = IceCreamStand("Frosty's")
stand.flavors = ["vanilla", "chocolate", "strawberry", "choco mint"]
stand.describe_restaurant()
stand.show_flavors()