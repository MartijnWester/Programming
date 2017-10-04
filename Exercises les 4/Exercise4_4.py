def new_password (oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        print("Your new password is acceptable")
        return True
    else:
        print("Choose a new password")
        return False

print(new_password('Woord12', 'Banaan'))