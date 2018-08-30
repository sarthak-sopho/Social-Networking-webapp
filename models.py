import sqlite3 as sql
from os import path
#file which will interact with the db
#Creating functions to add and delete info from db

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
    #creates a connection to db
    con = sql.connect(path.join(ROOT, 'database.db'))
    #using a cursor to access/traverse data
    #Instead of grabbing
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values (?, ?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT, 'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    #store all entries in posts variable
    posts = cur.fetchall()
    return posts