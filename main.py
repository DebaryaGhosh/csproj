import tkinter as tk
import tkinter.ttk as ttk
import constants as c

widgets = {
    c.ROOT: None,
    c.FRAME: None,
    c.TITLE_LBL: None,
    c.PLANE_WIN_BTN: None,
    c.TRAIN_WIN_BTN: None,
    c.LOCATIONS_TRVW: None,
    c.MODE_TRAVEL_LBL: None,
}

def setup_root():
    global widgets

    widgets[c.ROOT] = tk.Tk()
    widgets[c.ROOT].title(c.WINDOW_TITLE)
    widgets[c.ROOT].geometry(c.WINDOW_SIZE)
    widgets[c.ROOT].resizable(0, 0)
    

def setup_widgets():
    global widgets

    widgets[c.FRAME] = tk.Frame(
        widgets[c.ROOT],
        highlightbackground = 'black',
        highlightthickness = 1,
        width=c.FRAME_WIDTH,
        height=c.FRAME_HEIGHT,
    )
    widgets[c.FRAME].grid_propagate(0)
    widgets[c.FRAME].pack(padx=20, pady=10)

    widgets[c.TITLE_LBL] = ttk.Label(
        widgets[c.FRAME],
        text=c.TITLE_LBL_TEXT,
        font = ("Helvetica", "16", 'bold'),
    )
    widgets[c.TITLE_LBL].grid(row=0, column=0, padx=10, pady=5)

    widgets[c.MODE_TRAVEL_LBL] = ttk.Labelframe (
        widgets[c.FRAME],
        text=c.MODE_TRAVEL_TEXT,
    )
    widgets[c.MODE_TRAVEL_LBL].grid(row=0, column = 1, columnspan=2, padx=100, pady=5)

    widgets[c.TRAIN_WIN_BTN] = ttk.Button(
        widgets[c.MODE_TRAVEL_LBL],
        text = c.TRAIN_WIN_TEXT,
        command=lambda: print('open trains window')
    )
    widgets[c.TRAIN_WIN_BTN].grid(row=0, column = 0, padx = 5, pady=3, ipadx = 5, ipady = 3)

    widgets[c.PLANE_WIN_BTN] = ttk.Button(
        widgets[c.MODE_TRAVEL_LBL],
        text = c.PLANE_WIN_TEXT,
        command=lambda: print('open plane window')
    )
    widgets[c.PLANE_WIN_BTN].grid(row=0, column = 1, padx = 5, pady=3, ipadx = 5, ipady = 3)

    

    


def main():
    setup_root()
    setup_widgets()

main()
widgets[c.ROOT].mainloop()
