# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:31:20 2021

@author: robert
"""

import tkinter as tk


class GameGUI:
    def __init__(self, tiles):
        self.tiles = tiles
        self.tile_graphics = []
        self.window = tk.Tk()
        self.fullScreenState = False
        self.window.attributes('-fullscreen', self.fullScreenState)
        self.width = 1000
        self.height = 700
        self.window.geometry(str(self.width) + 'x' + str(self.height))
        self.window.title('Catan')
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)
        
        self.draw_tiles()
        
        self.window.mainloop()

    def toggleFullScreen(self, event):
        if not self.fullScreenState:
            self.width = self.window.winfo_screenwidth()
            self.height = self.window.winfo_screenheight()
        else:
            self.width = 1000
            self.height = 700
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.draw_tiles()

    def quitFullScreen(self, event):
        self.width = 1000
        self.height = 700
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)
        self.draw_tiles()
        
    def draw_tiles(self):
        print(self.width)
        rows = [3, 4, 5, 4, 3]
        for tile in self.tile_graphics:
            tile.destroy()
        self.tile_graphics = []
        for tile in self.tiles:
            self.tile_graphics.append(tk.Label(self.window, text = tile))
        
        c = 0
        y = (self.height - 200) // 5
        for i in range(len(rows)):
            x = (self.width - 100) // (rows[i] + 1)
            for j in range(rows[i]):
                self.tile_graphics[c].place(anchor = 'nw', x = x * (j + 1), y = y * (i + 1))
                c += 1