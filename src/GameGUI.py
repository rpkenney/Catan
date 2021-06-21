# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 19:31:20 2021

@author: robert
"""

import tkinter as tk
import functools as partial


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
        rows = [3, 4, 5, 4, 3]
        for tile in self.tile_graphics:
            tile.destroy()
        self.tile_graphics = []
        c= 0
        for tile in self.tiles:
            res = tile[1]
            num = tile[2]
            col = None
            if res == 'b':
                col = '#c4290e'
            elif res == 'w':
                col = '#ffff00'
            elif res == 'l':
                col = '#152b18'
            elif res == 's':
                col = '#abd685'
            elif res == 'd':
                col = '#e3e0a3'
            elif res == 'r':
                col = '#574f4f'
            self.tile_graphics.append(tk.Button(self.window, text = num, bg = col, fg = '#0a6b5b', 
                                                padx = 25, pady = 25, command = partial.partial(self.select_tile, c)))
            c+=1
            
        c = 0
        y = (self.height - 200) // 5
        for i in range(len(rows)):
            x = (self.width - 100) // (rows[i] + 1)
            for j in range(rows[i]):
                self.tile_graphics[c].place(anchor = 'nw', x = x * (j + 1), y = y * (i + 1))
                c += 1
                
    def select_tile(self, idx):
        print(self.tiles[idx][1])