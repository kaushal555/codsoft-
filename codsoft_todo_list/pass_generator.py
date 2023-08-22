import random

def generate_password(num_words):
    # List of common words (you can customize this list)
    word_list = [
        "apple", "banana", "123", "dog", "elephant",
        "65a", "guitar", "my", "island", "jazz",
        "kangaroo", "54", "gfg", "night", "ocean",
        "piano", "@", "rainbow", "#", "tiger",
        "u19", "violet", "#12", "98", "yellow",
        "zebra"
    ]

    # Generate the password
    password_words = random.sample(word_list, num_words)
    password = ''.join(word.capitalize() for word in password_words)

    return password

# Get user input
try:
    num_words = int(input("Enter the number of words for the password: "))
    if num_words <= 0:
        raise ValueError("Number of words must be a positive integer.")
    
    generated_password = generate_password(num_words)
    print("Generated Password:", generated_password)

except ValueError as e:
    print("Error:", e)
