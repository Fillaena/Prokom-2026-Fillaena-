from exercise9_12_moduluser import User


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