import sqlite3
import sys  
import re
import os

running = True

conn = sqlite3.connect('a3.db')
c = conn.cursor()

while running:

    os.system('clear')

    print("Welcome to Ride Services")

    print("0 - Exit    ")
    print("1 - Login   ")
    print("2 - Register \n")

    while True:
        inp = input("Enter desired integer to begin \n")
        if inp.isdigit():
            if 0 <= int(inp) <= 2:
                break
        print("Invalid input, please try again. \n")

    # If inp is 0, exit:
    if(int(inp) == 0):
        conn.commit()
        sys.exit()

    # If inp is 1, login:

    if(int(inp) == 1):

        while True:
            meme = input("Please enter your email: ")
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$", meme):
                c.execute("""SELECT * FROM members WHERE email=?;""", (meme,))
                useremail = c.fetchone()
                print(useremail)
                if useremail is None:
                    print("Invalid email")
                    break 
                count = 3
                while count != 0:
                    pwd = input("Please enter your password: ")
                    c.execute("""SELECT * FROM members WHERE email=? and pwd=?;""", (meme,pwd))
                    data = c.fetchone() 
                    if data is not None:
                        break
                    count = count - 1 
                    print("Invalid password please try again "+str(count)+" tries left.")
                running = False
                break     
            if(meme.isdigit()):
                if(int(meme) == 0):
                    break
            print("Invalid email, please try again. 0 to Main Menu\n")

key = data[0]
print(data)

c.execute("""SELECT * from inbox where email = ? and seen = "N" order by msgTimestamp;""", (key,))
messagetable = c.fetchall()

print("Welcome "+data[1]+"\nHere are your unseen messages: ")
for x in range(len(messagetable)):
    print("Message "+str(x+1))
    print(messagetable[x][3])