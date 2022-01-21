import tkinter.messagebox
from tkinter import *
import tkinter.ttk
from tkinter import filedialog

import data_organizer
from chrome_driver import ChromeDriver


class SearchWindow:
    def __init__(self):
        root = Tk()
        root.title("E-commerce Scraper")

        search_frame = LabelFrame(root, text="Search...", padx=5, pady=5)
        search_frame.pack(fill="x", padx=5, pady=5)

        self.__search_entry = Entry(search_frame)
        self.__search_entry.pack(side="left", fill="x", expand=True, ipady=4)

        folder_path_frame = LabelFrame(root, text="Save as...", padx=5, pady=5)
        folder_path_frame.pack(fill="x", padx=5, pady=5)

        btn_browse = Button(folder_path_frame, padx=5, pady=5, text="Browse...", command=self.btn_browse_pressed)
        btn_browse.pack(side="right")

        self.__folder_path_entry = Entry(folder_path_frame, state="readonly")
        self.__folder_path_entry.pack(side="left", fill="x", expand=True, ipady=4)

        option_frame = LabelFrame(root, text="Options")
        option_frame.pack(fill="x", padx=5, pady=5)

        self.__check_var_amazon, self.__check_var_ebay, self.__check_var_etsy = BooleanVar(), BooleanVar(), BooleanVar()
        check_amazon = Checkbutton(option_frame, text="Amazon", variable=self.__check_var_amazon)
        check_ebay = Checkbutton(option_frame, text="Ebay", variable=self.__check_var_ebay)
        check_etsy = Checkbutton(option_frame, text="Etsy", variable=self.__check_var_etsy)
        check_amazon.select()
        check_ebay.select()
        check_etsy.select()

        self.__combo_num_page = tkinter.ttk.Combobox(option_frame, values=[str(i) for i in range(1, 6)])
        self.__combo_num_page.set("Number of pages")

        check_amazon.grid(column=0, row=0)
        check_ebay.grid(column=1, row=0)
        check_etsy.grid(column=2, row=0)
        self.__combo_num_page.grid(column=3, row=0)

        progress_frame = LabelFrame(root, text="Progress bar")
        progress_frame.pack(fill="x", padx=5, pady=5)

        progress_var = DoubleVar()
        progress_bar = tkinter.ttk.Progressbar(progress_frame, maximum=100, variable=progress_var)
        progress_bar.pack(fill="x", padx=5, pady=5)

        btn_frame = Frame(root)
        btn_frame.pack(fill="x", padx=5, pady=5)

        btn_close = Button(btn_frame, padx=5, pady=5, text="Close", width=6, command=root.quit)
        btn_close.pack(side="right")

        btn_scrape = Button(btn_frame, padx=5, pady=5, text="Scrape", width=6, command=self.btn_scrape_pressed)
        btn_scrape.pack(side="right")

        root.resizable(False, False)

        root.mainloop()

    def btn_scrape_pressed(self):
        if self.__search_entry.get().strip() == "":
            tkinter.messagebox.showwarning("Warning", "No search query has been entered!")
            return

        if self.__folder_path_entry.get().strip() == "":
            tkinter.messagebox.showwarning("Warning", "No file path has been entered!")
            return

        if not (self.__check_var_amazon.get() or self.__check_var_ebay.get() or self.__check_var_etsy.get()):
            tkinter.messagebox.showwarning("Warning", "No website has been selected!")
            return

        if self.__combo_num_page.get() is None:
            tkinter.messagebox.showwarning("Warning", "Number of pages has not been selected!")
            return

        data_organizer.organize(self.__search_entry.get(), self.__folder_path_entry.get(), self.__check_var_amazon.get(), self.__check_var_ebay.get(), self.__check_var_etsy.get(), int(self.__combo_num_page.get()))

    def btn_browse_pressed(self):
        folder_path = filedialog.askdirectory()
        if folder_path == "":
            return
        self.__folder_path_entry.configure(state="normal")
        self.__folder_path_entry.delete(0, END)
        self.__folder_path_entry.insert(0, folder_path)
        self.__folder_path_entry.configure(state="readonly")
