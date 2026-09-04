import tkinter as tk
import random

window = tk.Tk()
window.title("Minesweeper")
window.geometry("400x400")

controlFrame = tk.Frame(window, pady = 2)
controlFrame.grid(row = 0, column = 0)

def reset_board():
  for kk in range (Nrows):
      for jj in range(Ncols):
        buttons[kk][jj]["state"] = "normal"
        buttons[kk][jj].config(relief = tk.RAISED)
        buttons[kk][jj]["text"] = ""
        buttons[kk][jj].config(bg = "#d9d9d9") 

  place_mines()
  update_field

# Define the frames and the widgets 

ResetButton = tk.Button(controlFrame, text = "R", command = reset_board)
ResetButton.grid(row = 0, column = 1)

MinesLabel = tk.Label(controlFrame, text = str(Nmines), font = ("Times New Roman", 12), padx = 5, width = 3, justify = "center", bg = "red")
MinesLabel.grid(row = 0, column = 0)

gameFrame = tk.Frame(window)
gameFrame.grid(row = 1, column = 0)

Nrows = 9
Ncols = 9


field = [[0 for _ in range(Ncols)] for _ in range (Nrows)]

Nmines = 10

def place_mines():
  global locations
  locations_all = [x for x in range(Nrows*Ncols)]
  locations = random.sample(locations_all, Nmines)

def display_field():
  for kk in range(Nrows):
    print(field[kk])

def find_neighbors(r0, c0):
  nn = []
  # Return the list of neighbors of a given cell (r0, c0)
  temp_c = [c0-1, c0, c0+1]
  temp_r = [r0-1, r0, r0+1]

  # Remove the cells that are outside (for corner/edge cells)
  temp_c = [x for x in temp_c if x > -1 and x < Ncols]
  temp_r = [x for x in temp_r if x > -1 and x < Nrows]

  for r in temp_r:
    for c in temp_c:
      nn.append((r, c))

  nn.remove((r0, c0))
  return nn

colors = ['white', 'blue', 'green', 'red', 'dark blue', 'brown', 'cyan', 'black', 'gray']


def clickOn(r, c):

  if buttons[r][c]["text"] == "M":
    return
  
  if field[r][c] == 9:
    # Mine
    for kk in range(0, Nrows):
      for jj in range(Ncols):
          buttons[kk][jj]['state'] = 'disabled'
          buttons[kk][jj].config(relief=tk.SUNKEN)
          if field[kk][jj] == 9:
              buttons[kk][jj]["text"] = "*"
              buttons[kk][jj].config(background = 'red', disabledforeground = 'black')
                
  
  elif field[r][c] != 0:
    # Non-zero
    # display the number of mines in the neighborhood
    buttons[r][c]['state'] = 'disabled'
    buttons[r][c].config(relief=tk.SUNKEN)
    
    buttons[r][c]["text"] = str(field[r][c])
    buttons[r][c].config(disabledforeground=colors[field[r][c]])
  else:
    OpenUp(r, c)

  if checkWinner():
    print('Player Won')
    for location in locations:
      loc_xy = divmod(location, Ncols)
      buttons[loc_xy[0]][loc_xy[1]]['state'] = 'disabled'
      buttons[loc_xy[0]][loc_xy[1]].config(relief=tk.SUNKEN)
      buttons[loc_xy[0]][loc_xy[1]]["text"] = "*"
      buttons[loc_xy[0]][loc_xy[1]].config(background = 'green', disabledforeground = 'black')
    


def checkWinner():
  count = 0
  for r in range(Nrows):
    for c in range(Ncols):
      if buttons[r][c]["state"] == "disabled":
        count = count + 1    

  if count == Nrows*Ncols-Nmines:
    return True


def OpenUp(r, c):

  # Notice the function is first called on an empty cell, 
  # but on recursion this may be called by non-empty cells also 

  if buttons[r][c]["state"] == "disabled":
    return

  if buttons[r][c]["text"] == "M":
    # A mine
   minesDone = MinesLabel.cget("text")
  MinesLabel.configure(text = str(int(minesDone)+1))

  buttons[r][c]['state'] = 'disabled'
  buttons[r][c].config(relief=tk.SUNKEN)
  
  if field[r][c] == 0:
    nn = find_neighbors(r, c)
    for neighbors in nn:
      OpenUp(neighbors[0], neighbors[1])
  else:
    # A non-empty cell
    buttons[r][c]['text'] = str(field[r][c])
    buttons[r][c].config(disabledforeground=colors[field[r][c]])
    

  
  

buttons = []

def on_right_click(event, r, c):
  if buttons[r][c]["state"] == "disabled":
    return

  else: 
    test = buttons[r][c]["text"]
    if test != "M":
      buttons[r][c]["test"] = "M"
      minesDone = MinesLabel.cget("text")
      MinesLabel.configure(text = str(int(minesDone)-1))
    else:
      buttons[r][c]["test"] = ""
      minesDone = MinesLabel.cget("text")
      MinesLabel.configure(text = str(int(minesDone)+1))

def create_board():
  #Create a Nrows x Ncols grid of buttons
  for kk in range (Nrows):
    buttons.append([])
    for jj in range(Ncols):
      b = tk.Button(gameFrame, command = lambda r=kk, c=jj : clickOn(r, c))
      b.bind("<Button-3>", lambda event, r=kk, c=jj : on_right_click(event, r, c))
      b.grid(row=kk, column = jj)
      b["width"] = 1 
      b["font"] = 40
      b['text'] = ""
      buttons[kk].append(b)
      

# Create a Nrows x Ncols grid of buttons
for kk in range(Nrows):
  buttons.append([])
  for jj in range(Ncols):
    b = tk.Button(command = lambda r=kk, c=jj : clickOn(r, c))
    b.grid(row=kk, column = jj)
    b["width"] = 2
    b["font"] = 40
    b['text'] = ' '
    buttons[kk].append(b)





Nmines = 10
locations_all = [x for x in range(Nrows*Ncols)]
locations = random.sample(locations_all, Nmines)
#locations = [67, 72, 80, 79, 41, 26, 16, 5, 59, 6]
locations = [53, 62, 28, 38, 52, 25, 39, 64, 2, 69]
#locations = [53, 62, 28, 38, 52, 25, 39, 64, 2, 69]


field = [[0 for _ in range(Ncols)] for _ in range(Nrows)]

# Notice, the code above is equivalent to:
#field = []
#for jj in range(Nrows):
#  field.append([])
#  for _ in range(Ncols):
#    field[jj].append(0)

# Convert locations to a (x, y) tuple

def update_field():

  # Make sure field if Empty (useful when we reset)
  for kk in range(Nrows):
    for jj in range(Ncols):
      field[kk][jj] = 0

  for location in locations:
   loc_xy = divmod(location, Ncols)
   field[loc_xy[0]][loc_xy[1]] = 9; 

  # Update the field for this location 
  # find neighbors
  nn = find_neighbors(loc_xy[0], loc_xy[1])

  for neighbors in nn:
    if field[neighbors[0]][neighbors[1]] != 9:
      field[neighbors[0]][neighbors[1]] += 1


create_board()
place_mines()
update_field()

  

    


    
# b = tk.Button(command = lambda x=kk, y=jj: clickOn(x,y))
