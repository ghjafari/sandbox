try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk


class Input_Fields:
    def __init__(self, master):
        input_field_frame = tk.Frame(master, width=475, height=75, pady=20, bg='green')
        input_field_frame.grid(row=0, columnspan=3, sticky="ew")

        entry_field = tk.Entry(input_field_frame, width=50, bd=3)
        entry_field.grid(row=0, column=0)
        entry_field.insert(0, "test")


class Format_Selection:
    def __init__(self, master):
        format_select_frame = tk.Frame(master, width=100, height=45, pady=5, padx=5, bg='grey')
        format_select_frame.grid(row=1, columnspan=2, stick="ew")

        # Add vertical radio buttons here
        radio1 = tk.Radiobutton(master, text="Text", variable=tk.IntVar(), value=1)
        radio1.grid(row=1, column=0)

        radio2 = tk.Radiobutton(master, text="Table", variable=tk.IntVar(), value=2)
        radio2.grid(row=1, column=1)


class Input_buttons:
    def __init__(self, master):
        input_button_frame = tk.Frame(master, width=200, height=45, pady=5, padx=5, bg='blue')
        input_button_frame.grid(row=1, column=2, columnspan=3, stick="e")

        button1 = tk.Button(master, text="SCRAPE")
        #button2 = tk.Button(master, text="ABORT")

        button1.grid(row=1, column=2)
        #button2.grid(row=1, column=2)


class About_Popup:
    def __init__(self, master):
        about_button_frame = tk.Frame(master, width=475, height=75, pady=5, padx=5, bg='red')
        about_button_frame.grid(row=2, columnspan=3)


class main():
    def __init__(self):
        root = tk.Tk()
        root.title("Web Scraper")
        root.geometry("475x175")
        # root.resizable(False, False)

        # Create frames with root
        Input_Fields(root)
        Format_Selection(root)
        Input_buttons(root)
        About_Popup(root)

        root.mainloop()


if __name__ == "__main__":
    main()
