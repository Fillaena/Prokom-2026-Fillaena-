from exercise9_12_moduladmin import Admin

admin = Admin('Fillaena', 'Bipta', 19, 'New York', 'fillaena@gmail.com')

admin.describe_user()
admin.greet_user()
print()
admin.privileges.show_privileges()