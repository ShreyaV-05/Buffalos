import sqlite3

def createTable() :
    print ("In Create Table")
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    c.execute("""CREATE TABLE users (
        user_name text NOT NULL,
        user_pswd text NOT NULL,
        user_email text NOT NULL,
        
        PRIMARY KEY(user_name, user_email)
    )""")

    # Commit our command
    conn.commit()
    print("Table Created")
    #Close Connection
    conn.close


def getData():
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    c = conn.cursor()
    print("Getting Data")
    c.execute("SELECT * FROM users")
    items = c.fetchall()
    for item in items:
        print("user_name" + "\t" + item[0] + "\t" + "user_pswd" + "\t" + item[1] + "\t" + "user_email" + "\t" + item[2])

    #Close Connection
    conn.close


def checkLogin(request):
    user = request.form['user']
    password = request.form['user_pswd']
    print("Username" + "\t" + user + "\t" + "Password" + "\t" + password)
    conn = sqlite3.connect('user.db')
    # Creating a Cursor
    try:
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE user_id=?", (user,))
        row = c.fetchall()
        print(row)
        print(row[0][1])
        if row[0][1] == password:
            print("success")
        else:
            print("failed")
            return 0


    # Commit our command
    #conn.commit()
    except IndexError as e:
        print(e)
        print("wrong username")
        return 0
    # close our connection
    conn.close()

    return 1
"""
def updatepwd(request):

    if checkLogin(request) == 1:
        user = request.form['user)name']
        password = request.form['user_pswd']
        npassword = request.form['user_pswd1']
        ncpassword = request.form['user_pswd2']

        if npassword != ncpassword:
            return "New password does not match"

        else:
            conn = sqlite3.connect('user.db')
            c = conn.cursor()
            c.execute("UPDATE users SET user_pswd = ? WHERE user_name = ?", (npassword, user))
            conn.commit()
            conn.close()
            return "Password Updated"
    else:
        return "Username or Password incorrect"


def delete(request):

    if checkLogin(request) == 1:
        user = request.form['user']
        conn = sqlite3.connect('user.db')
        c = conn.cursor()
        c.execute("DELETE FROM users WHERE user_name = ?", (user,))
        conn.commit()
        conn.close()
        return "Account Deleted"


    else:
        return "Username or Password Incorrect"
"""