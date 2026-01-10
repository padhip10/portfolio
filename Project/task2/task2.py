import random

# Ask the user to enter their password
password = input("Enter your password: ")

# Check if the password is long enough
if len(password) < 9:
    print("Password too short.")
    exit()  # Exit the program if password is too short

# If password is long enough, proceed to security checks
# We will randomly pick 3 positions to verify
# Note: positions shown to user are 1-indexed (human-friendly), but Python uses 0-indexing
positions_to_check = random.sample(range(len(password)), 3)

for pos in positions_to_check:
    # Ask the user for the character at the given position
    user_input = input(f"Enter letter at position {pos + 1}: ")
    
    if user_input == password[pos]:
        print("Correct")
    else:
        print("Security check failed.")
        exit()  # Exit immediately if the letter is incorrect

# If all letters were correct
print("Security check passed.")
