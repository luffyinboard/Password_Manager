import pandas as pd
import string
import random
import hashlib

file_path = "user_credentials.csv"

# This will return a password with a mix of ASCII characters, numbers, and special characters
def password_Gen():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    special_char = ['#', '%', '$', '_', '=', '@']
    temppassword = letters + numbers + special_char
    password = ""
    for _ in range(15):
        password += random.choice(temppassword)
    return password

# Create an empty DataFrame with columns for username and password
def create_csv():
    df = pd.DataFrame(columns=['username', 'password'])
    return df

# Add users and passwords to the DataFrame and save to a CSV
def add_password():
    df = create_csv()
    while True:
        user = input("Enter the Username: ")
        pwd = input("Enter the Password (or leave blank to auto-generate): ")

        # If the password is left blank, generate one
        if not pwd:
            pwd = password_Gen()
            print(f"Generated password for {user}: {pwd}")

        # Create a new row as a DataFrame
        new_row = pd.DataFrame({'username': [user], 'password': [pwd]})

        # Use pd.concat() to append the new row to the DataFrame
        df = pd.concat([df, new_row], ignore_index=True)

        # Ask if the user wants to add another entry
        add_more = input("Do you want to add another user? (yes/no): ").strip().lower()
        if add_more != 'yes':
            break

    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"CSV file saved successfully at {file_path}")



def read_password(username):
    try:
        # Read the CSV file into a DataFrame
        file = pd.read_csv(file_path)
        
        # Check if the DataFrame is empty
        if file.empty:
            print("The file is empty; nothing to read.")
            exit(-1)

        # Check if the username exists in the DataFrame (case-sensitive)
        if username in file["username"].values:
            # Retrieve the password associated with the username
            password = file.loc[file["username"] == username, "password"].values[0]
            print("The password is -> ", password)
        else:
            print("No such username exists.")
            exit(99)
    
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
        exit(1)
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
        exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        exit(1)

def code_execution():
    answer = input("You can add/read passwords:")
    if answer == "read":
        user = input("Type the username to look for, example: 'google.com' :")
        read_password(user)
    elif answer == "add":
        add_password()
    else:
        print("Bruh Type the read or add only :( \n")
        exit(-1)



if __name__ == "__main__":
    print("WELCOME TO PASSWORD MANAGER")
    print("REMEMBER THIS MANAGER IS CASE-SENSITIVE")
    print("SO BE CAREFUL WHEN YOU TYPE")
    print(r"""
                                            ooo,    .---.
        o`  o   /    |\________________
        o`   'oooo()  | ________   _   _)
        `oo   o` \    |/        | | | |
        `ooo'   `---'         "-" |_|
                    """)



    code_execution()
