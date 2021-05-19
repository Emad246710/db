import sqlite3
from werkzeug.security import generate_password_hash

def create_user_table(conn):
    cur = conn.cursor()
    sql = ("CREATE TABLE users ("
            "userid INTEGER, "
            "username VARCHAR(20) NOT NULL, "
            "passwordhash VARCHAR(120) NOT NULL, "
            "PRIMARY KEY(userid) "
            "UNIQUE(username))")
    cur.execute(sql)
    conn.commit
    cur.close()

def create_note_table(conn):
    cur = conn.cursor()
    sql = ("CREATE TABLE notes ("
            "user INTEGER, "
            "noteid INTEGER not null, "
            "content TEXT NOT NULL, "
            "title TEXT NOT NULL, "
            "createdOn TEXT not null, "
            "PRIMARY KEY(noteid) "
            "FOREIGN KEY (user) REFERENCES users (userid))")
    cur.execute(sql)
    conn.commit
    cur.close()

def add_user(conn, username, hash):
    cur = conn.cursor()
    sql = ("INSERT INTO users (username, passwordhash) VALUES (?,?)")
    cur.execute(sql, (username, hash))
    conn.commit()
    cur.close()

def add_note(conn, title, content,createdOn, userid):
    cur = conn.cursor()
    sql = ("INSERT INTO notes (user,title, content, createdOn) VALUES (?,?,?,?)")
    cur.execute(sql, (userid, title, content, createdOn))
    conn.commit()
    cur.close()

def get_user_notes(conn, userid):
    cur = conn.cursor()
    sql = ("SELECT title, content, createdOn FROM notes WHERE user = ?")
    cur.execute(sql, (userid,))
    notes = []
    for row in cur:
        (title,content,createdOn) = row
        notes.append({
            "title": title,
            "content": content,
            "createdOn": createdOn
        })
    cur.close()
    return notes
    

def get_user_by_name(conn, username):
    cur = conn.cursor()
    sql = ("SELECT userid, username FROM users WHERE username = ?")
    cur.execute(sql, (username,))
    for row in cur:
        (id,name) = row
        return {
            "username": name,
            "userid": id
        }
    else:
        #user does not exist
        return {
            "username": username,
            "userid": None
        }
    cur.close()

def get_hash_for_login(conn, username):
    cur = conn.cursor()
    sql = ("SELECT passwordhash FROM users WHERE username=?")
    cur.execute(sql, (username,))
    for row in cur:
        (passhash,) = row
        cur.close()
        return passhash
    else:
        cur.close()
        return None
    


if __name__ == "__main__":
    


    conn = sqlite3.connect("database.db")
    
    create_user_table(conn)
    create_note_table(conn)
    add_user(conn,"emadom", generate_password_hash("maherabd"))
    add_user(conn,"maherabd", generate_password_hash("emadom"))

        
    add_note(conn, "John Sigvard", "test note 1", "44-123-312", 1)
    add_note(conn, "Maher abdi", "test note 2", "12-442-622", 1)
    add_note(conn, "Kate Klisina", "test note 3", "86-865-987", 1)
    add_note(conn, "Maher abdi", "easy ", "d-622", 2)
    add_note(conn, "Kate Klisina", "test easy 3", "8s-987", 2)
        
    conn.close()