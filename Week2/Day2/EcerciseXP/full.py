def get_full_name(first_name, last_name, middle_name=None):
    """Returns the full name formatted with optional middle name, with proper capitalization."""
    # Capitalize the first letter of each part of the name
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    if middle_name:
        middle_name = middle_name.capitalize()
        return f"{first_name} {middle_name} {last_name}"
    else:
        return f"{first_name} {last_name}"

def main():
    """Main function to handle user input and display the full name."""
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    middle_name = input("Enter your middle name (or press Enter to skip): ").strip()

    # If the middle name is an empty string, set it to None
    if not middle_name:
        middle_name = None

    full_name = get_full_name(first_name, last_name, middle_name)
    print(f"Full name: {full_name}")

if __name__ == "__main__":
    main()

