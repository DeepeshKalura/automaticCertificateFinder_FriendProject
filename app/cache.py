import sqlite3 
# from app.logs import infoLog
import time


conn = sqlite3.connect('cache.db')
cursor = conn.cursor()

# Create the table
cursor.execute('''CREATE TABLE IF NOT EXISTS folder (
        folder_id Text PRIMARY KEY,       
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
) ''')

cursor.execute( 
    ''' CREATE TABLE IF NOT EXISTS file (
        file_id Text PRIMARY KEY,
        file_name Text,
        name Text,
        folder_id Text,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (folder_id) REFERENCES folder(folder_id)
) ''')

conn.commit()

def folder_id_exists(folder_id):
    cursor.execute("SELECT * FROM folder WHERE folder_id=?", (folder_id,))
    
    return cursor.fetchone() is not None

def file_exists(name: str, folder_id: str) -> any:
    response = cursor.execute("SELECT * FROM file WHERE name=? and folder_id=?", (name, folder_id))
    return response.fetchone()
    

def insert_folder(folder_id):
    cursor.execute("INSERT INTO folder (folder_id) VALUES (?)", (folder_id,))
    conn.commit()

def insert_file(file_id, name,  file_name, folder_id):
    cursor.execute("INSERT INTO file (file_id, name, file_name, folder_id) VALUES (?, ?, ?, ?)", (file_id, name, file_name, folder_id))
    conn.commit()


