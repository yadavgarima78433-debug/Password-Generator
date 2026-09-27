def generate_password(length, choices):
    """
    Generate a random password of given length using the selected character types.
    """
    # Verify parameter type using type() function and identity operator
    if type(length) is not int:
        length = int(length)

    # Build character pool based on user choices
    character_pool = ""

    if choices["uppercase"]:
        character_pool += string.ascii_uppercase

    if choices["lowercase"]:
        character_pool += string.ascii_lowercase

    if choices["numbers"]:
        character_pool += string.digits

    if choices["special"]:
        # Standard special punctuation characters
        character_pool += string.punctuation

    # Convert character pool string into a list
    character_list = list(character_pool)

    # Randomly select characters until desired length is reached
    password_chars = []
    for _ in range(length):
        random_char = random.choice(character_list)
        password_chars.append(random_char)

    # Join list of characters into a single string
    password = "".join(password_chars)
    return password

