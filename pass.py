import string
import random
import pyperclip

def get_strength_label(length):
    if length <= 4:
        return "🔴 Very Weak"
    elif length <= 7:
        return "🟠 Weak"
    elif length <= 10:
        return "🟡 Moderate"
    elif length <= 13:
        return "🟢 Strong"
    else:
        return "✅ Very Strong"

def generate_password(length, use_digits=True, use_lower=True, use_upper=True, use_symbols=True):
    char_pool = ''
    if use_digits:
        char_pool += string.digits
    if use_lower:
        char_pool += string.ascii_lowercase
    if use_upper:
        char_pool += string.ascii_uppercase
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        return "Error: No character types selected."

    # Guarantee one character from each selected set
    password = []
    if use_digits: password.append(random.choice(string.digits))
    if use_lower: password.append(random.choice(string.ascii_lowercase))
    if use_upper: password.append(random.choice(string.ascii_uppercase))
    if use_symbols: password.append(random.choice(string.punctuation))

    if length < len(password):
        return f"Error: Length must be at least {len(password)} to include all selected character types."

    # Fill the rest
    while len(password) < length:
        password.append(random.choice(char_pool))

    random.shuffle(password)
    return ''.join(password)

# CLI Interaction
print("🔐 Password Generator Tool 🔐")
length = int(input("Enter password length: "))
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_symbols = input("Include special characters? (y/n): ").lower() == 'y'

result = generate_password(length, use_digits, use_lower, use_upper, use_symbols)
strength = get_strength_label(length)
print(f"\n✅ Generated Password:\n{result}")
print(f"🔐 Strength: {strength}")

# Save to File
save_file = input("\n💾 Save password to file? (y/n): ").lower() == 'y'
if save_file:
    filename = input("Enter filename (e.g., mypass.txt): ")
    try:
        with open(filename, 'w') as f:
            f.write(result + '\n')
        print(f"✅ Password saved to '{filename}'")
    except Exception as e:
        print("❌ Error saving file:", e)

# Copy to Clipboard
copy_clip = input("\n📋 Copy password to clipboard? (y/n): ").lower() == 'y'
if copy_clip:
    try:
        pyperclip.copy(result)
        print("✅ Password copied to clipboard!")
    except Exception as e:
        print("❌ Clipboard error:", e)