'''
Created on Jun 14, 2021

@author: Noah

Call for certain board presets

return
    a list of corners that are in the map
'''

def generate_regular_hexmap(dim):
    
    rows = dim * 2
    cols = dim * 4 - 1
    
    corners = range(0, rows*cols-1)
    notCorners = []
    
    #I need to remove the corners that aren't on the map
    for i in range(1, dim):
        for j in range(dim-i,0,-1):
            notCorners.append(cols*(j-1) + i-1) #Top left
            notCorners.append(cols*j-i) #Top right
            notCorners.append(cols*(rows-i)+j-1) #Bottom left
            notCorners.append(cols*(rows-j+1)-i) #Bottom right
            
    notCorners = [0,1,9,10,11,21,44,54,55,56,64,65]
    
    corners = [x for x in corners if x not in notCorners]
    
    return corners
    
    
    