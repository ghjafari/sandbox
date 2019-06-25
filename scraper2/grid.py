from Tkinter import *


class Top_Frame:
    def __init__(self, root):
        top_frame = Frame(root, bg='cyan', width=450, height=50, pady=3)
        top_frame.grid(row=0, sticky="ew")

        # create the widgets for the top frame
        model_label = Label(top_frame, text='Model Dimensions')
        width_label = Label(top_frame, text='Width:')
        length_label = Label(top_frame, text='Length:')
        entry_W = Entry(top_frame, background="pink")
        entry_L = Entry(top_frame, background="orange")

        # layout the widgets in the top frame
        model_label.grid(row=0, columnspan=3)
        width_label.grid(row=1, column=0)
        length_label.grid(row=1, column=2)
        entry_W.grid(row=1, column=1)
        entry_L.grid(row=1, column=3)


class Center:
    def __init__(self, root):
        center = Frame(root, bg='gray2', width=50, height=40, padx=3, pady=3)
        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        ctr_left = Frame(center, bg='blue', width=100, height=190)
        ctr_mid = Frame(center, bg='yellow', width=250, height=190, padx=3, pady=3)
        ctr_right = Frame(center, bg='green', width=100, height=190, padx=3, pady=3)

        ctr_left.grid(row=0, column=0, sticky="ns")
        ctr_mid.grid(row=0, column=1, sticky="nsew")
        ctr_right.grid(row=0, column=2, sticky="ns")


class Btm_Frame:
    def __init__(self, root):
        btm_frame = Frame(root, bg='lavender', width=450, height=45, pady=3)
        root.grid_rowconfigure(1, weight=1)
        btm_frame.grid(row=3, sticky="ew")


class Btm_Frame2:
    def __init__(self, root):
        btm_frame2 = Frame(root, bg='red', width=450, height=60, pady=3)
        root.grid_columnconfigure(0, weight=1)
        btm_frame2.grid(row=4, sticky="ew")


class main():
    def __init__(self):
        root = Tk()
        root.title('Model Definition')
        root.geometry("460x350")

        Top_Frame(root)
        Center(root)
        Btm_Frame(root)
        Btm_Frame2(root)

        root.mainloop()


if __name__ == "__main__":
    main()
