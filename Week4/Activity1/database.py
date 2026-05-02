import sqlite3

def connect_database():
    conn = sqlite3.connect("exchange.db")
    return conn

def create_table():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customer(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT UNIQUE,
                   birth_date TEXT,
                   address TEXT,
                   password TEXT
                   )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Account(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   c_id INTEGER,
                   currency TEXT,
                   balance REAL,
                   open_date TEXT,
                   FOREIGN KEY(c_id) REFERENCES Customer(id)
                   )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Logs(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   c_id INTEGER,
                   operation_type TEXT,
                   description TEXT,
                   created_time TEXT,
                   FOREIGN KEY(c_id) REFERENCES Customer(id)
                   )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Records(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   c_id INTEGER,
                   a_id INTEGER,
                   trans_type TEXT,
                   amount REAL,
                   created_time TEXT,
                   FOREIGN KEY(c_id) REFERENCES Customer(id),
                   FOREIGN KEY(a_id) REFERENCES Account(id)
                   )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Transfer(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   a_src_id INTEGER,
                   a_dst_id INTEGER,
                   currency_rate REAL,
                   created_time TEXT,
                   FOREIGN KEY(a_src_id) REFERENCES Customer(id),
                   FOREIGN KEY(a_dst_id) REFERENCES Account(id)
                   )''')
    conn.commit()
    conn.close()