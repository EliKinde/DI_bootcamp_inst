#Exercise 7 : Faker Module
from faker import Faker

fake = Faker()

users = []

def add_user():
    name = fake.name()
    address = fake.address()
    language_code = fake.language_code()

    # Create a new user dictionary
    user = {
        'name': name,
        'address': address,
        'language_code': language_code
    }

    # Add the user dictionary to the users list
    users.append(user)

# Example usage:
for _ in range(5):
    add_user()

# Print out the users list to verify
for user in users:
    print(user)


