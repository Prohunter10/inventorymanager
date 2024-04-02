import tkinter as tk
import tkinter.filedialog
import sqlite3


#csatlakozás a szerverhez és curosr létrehozása
data=sqlite3.connect("mydatabase")
c=data.cursor()

#table létrehozása
try:
    c.execute("CREATE TABLE equipment(name, accessories, pc, picture)")
except:
    pass

def submit(name, accessories, pc, picture):
    c.execute("""
    INSERT INTO equipment VALUES
        (name, accessories, pc, picture),
""")
    data.commit()

def change():
    return