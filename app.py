import tkinter as tk
import os
from tkinter import filedialog
import sys

# Initialize a variable to track the current filename
current_filename = None

# Theme
window = tk.Tk()
window.title("pnote - personal notes made easy")
window.configure(bg="#d3d3d3")  # Set background color for dark theme

# Functions
def save_note():
    global current_filename
    note = note_entry.get("1.0", tk.END)
    if current_filename:
        with open(current_filename, "w") as f:
            f.write(note)
    else:
        current_filename = "untitled.txt"
        with open(current_filename, "w") as f:
            f.write(note)

def save_note_as():
    note = note_entry.get("1.0", tk.END)
    filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if filename:
        with open(filename, "w") as f:
            f.write(note)
        global current_filename
        current_filename = filename

def open_note(filename=None):
    global current_filename
    if filename:
        with open(filename, "r") as f:
            note = f.read()
            note_entry.delete("1.0", tk.END)  # Clear the text box
            note_entry.insert(tk.END, note)
        current_filename = filename
    else:
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            open_note(filename)

def show_about():
    about_window = tk.Toplevel(window)
    about_window.title("About pnote")
    about_text = tk.Label(about_window, text="pnote made by Anas Dhf. For the Free & Open-Source Software Community & Supporters.")
    about_text.pack()

# Layout
header_frame = tk.Frame(window, bg="#d3d3d3")  # Same color as text box
header_frame.pack(fill=tk.X)

open_button = tk.Button(header_frame, text="Open", command=open_note)
open_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(header_frame, text="Save", command=save_note)
save_button.pack(side=tk.LEFT, padx=5)

save_as_button = tk.Button(header_frame, text="Save As", command=save_note_as)
save_as_button.pack(side=tk.LEFT, padx=5)

know_more_button = tk.Button(header_frame, text="Know More", command=show_about)
know_more_button.pack(side=tk.LEFT, padx=5)

note_entry = tk.Text(window, bg="#d3d3d3")
note_entry.pack(fill=tk.BOTH, expand=True)

# Icon
if os.path.exists(".\ico.png"):
    window.iconbitmap(".\ico.png")

# Check for command line arguments (when opening .txt files)
if len(sys.argv) > 1:
    open_note(sys.argv[1])

# Main loop
window.mainloop()
