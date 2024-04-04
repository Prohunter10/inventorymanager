import sqlite3
from tkinter import *  # noqa: F403
from tkinter import ttk
import tkinter
from tkinter.filedialog import askopenfile


def submit(name, accessories, pc, picture):
    # csatlakozás a szerverhez és cursor létrehozása
    data = sqlite3.connect("mydatabase")
    c = data.cursor()

    # table létrehozása
    try:
        c.execute("CREATE TABLE equipment(category, name, accessories, pc, picture)")
    except:  # noqa: E722
        pass

    c.execute("""
    INSERT INTO equipment VALUES
        (name, accessories, pc, picture),
    """)

    data.commit()

    data.close()


def edit():
    # csatlakozás a szerverhez és cursor létrehozása
    data = sqlite3.connect("mydatabase")
    c = data.cursor()

    # table létrehozása
    try:
        c.execute("CREATE TABLE equipment(category, name, accessories, pc, picture)")
    except:  # noqa: E722
        pass

    c.execute("""
    INSERT INTO equipment VALUES
        (name, accessories, pc, picture),
    """)

    data.commit()

    data.close()


def delete():
    # csatlakozás a szerverhez és cursor létrehozása
    data = sqlite3.connect("mydatabase")
    c = data.cursor()

    # table létrehozása
    try:
        c.execute("CREATE TABLE equipment(category, name, accessories, pc, picture)")
    except:  # noqa: E722
        pass

    c.execute("DELETE FROM equipment WHERE oid=PLACEHOLDER")

    data.commit()

    data.close()

def new_cat():
    data = sqlite3.connect("mydatabase")
    c = data.cursor()

    # table létrehozása
    try:
        c.execute("CREATE TABLE equipment(category, name, accessories, pc, picture)")
    except:  # noqa: E722
        pass
    
    toplevel1 = tkinter.Toplevel()
    toplevel1.geometry("300x150")
    toplevel1.title("Új kategória hozzáadása")
    
    label1= tkinter.Label(master=toplevel1, text="Az új kategória neve:")
    entry1=  tkinter.Entry(master=toplevel1)
    button1= tkinter.Button(master=toplevel1, text="Hozzáadás")
    button2= tkinter.Button(master=toplevel1, text="Vissza")
    label1.grid()
    entry1.grid()
    button1.grid()
    button2.grid()
    
    
    toplevel1.mainloop()
    
def add():
    data = sqlite3.connect("mydatabase")
    c = data.cursor()

    # table létrehozása
    try:
        c.execute("CREATE TABLE equipment(category, name, accessories, pc, picture)")
    except:  # noqa: E722
        pass
    
    toplevel2 = tkinter.Toplevel()
    toplevel2.geometry("1200x800")
    toplevel2.title("Új elem hozzáadása")
    
    # Create a StringVar to hold the selected option
    selected_option = tkinter.StringVar()
    categories = c.execute("SELECT category FROM equipment")
    categories.fetchall()
    
    dropdown = tkinter.OptionMenu(toplevel2, selected_option, "Válassz kategóriát")
    dropdown.grid(row=0,column=0, pady=50, padx=50)
    
    for category in categories:
        dropdown["menu"].add_command(label=category, command=lambda opt=category: selected_option.set(opt))
        
    dropdown["menu"].add_command(label="Új kategória", command=new_cat)
    
    entry_add1=  tkinter.Entry(master=toplevel2)
    entry_add2=  tkinter.Entry(master=toplevel2)
    entry_add3=  tkinter.Entry(master=toplevel2)
    
    name_add1=  tkinter.Label(master=toplevel2, text="Név:")
    accessories_add2=  tkinter.Label(master=toplevel2, text="Kiegészítők:")
    pc_add3=  tkinter.Label(master=toplevel2, text="Mennyiség")
    
    name_add1.grid()
    entry_add1.grid()
    accessories_add2.grid()
    entry_add2.grid()
    pc_add3.grid()
    entry_add3.grid()
    
    toplevel2.mainloop()

def clckd():
    return


main = Tk()  # noqa: F405
main.geometry("1200x800")
main.title("Felszereléskezelő")

menubar = Menu(main)  # noqa: F405
filemenu = Menu(menubar, tearoff=0)  # noqa: F405
filemenu.add_command(label="Új elem", command = lambda: add())
filemenu.add_command(label="Megnyitás")
filemenu.add_command(label="Mentés")
filemenu.add_command(label="Mentés, mint...")
filemenu.add_command(label="Bezárás")

filemenu.add_separator()
filemenu.add_command(label="Kilépés")

menubar.add_cascade(label="Fájl", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)  # noqa: F405
editmenu.add_command(label="Vissza")
editmenu.add_separator()
editmenu.add_command(label="Kivágás")
editmenu.add_command(label="Másolás")
editmenu.add_command(label="Beillesztés")
editmenu.add_command(label="Törlés")
editmenu.add_command(label="Összes kiválasztása")

menubar.add_cascade(label="Szerkesztés", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)  # noqa: F405
helpmenu.add_command(label="Segítség")
helpmenu.add_command(label="Egyéb...")
menubar.add_cascade(label="Segítség", menu=helpmenu)

main.config(menu=menubar)

frm = ttk.Frame(main, padding=10)
frm.grid()






main.mainloop()