class User:
    """A simple model of a user profile."""

    def __init__(self, first_name, last_name, age, city, email):
        """Store the user's profile information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"Name  : {self.first_name} {self.last_name}")
        print(f"Age   : {self.age}")
        print(f"City  : {self.city}")
        print(f"Email : {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")


user_1 = User('Fillaena', 'Bipta', 19, 'New York', 'fillaena@gmail.com')
user_2 = User('Alfa', 'Nurochman', 19, 'Tokyo', 'alfa@gmail.com')
user_3 = User('Maekky', 'Cavalera', 18, 'Edinburgh', 'cavalera@gamil.com')

user_1.describe_user()
user_1.greet_user()
print()

user_2.describe_user()
user_2.greet_user()
print()

user_3.describe_user()
user_3.greet_user()
print()
