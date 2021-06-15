'''
Created on Jun 14, 2021

@author: Noah

Call for certain board presets
'''

def generate_regular_hexmap(dim):
    
    rows = dim * 2
    cols = dim * 4 - 1
    
    corners = range(0, rows*cols-1)
    notCorners = []
    
    #I need to remove the corners that aren't on the map
    for i in range(1, dim):
        for j in range(1,dim-i):
            notCorners.append(cols*(j-1) + i-1) #Top left
    
    notCorners = [0,1,9,10,11,21,44,54,55,56,64,65]
    
    corners = [x for x in corners if x not in notCorners]
    
    
    