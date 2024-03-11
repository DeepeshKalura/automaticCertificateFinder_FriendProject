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
    # infoLog("Checking if folder id exists in cache")
    cursor.execute("SELECT * FROM folder WHERE folder_id=?", (folder_id,))
    # infoLog("Folder id exists in cache or not")
    return cursor.fetchone() is not None

def file_exists(name, folder_id):
    # infoLog("Checking if file exists in cache")
    response = cursor.execute("SELECT * FROM file WHERE name=? and folder_id=?", (name, folder_id))
    # infoLog("File exists in cache or not")
    return response.fetchone()
    

def insert_folder(folder_id):
    # infoLog("Inserting folder id in cache")
    cursor.execute("INSERT INTO folder (folder_id) VALUES (?)", (folder_id,))
    conn.commit()
    # infoLog("Folder id inserted in cache")

def insert_file(file_id, name,  file_name, folder_id):
    # infoLog("Inserting file in cache")
    cursor.execute("INSERT INTO file (file_id, name, file_name, folder_id) VALUES (?, ?, ?, ?)", (file_id, name, file_name, folder_id))
    conn.commit()
    # infoLog("File inserted in cache")


