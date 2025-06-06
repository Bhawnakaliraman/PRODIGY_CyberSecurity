import re

def check_password_strength(password):
    strength = 0
    remarks = ""

    # Criteria checks
    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[\W_]", password):  # Special characters
        strength += 1

    # Feedback based on score
    if strength <= 2:
        remarks = "Weak Password ❌"
    elif strength == 3 or strength == 4:
        remarks = "Moderate Password ⚠️"
    else:
        remarks = "Strong Password ✅"

    return remarks

# Main
if __name__ == "__main__":
    print("🔐 Password Complexity Checker 🔐")
    user_password = input("Enter a password to check its strength: ")
    result = check_password_strength(user_password)
    print("\nResult:", result)
