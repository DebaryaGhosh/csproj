import tkinter as tk
import tkinter.ttk as ttk
import constants as c

widgets = {
    c.LCTN_LBLFRME: c.NONE,
    c.STRTNG_LBL: c.NONE,
    c.STRTNG_CMBX: c.NONE,
    c.DSTNTN_LBL: c.NONE,
    c.DSTNTN_CMBX: c.NONE,
}

def setup_trainframe(notebook):
    train_frame = ttk.Frame(
        notebook,
        width=c.NTBK_FRAME_WIDTH,
        height=c.NTBK_FRAME_HEIGHT,
    )
    return train_frame

def setup_widgets(train_frame):

    #-----------LOCATIONS LABELFRAME-----------------
    widgets[c.LCTN_LBLFRME] = ttk.LabelFrame(
        train_frame,
        text=c.LCTN_LBLFRME_TEXT
    )
    widgets[c.LCTN_LBLFRME].grid(row=0, column=0, padx=10, pady=10)

    #-----------STARTING LABEL-----------------------
    widgets[c.STRTNG_LBL] = ttk.Label(
        widgets[c.LCTN_LBLFRME],
        text=c.STRTNG_LBL_TEXT
    )
    widgets[c.STRTNG_LBL].grid(row=0, column=0, sticky='w', padx=(10, 0), pady=(10, 0))

    widgets[c.STRTNG_CMBX] = ttk.Combobox(
        widgets[c.LCTN_LBLFRME],
        width=c.STRTNG_CMBX_WIDTH,
        textvariable=tk.StringVar()
    )
    widgets[c.STRTNG_CMBX]['values'] = ('Kolkata', 'Delhi', 'Mumbai', 'Chennai')
    widgets[c.STRTNG_CMBX].grid(row=1, column=0, padx=10, pady=(0, 10))

    #-----------DESTINATION LABEL-----------------------
    widgets[c.DSTNTN_LBL] = ttk.Label(
        widgets[c.LCTN_LBLFRME],
        text=c.DSTNTN_LBL_TEXT
    )
    widgets[c.DSTNTN_LBL].grid(row=2, column=0, sticky='w', padx=(10, 0), pady=(10, 0))

    widgets[c.DSTNTN_CMBX] = ttk.Combobox(
        widgets[c.LCTN_LBLFRME],
        width=c.DSTNTN_CMBX_WIDTH,
        textvariable=tk.StringVar()
    )
    widgets[c.DSTNTN_CMBX]['values'] = ('Kolkata', 'Delhi', 'Mumbai', 'Chennai')
    widgets[c.DSTNTN_CMBX].grid(row=3, column=0, padx=10, pady=(0, 10))

