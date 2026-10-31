current_users = ['Fillaena', 'yusrina', 'NISSA', 'Domi', 'berlin']
new_users = ['Yusrina', 'bipta', 'DOMI', 'putri', 'Alfa']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: username sudah dipakai, masukkan yang lain.")
    else:
        print(f"{new_user}: username tersedia.")