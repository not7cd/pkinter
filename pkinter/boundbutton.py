#!/usr/bin/env python
# -*- coding: utf-8 -*-
""""""

import tkinter as tk
from tkinter import ttk

# link

__title__ = "BoundButton"
__version__ = "1.0.3"
__author__ = "DeflatedPickle"


class BoundButton(ttk.Button):
    """
            -----DESCRIPTION-----
    A ttk Button that can be bound to any key to run any function.

            -----USAGE-----
    def function():
        print("Button Pressed")

    boundButton = BoundButton(parent, text=[string], key=[string], command=[function])
    boundButton.pack()

            -----PARAMETERS-----
    parent  = The parent of the widget.
    text    = The text of the Button.
    key     = The key that will activate the Button.
    command = The function the button will run.

            -----CONTENTS-----
    ---VARIABLES---
    parent  = The parent of the widget.
    _text    = The text of the Button.
    _key     = The key that will activate the Button.
    _command = The function the button will run.

    ---TKINTER VARIABLES---
    None

    ---WIDGETS---
    self

    ---FUNCTIONS---
    None
    """
    def __init__(self, parent, text="", key="Return", command=None, *args):
        ttk.Button.__init__(self, parent, default="active", text=text, command=command, *args)
        self.parent = parent

        self._text = text
        self._key = key
        self._command = command

        self.bind("<{}>".format(key), command)
        self.focus()

##################################################

if __name__ == "__main__":
    def function(event):
        if variable.get() == "foo":
            variable.set("bar")

        elif variable.get() == "bar":
            variable.set("foo")

    root = tk.Tk()
    bbutton = BoundButton(root, text="Press F", key="f", command=function)
    bbutton.pack(expand=True, padx=5, pady=5)
    variable = tk.StringVar()
    variable.set("foo")
    label = ttk.Label(root, textvariable=variable).pack(expand=True, padx=5, pady=5)
    root.mainloop()
