import tkinter as tk
import tkinter.ttk as ttk
import constants as c

widgets = {
    c.ROOT: c.NONE,
    c.FRAME: c.NONE,
    c.TITLE_LBL: c.NONE,
    c.TABS_NTBK: c.NONE,
    c.NTBK_FRAME_TRAIN: c.NONE,
    c.NTBK_FRAME_PLANE: c.NONE,
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
        highlightbackground = c.FRAME_BRDR,
        highlightthickness = c.FRAME_BRDR_THKS,
        width=c.FRAME_WIDTH,
        height=c.FRAME_HEIGHT,
    )
    widgets[c.FRAME].grid_propagate(0)
    widgets[c.FRAME].pack(padx=5, pady=5)
    
    widgets[c.TITLE_LBL] = ttk.Label(
        widgets[c.FRAME],
        text=c.TITLE_LBL_TEXT,
        font = c.TITLE_LBL_FONT,
    )
    widgets[c.TITLE_LBL].grid(row=0, column=0, sticky='w', padx=10, pady=5)

    widgets[c.TABS_NTBK] = ttk.Notebook(
        widgets[c.FRAME],
    )
    widgets[c.TABS_NTBK].grid(row=1, column=0, columnspan=2, sticky='ew', padx=10, pady=(30, 0))

    widgets[c.NTBK_FRAME_TRAIN] = ttk.Frame(
        widgets[c.TABS_NTBK],
        width = c.NTBK_FRAME_WIDTH,
        height=c.NTBK_FRAME_HEIGHT,
    )
    widgets[c.NTBK_FRAME_PLANE] = ttk.Frame(
        widgets[c.TABS_NTBK],
        width=c.NTBK_FRAME_WIDTH,
        height=c.NTBK_FRAME_HEIGHT,
    )

    widgets[c.NTBK_FRAME_TRAIN].pack(fill=tk.BOTH, expand=True)
    widgets[c.NTBK_FRAME_PLANE].pack(fill=tk.BOTH, expand=True)

    widgets[c.TABS_NTBK].add(widgets[c.NTBK_FRAME_TRAIN], text = c.TAB_TRAINS)
    widgets[c.TABS_NTBK].add(widgets[c.NTBK_FRAME_PLANE], text = c.TAB_PLANES)

    s = ttk.Style()
    s.configure("TNotebook", tabposition='n')

def main():
    setup_root()
    setup_widgets()

main()
widgets[c.ROOT].mainloop()