import sqlite3
con=sqlite3.connect("data.db")

def user_add(username,parol,main=0):
    cur=con.execute(f"SELECT username FROM users_data WHERE username='{username}'")
    info=cur.fetchone()
    if info is None:
        con.execute(F"""INSERT INTO users_data (username,parol,main)\
          VALUES (?,?,?);""",(username,parol,main,))
        con.commit()

def all_users():
    cur=con.execute(f"SELECT username FROM users_data")
    info=cur.fetchall()
    return [ i[0] for i in info]

def update_main(name):
    con.execute(f"UPDATE users_data SET main=0")
    con.commit()
    con.execute(f"UPDATE users_data SET main=1 WHERE username='{name}'")
    con.commit()

def main_user():
    cur=con.execute(f"SELECT username,parol FROM users_data WHERE main=1")
    info=cur.fetchone()
    return info

