#HW5_task4
import os

#decorator to work with incorrect input
def input_error(func):
    def inner(args, contacts):
        try:
            return func(args, contacts)

        except ValueError:
            return "Number of provided arguments is incorrect.Please correct your input."
        
        #checked also inside function by using  if-in operators
        except KeyError:
            return "Incorrect phone number or name. Please correct your input."
 
        except IndexError:
            "Index your are trying to access is incorrect. Please provide the correct one."

    return inner

#handler funcions
#function to parse input from user
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower() 
    return cmd, *args

#function to add a contact in a dictionary
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} {contacts[name]} added."

#function to change a phone number by a name
@input_error
def change_contact(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact changed"
    else:
        return "There is no contact with requested name"

#function to show phone number by a name    
@input_error
def show_phone(args, contacts):
    name = args[0]
    
    if name in contacts:
        return f"Phone of {name} is {contacts[name]}"
    else:
        return "Phone is not in contacts"    

#function to show all contacts
@input_error
def show_all(args, contacts):
    if len(contacts) == 0:
        return "Contacts are empty"
    
    for key in contacts:
        print(f"Name: {key.capitalize()}, phone: {contacts[key]}")
    return "End of show all command"

#main logic
def main():
    print("Welcome to the assistant bot")

    contacts = {}
    
    while True:
        user_input = input("Enter a command:\n").strip().lower()

        command, *args = parse_input(user_input)

        if command == 'exit' or command == 'close':
            print("Good bye!")
            os._exit(0)

        elif command == 'hello':
            print('How can I help you?')
            continue

        elif command == 'add':
            print("\n=== Add contact start ===")
            print(add_contact(args, contacts))
            print("=== Add contact end ===\n")

        elif command == 'change':
            print("\n=== Change contact start ===")
            change_contact(args, contacts)
            print("=== Change contact end ===\n")

        elif command == 'phone':
            print("\n=== Show phone start ===")
            print(show_phone(args, contacts))  
            print("=== Show phone end ===\n")

        elif command == 'all':
            print("\n=== Show all contacts start ===")
            print(show_all(args, contacts))
            print("=== Show all contacts end ===\n")
        else:
            print("Invalid command. Please correct your input.")

    print("End of contact assistant work")


if __name__ == "__main__":
    main()