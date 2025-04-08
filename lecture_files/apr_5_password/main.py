import bcrypt

my_password = "abc123!"

hashed_password = bcrypt.hashpw(my_password)
print(hashed_password)
