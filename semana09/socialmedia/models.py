import sqlite3
from os import path

ROOT = path.dirname(path.relpath((__file__)))

def create_post(name, content):
	con = sql.connect(path.join(ROOT, 'database.db'))
	cur = con.cusor()
	cur.execute('insert into posts(name, content) values(?, ?), (name, content))
	con.commit()
	con.close()

def get_posts():
	con = sql.connect(path.join(ROOT, 'database.db'))
	cur = con.cusor()
	cur.execute('select * from posts')
	posts = cur.fetchall()
	return posts