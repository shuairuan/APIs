import pymysql as sql

def connect(host, user, password, charset='utf8'):
    # Connect to MySQL DB, requires host IP, username, password.
    conn = sql.connect(host=host, user=user, passwd=password, charset=charset)
    return conn

def cursor(conn):
    # Get cursor then return.
    cur = conn.cursor()
    return cur

def run(cur, cmd):
    # Run user provided command
    cur.execute(cmd)
    return True

def fetchline(cur):
    # Fetch One Line
    line = cur.fetchone()
    return line

def fetchall(cur):
    # Fetch All Line
    line = cur.fetchall()
    return line
