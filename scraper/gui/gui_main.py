import Tkinter as tk
import time

class Main_Window:
    def __init__(self):
        root = tk.Tk()
        root.title("Web Scraper")
        root.geometry("700x120")
        root.resizable(False, False)

        # Initialize the different components of the Main Window
        Entry_Fields(root)
        Output_Type_Select(root)

        root.mainloop()

class Entry_Fields:
    def __init__(self, master):
        self.entry_field  = tk.Entry(master, bd=3, justify="center", width=50)
        self.entry_button = tk.Button(master, text="Scrape!", width=42)
        self.about_button = tk.Button(master, text="About")

        # Widget Prorperties
        self.entry_field.grid(row=0, column=0, padx=12, pady=5)
        self.entry_field.insert(0, "Enter URL here...")

        self.entry_button.grid(row=1, column=0)
        self.about_button.grid(row=3, column=0, pady=5)

        # Widget Events
        self.entry_field.bind("<Return>", self.Entry_Field_Event)
        self.entry_field.bind("<FocusIn>", self.Entry_Field_Focus_In)
        self.entry_button.bind("<Button-1>", self.Entry_Field_Event)
        self.about_button.bind("<Button-1>", self.About_Button_Event)


    def Entry_Field_Event(self, eventObj):
        print("SCRAPING!")
        InProgress_Popup()

    def Entry_Field_Focus_In(self, event):
        if self.entry_field.get() == "Enter URL here...":
            self.entry_field.delete(0, tk.END)

    def Entry_Button_Event(self, eventObj):
        print("SCRAPING!")
        InProgress_Popup()

    def About_Button_Event(self, eventObj):
        About_Popup()

class Output_Type_Select:
    def __init__(self, master):
        self.radio1 = tk.Radiobutton(master, text="Text", variable=tk.IntVar(), value=1)
        self.radio2 = tk.Radiobutton(master, text="Table", variable=tk.IntVar(), value=2)

        self.radio1.grid(row=2, column=0)
        self.radio2.grid(row=2, column=1)

class About_Popup:
    def __init__(self):
        about_popup = tk.Tk()
        about_popup.title("About")
        about_popup.geometry("230x100")
        about_popup.resizable(False, False)

        about_text   = tk.Text(about_popup, bd = 3, height = 4, width = 50)
        close_button = tk.Button(about_popup, text="Close", command = self.Close_About_Popup)

        # Widget Prorperties
        close_button.grid(row = 1, column = 1)
        about_text.grid(row = 0, column = 1)
        about_text.insert(tk.INSERT, "TEST!")
        about_text.configure(state = "disabled")

        about_popup.mainloop()

    def Close_About_Popup(self):
        #self.destroy()
        # TODO: Find a way to close this window with the button.
        # NOTE: .destroy() won't work because of Toplevel()?
        print("#TODO: Close this window")


class InProgress_Popup:
    def __init__(self):
        # Create a window and display the message
        # before closing on timeout
        inprogress_popup = tk.Tk()
        inprogress_popup.geometry("230x100")
        inprogress_popup.resizable(False, False)

        # TODO: Change the lambda to close the window after
        #       the scraping has been completed
        inprogress_popup.after(3000, lambda: inprogress_popup.destroy())

        # TODO Create progress bar for scraping
        inprogress_popup.mainloop()

# TODO: Remove later... use this for debug
if __name__ == '__main__':
   Main_Window()
