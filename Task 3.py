import re

def assess_password_strength(password):
    # Initialize score and feedback messages
    score = 0
    feedback = []

    # Check for length (at least 8 characters)
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for presence of uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter (A-Z).")

    # Check for presence of lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter (a-z).")

    # Check for presence of digits
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one number (0-9).")

    # Check for presence of special characters
    if re.search(r'[\W_]', password):  
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !@#$%^&*).")

    # Determine password strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


# Main function to interact with the user
def password_strength_tool():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter a password to assess its strength: ")

    strength, feedback = assess_password_strength(password)

    # Display the strength result
    print(f"Password Strength: {strength}")
    
    # If feedback exists, provide it to the user
    if feedback:
        print("\nSuggestions for improvement:")
        for item in feedback:
            print(f"- {item}")
    else:
        print("Great! Your password meets all the recommended criteria.")

# Run the tool
password_strength_tool()
