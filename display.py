def display_password(password):
    """
    Display the generated password to the user.
    """
    print("\nGenerated Password: " + password)


def main():
    """
    Main function to control program execution flow.
    """
    print("========================================")
    print("PASSWORD GENERATOR")
    print("========================================")
    print()

    while True:
        # Step 1: Get validated password length
        length = get_password_length()
        print()

        # Step 2: Get user character preferences
        choices = get_user_choices()

        # Step 3: Generate the password
        password = generate_password(length, choices)

        # Step 4: Display the result
        display_password(password)

        # Step 5: Ask if user wants to generate another password
        print()
        again = input("Generate another password? (yes/no): ").strip().lower()
        while again not in ("yes", "y", "no", "n"):
            print("Please enter 'yes' or 'no'.")
            again = input("Generate another password? (yes/no): ").strip().lower()

        if again in ("no", "n"):
            print("\nThank you for using Password Generator!")
            break
        print()


if __name__ == "__main__":
    main()
