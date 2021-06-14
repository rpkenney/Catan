# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:31:20 2021

@author: robert
"""

import tkinter as tk


class GameGUI:
    def __init__(self, tiles):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.window.geometry('800x500')
        self.window.title('Catan')
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        
        self.draw_tiles(tiles)
        
        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        
    def draw_tiles(self, tiles):
        tk.Label(self.window, text = "test").pack()