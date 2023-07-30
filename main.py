import tkinter as tk
import constants as c

widgets = {
    c.ROOT: None,
    c.WINDOW_BUTTON_1: None,
}

def setup_root():
    global widgets

    widgets[c.ROOT] = tk.Tk()
    widgets[c.ROOT].title(c.WINDOW_TITLE)
    widgets[c.ROOT].geometry(c.WINDOW_SIZE)
    widgets[c.ROOT].resizable(0, 0)
    

def setup_widgets():
    global widgets

    widgets[c.WINDOW_BUTTON_1] = tk.Button(
        widgets[c.ROOT],
        text='hello world',
        command=lambda: print('hello')
    )
    widgets[c.WINDOW_BUTTON_1].pack()

def main():
    setup_root()
    setup_widgets()

main()
widgets[c.ROOT].mainloop()