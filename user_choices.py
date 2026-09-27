def get_user_choices():
    """
    Prompt user for character preferences (uppercase, lowercase, numbers, special characters).
    Validates that user chooses at least one character type.
    Returns choices stored in a dictionary.
    """
    # Tuple of acceptable answers
    valid_yes = ("yes", "y")
    valid_no = ("no", "n")

    while True:
        # Uppercase choice
        upper_input = input("Include uppercase letters? (yes/no): ").strip().lower()
        while upper_input not in valid_yes and upper_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            upper_input = input("Include uppercase letters? (yes/no): ").strip().lower()

        # Lowercase choice
        lower_input = input("Include lowercase letters? (yes/no): ").strip().lower()
        while lower_input not in valid_yes and lower_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            lower_input = input("Include lowercase letters? (yes/no): ").strip().lower()

        # Numbers choice
        num_input = input("Include numbers? (yes/no): ").strip().lower()
        while num_input not in valid_yes and num_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            num_input = input("Include numbers? (yes/no): ").strip().lower()

        # Special characters choice
        special_input = input("Include special characters? (yes/no): ").strip().lower()
        while special_input not in valid_yes and special_input not in valid_no:
            print("Please enter 'yes' or 'no'.")
            special_input = input("Include special characters? (yes/no): ").strip().lower()

        # Convert responses to booleans
        include_upper = upper_input in valid_yes
        include_lower = lower_input in valid_yes
        include_numbers = num_input in valid_yes
        include_special = special_input in valid_yes

        # Logical check: at least one character type must be selected
        if include_upper or include_lower or include_numbers or include_special:
            # Store choices in a dictionary
            choices = {
                "uppercase": include_upper,
                "lowercase": include_lower,
                "numbers": include_numbers,
                "special": include_special
            }
            return choices
        else:
            print("\nError: You must select at least one character type! Please try again.\n")
