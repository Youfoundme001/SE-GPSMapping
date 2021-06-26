import pandas as pd
import matplotlib.pyplot as plt
import os
from tkinter import *

def selectserver(server):
    locations = pd.read_csv("collective.csv")
    refinedlocations = locations.loc[locations["Server"] == server]
    x = refinedlocations.X
    y = refinedlocations.Y
    z = refinedlocations.Z
    ax = plt.axes(projection='3d')
    ax.scatter3D(x,y,z)
    plt.show()

def dieselectserver(server):
    locations = pd.read_csv("diecollective.csv")
    refinedlocations = locations.loc[locations["Server"] == server]
    x = refinedlocations.X
    y = refinedlocations.Y
    z = refinedlocations.Z
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.scatter3D(x,y,z)
    plt.show()


def fullserver():
    locations = pd.read_csv("collective.csv")
    x = locations.X
    y = locations.Y
    z = locations.Z
    ax = plt.axes(projection='3d')
    ax.scatter3D(x,y,z)
    plt.show()

def diefullserver():
    locations = pd.read_csv("diecollective.csv")
    x = locations.X
    y = locations.Y
    z = locations.Z
    gridsize = locations.TotalBlocks
    ax = plt.axes(projection='3d')
    ax.scatter3D(x,y,z,s=gridsize/100, marker='d')
    plt.show()

maincluster=["SENDS02","SENDS03","SENDS02",
"SENDS04","SENDS05","SENDS06","SENDS07","SENDS08",
"SENDS09","SENDS10","SENDS11","SENDS12","SENDS13",
"SENDS14","SENDS15","SENDS16"]

dieserver=["TDRAC02","TDRAC03","TDRAC04","TDRAC05","TDRAC06"]

# resets the collective files to ensure data is new and clean.
if os.path.exists("collective.csv"):
    os.remove("collective.csv")
if os.path.exists("diecollective.csv"):
    os.remove("diecollective.csv")

# Attempt to connect and pull data from Main Cluster Lobby
try:
    print(f'Attempting to Connect to SENDS01')
    lobby = pd.read_csv("//internal/torch/SENDS/SENDS01/Instance/GridExport.csv")
    lobby["Server"] = "SENDS01"
    lobby.to_csv("collective.csv", index=False)
except:
    print(f'Failed to connect to SENDS01.')

# Attempt to connect and pull data from DIE Lobby
try:
    print(f'Attempting to Connect to TDRAC01')
    dielobby = pd.read_csv("//internal/torch/TDRAC/TDRAC01/Instance/GridExport.csv")
    dielobby["Server"] = "TDRAC01"
    dielobby.to_csv("diecollective.csv", index=False)
except:
    print(f'Failed to connect to TDRAC01.')

# Attempting to connect and pull data from All Servers back to Program Home.
for item in maincluster:
    try:
        print(f'Attempting to Connect to {item}')
        file = f"//internal/torch/SENDS/{item}/Instance/GridExport.csv"
        tempcsv = pd.read_csv(file)
        tempcsv["Server"] = item
        tempcsv.to_csv(f'{item}.csv', index=False)
        addcsv = tempcsv
        addcsv.to_csv("collective.csv", mode='a', header=False, index=False)
    except:
        print(f'Failed to connect to {item}.')

for item in dieserver:
    try:
        print(f'Attempting to Connect to {item}')
        file = f"//internal/torch/TDRAC/{item}/Instance/GridExport.csv"
        tempcsv = pd.read_csv(file)
        tempcsv["Server"] = item
        tempcsv.to_csv(f'{item}.csv', index=False)
        addcsv = tempcsv
        addcsv.to_csv("diecollective.csv", mode='a', header=False, index=False)
    except:
        print(f'Failed to connect to {item}.')

# The OMG SO MANY BUTTONS CODE (I'm sure there are better ways to do this)
win = Tk()
f = Frame(win)
l = Label(win, text="Please select a Server")
l2 = Label(win, text="Please select a DI Server")
b1 = Button(win, text="Full Server")
b2 = Button(win, text="SENDS01")
b3 = Button(win, text="SENDS02")
b4 = Button(win, text="SENDS03")
b5 = Button(win, text="SENDS04")
b6 = Button(win, text="SENDS05")
b7 = Button(win, text="SENDS06")
b8 = Button(win, text="SENDS07")
b9 = Button(win, text="SENDS08")
b10 = Button(win, text="SENDS09")
b11 = Button(win, text="SENDS10")
b12 = Button(win, text="SENDS11")
b13 = Button(win, text="SENDS12")
b14 = Button(win, text="SENDS13")
b15 = Button(win, text="SENDS14")
b16 = Button(win, text="SENDS15")
b17 = Button(win, text="SENDS16")
b18 = Button(win, text="DIE Full Server")
b19 = Button(win, text="TDRAC01")
b20 = Button(win, text="TDRAC02")
b21 = Button(win, text="TDRAC03")
b22 = Button(win, text="TDRAC04")
b23 = Button(win, text="TDRAC05")
b24 = Button(win, text="TDRAC06")

l.grid(row=0, column=1)
b1.grid(row=1, column=1)
b2.grid(row=2, column=0)
b3.grid(row=2, column=1)
b4.grid(row=2, column=2)
b5.grid(row=3, column=0)
b6.grid(row=3, column=1)
b7.grid(row=3, column=2)
b8.grid(row=4, column=0)
b9.grid(row=4, column=1)
b10.grid(row=4, column=2)
b11.grid(row=5, column=0)
b12.grid(row=5, column=1)
b13.grid(row=5, column=2)
b14.grid(row=6, column=0)
b15.grid(row=6, column=1)
b16.grid(row=6, column=2)
b17.grid(row=7, column=1)
l2.grid(row=8, column=1)
b18.grid(row=9, column=1)
b19.grid(row=10, column=0)
b20.grid(row=10, column=1)
b21.grid(row=10, column=2)
b22.grid(row=11, column=0)
b23.grid(row=11, column=1)
b24.grid(row=11, column=2)

b1.configure(command=fullserver)
b2.configure(command=lambda: selectserver("SENDS01"))
b3.configure(command=lambda: selectserver("SENDS02"))
b4.configure(command=lambda: selectserver("SENDS03"))
b5.configure(command=lambda: selectserver("SENDS04"))
b6.configure(command=lambda: selectserver("SENDS05"))
b7.configure(command=lambda: selectserver("SENDS06"))
b8.configure(command=lambda: selectserver("SENDS07"))
b9.configure(command=lambda: selectserver("SENDS08"))
b10.configure(command=lambda: selectserver("SENDS09"))
b11.configure(command=lambda: selectserver("SENDS10"))
b12.configure(command=lambda: selectserver("SENDS11"))
b13.configure(command=lambda: selectserver("SENDS12"))
b14.configure(command=lambda: selectserver("SENDS13"))
b15.configure(command=lambda: selectserver("SENDS14"))
b16.configure(command=lambda: selectserver("SENDS15"))
b17.configure(command=lambda: selectserver("SENDS16"))
b18.configure(command=diefullserver)
b19.configure(command=lambda: selectserver("TDRAC01"))
b20.configure(command=lambda: selectserver("TDRAC02"))
b21.configure(command=lambda: selectserver("TDRAC03"))
b22.configure(command=lambda: selectserver("TDRAC04"))
b23.configure(command=lambda: selectserver("TDRAC05"))
b24.configure(command=lambda: selectserver("TDRAC06"))
win.title('SD - Grid Mapping')
win.wm_iconbitmap('draconislogo.ico')
win.mainloop()

print("Post Buttons")