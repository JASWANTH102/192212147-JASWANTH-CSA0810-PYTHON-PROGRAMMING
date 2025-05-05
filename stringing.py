# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Function to count characters in a string
def count_characters(s):
    return len(s)

# Function to replace a character in a string
def replace_characters(s, old_char, new_char):
    return s.replace(old_char, new_char)

# Main menu
print("1. Reverse String")
print("2. Count Characters")
print("3. Replace Characters")
choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    text = input("Enter a string: ")
    print("Reversed String:", reverse_string(text))

elif choice == 2:
    text = input("Enter a string: ")
    print("Total Characters:", count_characters(text))

elif choice == 3:
    text = input("Enter a string: ")
    old = input("Enter character to replace: ")
    new = input("Enter new character: ")
    print("Updated String:", replace_characters(text, old, new))

else:
    print("Invalid choice.")
