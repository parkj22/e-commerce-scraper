
"""
search_window.py

Utilizes Tk interface to receive inputs in a more
user-friendly way

# Author: Jinyoung Park (parkj22)
# Version: January 22, 2022
"""

import tkinter.messagebox
import tkinter.ttk
import data_organizer
from tkinter import *
from tkinter import filedialog


def btn_scrape_pressed():
    """
    btn_scrape_pressed(): triggered when 'Scrape' button is pressed
        once all fields are correctly entered in, user's inputs
        are passed onto data_organizer module
    """
    if search.get().strip() == "":
        tkinter.messagebox.showwarning("Warning", "No search query has been entered!")
        return
    if path.get().strip() == "":
        tkinter.messagebox.showwarning("Warning", "No file path has been entered!")
        return
    if not (use_amazon.get() or use_ebay.get() or use_etsy.get()):
        tkinter.messagebox.showwarning("Warning", "No website has been selected!")
        return
    if num_page.get() is None:
        tkinter.messagebox.showwarning("Warning", "Number of pages has not been selected!")
        return

    progress_frame.configure(text="Initializing...")
    progress_frame.update()

    data_organizer.organize(search.get().replace(" ", "+"), path.get(), use_amazon.get(),
                            use_ebay.get(), use_etsy.get(), int(num_page.get()))


def btn_browse_pressed():
    """
    btn_browse_pressed(): triggered when 'Browse' button is pressed
        opens up filedialog to allow user to choose a location
        for the csv file
    """
    folder_path = filedialog.askdirectory()

    # Do nothing if user hits cancel
    if folder_path == "":
        return

    # Path entry is kept at "readonly" to limit editing file path by hand
    path.configure(state="normal")
    path.delete(0, END)
    path.insert(0, folder_path)
    path.configure(state="readonly")


def open_window():
    """
    open_window(): begins Tk mainloop
    """
    root.mainloop()


def notify_complete():
    """
    notify_complete(): throws an info message written below
    """
    tkinter.messagebox.showinfo("Info", "Your products are ready to be viewed!")


# Tk window configuration starts here
root = Tk()
root.title("E-commerce Scraper")

# Search frame & entry
search_frame = LabelFrame(root, text="Search...", padx=5, pady=5)
search_frame.pack(fill="x", padx=5, pady=5)

search = Entry(search_frame)
search.pack(side="left", fill="x", expand=True, ipady=4)

# Folder path frame & browse button & path entry
folder_path_frame = LabelFrame(root, text="Save as...", padx=5, pady=5)
folder_path_frame.pack(fill="x", padx=5, pady=5)

btn_browse = Button(folder_path_frame, padx=5, pady=5, text="Browse...", command=btn_browse_pressed)
btn_browse.pack(side="right")

path = Entry(folder_path_frame, state="readonly")
path.pack(side="left", fill="x", expand=True, ipady=4)

# Option frame with checkboxes and a combobox
option_frame = LabelFrame(root, text="Options")
option_frame.pack(fill="x", padx=5, pady=5)

use_amazon, use_ebay, use_etsy = BooleanVar(), BooleanVar(), BooleanVar()
check_amazon = Checkbutton(option_frame, text="Amazon", variable=use_amazon)
check_ebay = Checkbutton(option_frame, text="Ebay", variable=use_ebay)
check_etsy = Checkbutton(option_frame, text="Etsy", variable=use_etsy)
check_amazon.select()
check_ebay.select()
check_etsy.select()

num_page = tkinter.ttk.Combobox(option_frame, values=[str(i) for i in range(1, 6)])
num_page.set("Number of pages")

check_amazon.grid(column=0, row=0)
check_ebay.grid(column=1, row=0)
check_etsy.grid(column=2, row=0)
num_page.grid(column=3, row=0)

# Progress frame & bar
progress_frame = LabelFrame(root, text="Progress bar")
progress_frame.pack(fill="x", padx=5, pady=5)

progress_var = IntVar()  # progress variable
progress = tkinter.ttk.Progressbar(progress_frame, mode="determinate", variable=progress_var)
progress.pack(fill="x", padx=5, pady=5)

# Button frame & scrape button & close button
btn_frame = Frame(root)
btn_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(btn_frame, padx=5, pady=5, text="Close", width=6, command=root.quit)
btn_close.pack(side="right")

btn_scrape = Button(btn_frame, padx=5, pady=5, text="Scrape", width=6, command=btn_scrape_pressed)
btn_scrape.pack(side="right")

root.resizable(False, False)
