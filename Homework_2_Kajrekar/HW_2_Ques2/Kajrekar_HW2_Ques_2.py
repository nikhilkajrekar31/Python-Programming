# Name: Nikhil Kajrekar
# UTA ID: 1001552488

import os

def main():
    while True:
        print("\tCHOICE  MENU\n"
              "1) Add a contact\n"
              "2) Show the list of contacts\n"
              "3) Search for a name in the list\n"
              "4) Modify a contact\n"
              "5) Delete a contact from the list\n"
              "6) Quit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Enter a valid choice")
            continue

        if choice == 1:
            add()
        elif choice == 2:
            show()
        elif choice == 3:
            search()
        elif choice == 4:
            modify()
        elif choice == 5:
            delete()
        elif choice == 6:
            break
        else:
            print("Invalid choice")
            continue

def add():
    print("Enter the following contact info:\n")
    name = str(input("Name: "))
    email = str(input("email: "))
    phone = str(input("phone: "))
    f = open("contacts.txt", "a")
    if (os.path.getsize("contacts.txt") > 0):
        f.write("\n" + name + "\n")
        f.write(email + "\n")
        f.write(phone)
    else:
        f.write(name + "\n")
        f.write(email + "\n")
        f.write(phone)
    f.close()
    while True:
        add_another = input(str("Do you want to add another record? Enter Y for yes or N for no: "))
        if add_another == "Y" or add_another == "y":
            add()
        elif add_another == "N" or add_another == "n":
            break
        else:
            print("Please enter Y for yes or N for no")
            continue

def show():
    line_count = 0
    contacts_count = 1
    count = 1
    f = open("contacts.txt", "r")
    if (os.path.getsize("contacts.txt") > 0):
        print("List of contact(s):")
        for line in f:
            if count == 1:
                print("Contact # ", contacts_count)
                print("\tName: "+line.rstrip())
                count += 1
            elif count == 2:
                print("\tEmail: " + line.rstrip())
                count += 1
            elif count == 3:
                print("\tPhone: " + line.rstrip())
                count += 1
            line_count += 1
            if line_count%3 == 0:
                count = 1
                contacts_count += 1
                print("------------------------------------------")
    else:
        print("No contacts found")
    f.close()


def search():
    found = False
    name_to_search = input(str("Enter a name to search for: "))
    f = open("contacts.txt", "r")
    for line in f:
        if line.rstrip() == name_to_search:
            found = True
            print("Name: " + line.rstrip())
            print("Email: " + f.readline().rstrip())
            print("Phone: " + f.readline().rstrip()+"\n")
            break
    if found == False:
        print("Name not found")
    f.close()

def modify():
    found = False
    name_for_update = input(str("Enter a name to search for update: "))
    new_email = input(str("Enter the new email for update: "))
    new_phone = input(str("Enter the new phone for update: "))
    f = open('contacts.txt', 'r')
    f1 = open('tempfile.txt', 'w')
    name = f.readline()
    while name != '':
        email = f.readline().rstrip()
        phone = f.readline().rstrip()
        name = name.rstrip('\n')
        if name == name_for_update:
            f1.write(name + '\n')
            f1.write(new_email + '\n')
            f1.write(new_phone + '\n')
            found = True
        else:
            f1.write(name + '\n')
            f1.write(email + '\n')
            f1.write(phone + '\n')
        name = f.readline()
    f.close()
    f1.close()

    os.remove('contacts.txt')
    os.rename('tempfile.txt', 'contacts.txt')

    if found:
        print('The file has been updated')
    else:
        print('That item was not found in the file')


def delete():
    found = False
    name_to_delete = input(str("Which name do you want to delete? "))
    f = open('contacts.txt', 'r')
    f1 = open('tempfile.txt', 'w')
    name = f.readline()
    while name != '':
        email = f.readline().rstrip()
        phone = f.readline().rstrip()
        name = name.rstrip('\n')
        if name != name_to_delete:
            f1.write(name + '\n')
            f1.write(email + '\n')
            f1.write(phone + '\n')
        else:
            found = True
        name = f.readline()
    f.close()
    f1.close()

    os.remove('contacts.txt')
    os.rename('tempfile.txt', 'contacts.txt')

    if found:
        print('The file has been updated')
    else:
        print('That item was not found in the file')


main()