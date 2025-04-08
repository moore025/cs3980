from hash_pass import HashPassword


hash_password = HashPassword()

my_password = "abc123456!"

hashed_pass = hash_password.create_hash(my_password)
print(hashed_pass)

not_good_case = hash_password.create_hash_with_salt(my_password, "a" * 21 + "e")
print(not_good_case)

match = hash_password.verify_hash(my_password, hashed_pass)
print(match)
# True
