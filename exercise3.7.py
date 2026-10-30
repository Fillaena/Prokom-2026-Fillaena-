guests = ['Fillaena Putri', 'Alfa Aulia', 'Yusrina Putri', 'Neysa Elmira', 'Keira Putri', 'Kinarsieh']

print("Sorry, the new table won't arrive in time. I can invite only two people for dinner.")

removed = guests.pop()
print(f"Dear {removed}, I'm sorry, I can't invite you to dinner.")
removed = guests.pop()
print(f"Dear {removed}, I'm sorry, I can't invite you to dinner.")
removed = guests.pop()
print(f"Dear {removed}, I'm sorry, I can't invite you to dinner.")
removed = guests.pop()
print(f"Dear {removed}, I'm sorry, I can't invite you to dinner.")

print(f"\nDear {guests[0]}, you are still invited to dinner.")
print(f"Dear {guests[1]}, you are still invited to dinner.")

del guests[1]
del guests[0]

print(guests)   