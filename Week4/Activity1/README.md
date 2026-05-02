## Create database based on activity 2 of week 3

This database includes 5 tables.

This database does not consider joint accounts.



- The Customer table defines information about each customer.

CREATE TABLE IF NOT EXISTS Customer(

                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   name TEXT UNIQUE,

                   birth_date TEXT,

                   address TEXT,

                   password TEXT

                   )



- The Account table defines all accounts for each Customer.

CREATE TABLE IF NOT EXISTS Account(

                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   c_id INTEGER,

                   currency TEXT,

                   balance REAL,

                   open_date TEXT,

                   FOREIGN KEY(c_id) REFERENCES Customer(id)

                   )



- The Logs table records all operations for each Customer.

CREATE TABLE IF NOT EXISTS Logs(

                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   c_id INTEGER,

                   operation_type TEXT,

                   description TEXT,

                   created_time TEXT,

                   FOREIGN KEY(c_id) REFERENCES Customer(id)

                   )



- The Records table records all deposit and withdrawal operations for each Account.

CREATE TABLE IF NOT EXISTS Records(

                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   c_id INTEGER,

                   a_id INTEGER,

                   trans_type TEXT,

                   amount REAL,

                   created_time TEXT,

                   FOREIGN KEY(c_id) REFERENCES Customer(id),

                   FOREIGN KEY(a_id) REFERENCES Account(id)

                   )



- The Transfer table records the related record items of exchange.

CREATE TABLE IF NOT EXISTS Transfer(

                   id INTEGER PRIMARY KEY AUTOINCREMENT,

                   a_src_id INTEGER,

                   a_dst_id INTEGER,

                   currency_rate REAL,

                   created_time TEXT,

                   FOREIGN KEY(a_src_id) REFERENCES Customer(id),

                   FOREIGN KEY(a_dst_id) REFERENCES Account(id)

                   )
