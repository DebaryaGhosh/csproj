import tkinter as tk
import tkinter.ttk as ttk
import constants as c

widgets = {
    c.ROOT: None,
    c.FRAME: None,
    c.PLANE_WIN_BTN: None,
    c.TRAIN_WIN_BTN: None,
}

def setup_root():
    global widgets

    widgets[c.ROOT] = tk.Tk()
    widgets[c.ROOT].title(c.WINDOW_TITLE)
    widgets[c.ROOT].geometry(c.WINDOW_SIZE)
    widgets[c.ROOT].resizable(0, 0)
    

def setup_widgets():
    global widgets

    widgets[c.FRAME] = ttk.Frame(
        widgets[c.ROOT],
        width=c.FRAME_WIDTH,
        height=c.FRAME_HEIGHT,
    )
    widgets[c.FRAME].grid_propagate(0)
    widgets[c.FRAME].pack()

    widgets[c.TRAIN_WIN_BTN] = ttk.Button(
        widgets[c.FRAME],
        text = c.TRAIN_WIN_TEXT,
        command=lambda: print('open trains window')
    )
    widgets[c.TRAIN_WIN_BTN].grid(row=0, column = 1, ipadx = 5, ipady = 3)

    widgets[c.PLANE_WIN_BTN] = ttk.Button(
        widgets[c.FRAME],
        text = c.PLANE_WIN_TEXT,
        command=lambda: print('open plane window')
    )
    widgets[c.PLANE_WIN_BTN].grid(row=0, column = 2, ipadx = 5, ipady = 3)


def main():
    setup_root()
    setup_widgets()

main()
print(widgets[c.FRAME])
widgets[c.ROOT].mainloop()
