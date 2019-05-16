import sqlite3
conn = sqlite3.connect('players_Data.db')
conn.execute(''' CREATE TABLE if not exists Player( name TEXT NOT NULL, wins INT NOT NULL, losses INT NOT NULL, ties INT NOT NULL)''')
conn.commit()

def main():
    command = ""
    print("COMMAND MENU\nview - View players\nadd - Add a player\ndel - Delete a player\nupdate - Update a player\nexit - Exit program\n")
    while True:
        command = str(input("\nCommand: "))
        if command == "view":
            view()
        elif command == "add":
            add()
        elif command == "delete":
            delete()
        elif command == "update":
            update()
        elif command == "exit":
            conn.close()
            print("Bye!")
            break
        else:
            print("Please enter correct command")

def view():

    sql = "SELECT * FROM Player ORDER BY wins DESC"
    cursor = conn.execute(sql)
    print('{:15}{:6}{:8}{:6}{:}'.format('Name', 'Wins', 'Losses', 'Ties', 'Games'))
    print("- - - - - - - - - - - - - - - - - - - - -")
    for c in cursor:
        print('{:15}{:3}{:6}{:7}{:7}'.format(c[0], c[1], c[2], c[3], c[1]+c[2]+c[3]))


def add():
    name = str(input("Name: "))
    while True:
        try:
            wins = int(input("Wins: "))
            losses = int(input("Losses: "))
            ties = int(input("Ties: "))
        except ValueError:
            print("Invalid input. Please try again")
        else:
            games = wins + losses + ties
            conn.execute("INSERT INTO Player (name, wins, losses, ties) VALUES (?, ?, ?, ?)",(name,wins,losses,ties))
            conn.commit()
            print(name,"was added to the database")
            break

def delete():
    name = str(input("Name: "))
    sql = "SELECT COUNT(*) FROM Player WHERE name = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    count = cursor.fetchone()[0]
    if count == 0:
        print("Name not found in database")
    else:
        sql = "DELETE FROM Player WHERE name = ?"
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        conn.commit()
        print(name,"was deleted from database")

def update():
    name = str(input("Name: "))
    sql = "SELECT COUNT(*) FROM Player WHERE name = ?"
    cursor = conn.cursor()
    cursor.execute(sql, (name,))
    count = cursor.fetchone()[0]
    if count == 0:
        print("Name not found in database")
    else:
        while True:
            try:
                wins = int(input("Wins: "))
                losses = int(input("Losses: "))
                ties = int(input("Ties: "))
            except ValueError:
                print("Invalid input. Please try again")
            else:
                sql = "UPDATE Player SET wins = ?, losses = ?, ties = ? WHERE name = ?"
                cursor = conn.cursor()
                cursor.execute(sql, (wins,losses,ties,name))
                conn.commit()
                print("Player updated successfully")
                break

main()

