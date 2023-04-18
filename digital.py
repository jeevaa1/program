# Initialize an empty dictionary to store the terms and their meanings
dictionary = {}

# Define a function to add a term and its meaning to the dictionary
def add_term():
    term = input("Enter the term to add: ")
    meaning = input("Enter the meaning: ")
    dictionary[term] = meaning
    print(f"Term '{term}' added to the dictionary with meaning '{meaning}'.")

# Define a function to search for a term in the dictionary
def search_term():
    term = input("Enter the term to search for: ")
    if term in dictionary:
        print(f"Meaning of '{term}': {dictionary[term]}")
    else:
        print(f"Term '{term}' not found in the dictionary.")

# Define a function to display all the terms and their meanings in the dictionary
def display_terms():
    if len(dictionary) == 0:
        print("Dictionary is empty.")
    else:
        print("---- Dictionary ----")
        for term, meaning in sorted(dictionary.items()):
            print(f"{term}: {meaning}")
        print("--------------------")

# Define a function to remove a term from the dictionary
def remove_term():
    term = input("Enter the term to remove: ")
    if term in dictionary:
        del dictionary[term]
        print(f"Term '{term}' removed from the dictionary.")
    else:
        print(f"Term '{term}' not found in the dictionary.")

# Define a function to display the main menu and prompt the user to choose an option
def main_menu():
    print("----- Digital Dictionary -----")
    print("1. Add Term")
    print("2. Search Term")
    print("3. Display All Terms")
    print("4. Remove Term")
    print("0. Exit")
    choice = input("Enter your choice: ")
    return choice

# Define the main program loop
while True:
    choice = main_menu()
    if choice == "1":
        add_term()
    elif choice == "2":
        search_term()
    elif choice == "3":
        display_terms()
    elif choice == "4":
        remove_term()
    elif choice == "0":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
