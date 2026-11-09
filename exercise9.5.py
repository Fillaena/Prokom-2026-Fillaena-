class User:
    """A simple model of a user profile."""

    def __init__(self, first_name, last_name, age, city, email):
        """Store the user's profile information."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.email = email
        self.login_attempts = 0   

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"Name  : {self.first_name} {self.last_name}")
        print(f"Age   : {self.age}")
        print(f"City  : {self.city}")
        print(f"Email : {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back.")

    def increment_login_attempts(self):
        """Increase the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0


user = User('Fillaena', 'Bipta', 18, 'New York', 'fillaena@gmail.com')

# increment several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"Login attempts: {user.login_attempts}")

# reset and check again
user.reset_login_attempts()
print(f"Login attempts: {user.login_attempts}")