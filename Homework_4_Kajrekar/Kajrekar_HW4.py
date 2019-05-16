# This program manages employees.
import employee
import pickle

# Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

# Global constant for the filename
FILENAME = 'employees.dat'

# main function
def main():
    # Load the existing employees dictionary and
    # assign it to employees.
    employees = load_employees()

    # Initialize a variable for the user's choice.
    choice = 0

    # Process menu selections until the user
    # wants to quit the program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()

        # Process the choice.
        if choice == LOOK_UP:
            look_up(employees)
        elif choice == ADD:
            add(employees)
        elif choice == CHANGE:
            change(employees)
        elif choice == DELETE:
            delete(employees)

    # Save the employees dictionary to a file.
    save_contacts(employees)

def load_employees():
    try:
        # Open the employees.dat file.
        input_file = open(FILENAME, 'rb')

        # Unpickle the dictionary.
        employee_dct = pickle.load(input_file)

        # Close the employees.dat file.
        input_file.close()
    except IOError:
        # Could not open the file, so create
        # an empty dictionary.
        employee_dct = {}

    # Return the dictionary.
    return employee_dct

# The get_menu_choice function displays the menu
# and gets a validated choice from the user.
def get_menu_choice():
    print()
    print('Menu')
    print('---------------------------')
    print('1. Look up an employee')
    print('2. Add a new employee')
    print('3. Change an existing employee')
    print('4. Delete an employee')
    print('5. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # return the user's choice.
    return choice

# The look_up function looks up an item in the
# specified dictionary.
def look_up(employees):
    # Get a name to look up.
    name = input('Enter a name: ')

    # Look it up in the dictionary.
    print(employees.get(name, 'That name is not found.'))

# The add function adds a new entry into the
# specified dictionary.
def add(employees):
    # Get the employee info.
    name = input('Name: ')
    id_number = input('ID number: ')
    department = input('Department: ')
    job_title = input('Job title: ')

    # Create a Employee object named entry.
    entry = employee.Employee(name, id_number, department, job_title)
    # If the name does not exist in the dictionary,
    # add it as a key with the entry object as the
    # associated value.
    if name not in employees:
        employees[name] = entry
        print('The entry has been added.')
    else:
        print('That name already exists.')

# The change function changes an existing
# entry in the specified dictionary.
def change(employees):
    # Get a name to look up.
    name = input('Enter a name: ')

    if name in employees:
        # Get a new id number number.
        id_number = input('Enter the new ID number: ')

        # Get a new department address.
        department = input('Enter the new department: ')

        # Get a new job title address.
        job_title = input('Enter the new job title: ')

        # Create a employee object named entry.
        entry = employee.Employee(name, id_number, department, job_title)

        # Update the entry.
        employees[name] = entry
        print('Information updated.')
    else:
        print('That name is not found.')

# The delete function deletes an entry from the
# specified dictionary.
def delete(employees):
    # Get a name to look up.
    name = input('Enter a name: ')

    # If the name is found, delete the entry.
    if name in employees:
        del employees[name]
        print('Entry deleted.')
    else:
        print('That name is not found.')

# The save_contacts funtion pickles the specified
# object and saves it to the employees file.
def save_contacts(employees):
    # Open the file for writing.
    output_file = open(FILENAME, 'wb')

    # Pickle the dictionary and save it.
    pickle.dump(employees, output_file)

    # Close the file.
    output_file.close()

# Call the main function.
main()
