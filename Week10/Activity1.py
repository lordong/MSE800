# Activity 1: User Management System
# This program simulates a simple user management system with functionalities
# to create users, login, # forget passwords, and view user information.
# It uses bcrypt for secure password hashing.
import bcrypt   # Make sure to install bcrypt using: pip install bcrypt

# Make hash password
def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Check password
def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

# Simulated database, default user: admin/admin
DB_USERS = [
    {"username": "admin", "password": hash_password("admin"), "bod": "1980-01-01"},
]

# Create user
def create_user(username, password, bod):
    if any(user["username"] == username for user in DB_USERS):
        print("Username already exists.")
        return False
    hashed_password = hash_password(password)
    DB_USERS.append({"username": username, "password": hashed_password, "bod": bod})
    print("User created successfully.")
    return True

# Login user
def login_user(username, password):
    user = next((user for user in DB_USERS if user["username"] == username), None)
    if user and check_password(password, user["password"]):
        print("Login successful.")
        return True
    print("Invalid username or password.")
    return False

# Forget password
def forget_password(username, new_password):
    user = next((user for user in DB_USERS if user["username"] == username), None)
    if user:
        user["password"] = hash_password(new_password)
        print("Password reset successful.")
        return True
    print("Username not found.")
    return False

# View user
def view_user(username):
    user = next((user for user in DB_USERS if user["username"] == username), None)
    if user:
        print(f"Username: {user['username']}, Date of Birth: {user['bod']}")
        return True
    print("Username not found.")
    return False

# Main menu
def menu():
    print("\nWelcome to user management!")
    print("1. create user")
    print("2. login user")
    print("3. forget password")
    print("4. view user")
    print("0. exit")
    return input("Please select an option: ")

# Main function
def main():
    while True:
        option = menu()
        if option == "1":
            print("Creating user...")
            username = input("Enter username: ")
            password = input("Enter password: ")
            bod = input("Enter date of birth (YYYY-MM-DD): ")
            create_user(username, password, bod)
        elif option == "2":
            print("Logging in user...")
            username = input("Enter username: ")
            password = input("Enter password: ")
            login_user(username, password)
        elif option == "3":
            print("Forgetting password...")
            username = input("Enter username: ")
            new_password = input("Enter new password: ")
            forget_password(username, new_password)
        elif option == "4":
            print("Viewing user...")
            username = input("Enter username: ")
            view_user(username)
        elif option == "0":
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == '__main__':
    main()
