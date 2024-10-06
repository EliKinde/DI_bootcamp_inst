#Exercise 1 : What’s Your Name ?

def get_full_name(first_name, last_name, middle_name=None):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    if middle_name:
        middle_name = middle_name.capitalize()
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()
middle_name = input("Enter your middle name if there:" ).strip()

if not middle_name:
    middle_name = None

print(get_full_name(first_name, last_name, middle_name))

