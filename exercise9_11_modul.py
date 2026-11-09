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


class Privileges:
    """A class to store an administrator's privileges."""

    def __init__(self, privileges=None):
        """Initialize the list of privileges."""
        if privileges is None:
            privileges = [
                'can add post',
                'can delete post',
                'can ban user',
            ]
        self.privileges = privileges

    def show_privileges(self):
        """List the administrator's set of privileges."""
        print("Administrator privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")


class Admin(User):
    """A special kind of user with administrative privileges."""

    def __init__(self, first_name, last_name, age, city, email):
        """Initialize the user attributes, then add a Privileges instance."""
        super().__init__(first_name, last_name, age, city, email)
        self.privileges = Privileges()