class Restaurant:
    """A simple model of a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0   

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a restaurant serving {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open. Come on in!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        self.number_served += increment


restaurant = Restaurant('Kimukatsu', 'Japanese')

print(f"Customers served: {restaurant.number_served}")

restaurant.number_served = 20
print(f"Customers served: {restaurant.number_served}")

restaurant.set_number_served(35)
print(f"Customers served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Customers served: {restaurant.number_served}")