# Importing libraries
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Creating and setting up the window
root = Tk()
root.title("Abhiram's Text Editor")
root.geometry("600x500")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)
root.configure(background="OliveDrab2")

# Creating open and save functions
def open_file():
    files = [("Text Files", "*.txt"),
             ("All Files", "*.*")]
    file_path = askopenfilename(filetypes=files)
    if not file_path:
        return
    with open(file_path, "r") as input_file:
        txt_edit.delete(1.0, END)
        text = input_file.read()
        txt_edit.insert(END, text)
        input_file.close()
    root.title(f"Abhiram's Text Editor - {file_path}")

def save_file():
    files = [("Text Files", "*.txt"),
             ("Python Files", "*.py"),
             ("All Files", "*.*")]
    file_path = asksaveasfilename(filetypes=files, defaultextension="txt")
    if not file_path:
        return
    with open(file_path, "w") as output_file:
        text = txt_edit.get(1.0, END)
        output_file.write(text)
        output_file.close()
    root.title(f"Abhiram's Text Editor - {file_path}")


txt_edit = Text(master=root)
frame = Frame(master=root, relief="ridge", bd=2, bg="orange", width=15)
open_btn = Button(master=frame, text="Open", command=open_file, relief="groove", bg="medium blue")
save_btn = Button(master=frame, text="Save", command=save_file, relief="groove", bg="medium blue")

frame.grid(row=0, column=0, sticky="ns")
open_btn.grid(row=0, column=0, sticky="ew", padx=10, pady=10)
save_btn.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
txt_edit.grid(row=0, column=1, sticky="nsew")

root.mainloop()