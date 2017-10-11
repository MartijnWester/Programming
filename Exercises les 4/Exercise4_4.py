def new_password (oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6:
        print("Your new password is acceptable")
        return True
    else:
        print("Unacceptable, choose a new password")
        return False

print(new_password(input("Enter your old password here: "), input("Enter your new password here: ")))