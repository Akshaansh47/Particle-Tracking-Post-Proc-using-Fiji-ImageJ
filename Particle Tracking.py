import numpy as np
import pandas as pd
from tqdm import tqdm
import time
import matplotlib.pyplot as plt


def ptrack():
    option = input("What would you like to see next?"
                   "\n 1. Snapshot of particle positions at a given frame"
                   "\n 2. Total (net) displacement of a single particle over time"
                   "\n 3. X-Y trajectory of any single particle"
                   "\n 4. Cumulative plots\n")
    option = int(option)
    if option == 1:
        frame = input("\n Which frame would you like to view? \n Your available range is: [0,%i]\n" % frames)
        frame = int(frame)
        print("")
        snap(frame,xloc,yloc,nspots)
    elif option == 2:
        part = input("\n Which particle would you like to view the displacement of? Your available range is: [0,"
                     "%i]. Use the first frame plotted before for particle numbering reference\n" % (nspots-1))
        part = int(part)
        disp(part,frames,xloc,yloc,nspots)
    elif option == 3:
        part2 = input("\n Which particle would you like to view the x-y trajectory of? Use the first frame plotted "
                      "before for particle numbering reference\n")
        part2 = int(part2)
        traj(part2,xloc,yloc)
    elif option == 4:
        option2 = input("\n 1. Net displacement over time"
                        "\n 2. X-location over time"
                        "\n 3. Y-Location over time\n")
        option2 = int(option2)
        cplots(option2,xloc,yloc,nspots,frames)
    else:
        print("\n Invalid input")


def cplots(o,x,y,n,f):
    if o == 1:
        displ = np.zeros((f, n))
        for i in range(0, f):
            for j in range(0, n):
                displ[i, j] = np.sqrt((x[i][j] - x[0][j]) ** 2 + (y[i][j] - y[0][j]) ** 2)
        plt.plot(displ)
        plt.xlabel("Time (frames)")
        plt.ylabel("Net displacement (pixels)")
        plt.title("Cumulative Displacement vs. Time")
        plt.show()
    elif o == 2:
        xd = np.zeros((f, n))
        for i in range(0,f):
            xd[i] = x[i] - x[0]
        plt.plot(xd)
        plt.xlabel("Time (frames")
        plt.ylabel("X-Location (pixels)")
        plt.title("X-Location vs. Time")
        plt.show()
    elif o == 3:
        yd = np.zeros((f, n))
        for i in range(0, f):
            yd[i] = y[i] - y[0]
        plt.plot(yd)
        plt.xlabel("Time (frames")
        plt.ylabel("Y-Location (pixels)")
        plt.title("Y-Location vs. Time")
        plt.show()
    else:
        print("Invalid input")

def snap(f,x,y,n):
    plt.scatter(x[f], y[f])
    for i in range(0, n):
        plt.text(float(x[f][i]), float(y[f][i]), i)
    plt.xlabel("X-location (pixels)")
    plt.ylabel("Y-location (pixels)")
    plt.title("Exact particle locations at frame %i" % f)
    plt.show()


def disp(p,f,x,y,n):
    displ = np.zeros((f, n))
    for i in range(0, f):
        for j in range(0, n):
            displ[i, j] = np.sqrt((x[i][j] - x[0][j]) ** 2 + (y[i][j] - y[0][j]) ** 2)
    plt.plot(displ[:, p])
    plt.xlabel("Time (frames)")
    plt.ylabel("Net displacement (pixels)")
    plt.title("Displacement Vs. Time for particle %i" % p)
    plt.show()


def traj(p,x,y):
    plt.plot(x[:,p],y[:,p])
    plt.text(x[0, p], y[0, p], "Start")
    plt.text(x[-1, p], y[-1, p], "End")
    plt.xlabel("X-Location (pixels)")
    plt.ylabel("Y-Location (pixels)")
    plt.title("X vs. Y locations for particle %i" % p)
    plt.show()


print("DISCLAIMER: Please ensure that your 'spots.csv' file is sorted by frame A-Z, using the Filter Sort function!")
file_path = input("\nPlease enter your file path")
q1,file_path,q2 = file_path.split('"')
df = pd.read_csv(file_path,skiprows=3)

# Column 3 (index:2) has the spot no.
# Columns 5,6 (indices:4,5) have x,y displacements

# Initialize lists for dynamic storage
nspots = max(df.iloc[:,2]) + 1
xloc = [[] for _ in range(nspots)]
yloc = [[] for _ in range(nspots)]

# Populate lists
print("Populating Lists...")
for i in tqdm(range(len(df))):
    tempx = int(df.iloc[i,2])
    xloc[tempx].append(df.iloc[i,4])
    yloc[tempx].append(df.iloc[i,5])
    time.sleep(0.00001)

# Convert lists to NumPy arrays
xloc = [np.array(x) for x in xloc]
yloc = [np.array(y) for y in yloc]
# Transpose lists for ease of access --> [frame,particle]
xloc = np.transpose(xloc)
yloc = np.transpose(yloc)
frames = int(np.size(xloc[:,0]))

print("\n This is what the first frame looks like. Remember to save this on the side!")
plt.scatter(xloc[0],yloc[0])
for i in range(0,nspots):
    plt.text(float(xloc[0][i]),float(yloc[0][i]),i)
plt.xlabel("X-location (pixels)")
plt.ylabel("Y-location (pixels)")
plt.title("Exact particle locations at frame 0\n Close window to continue")
plt.show()

running = True
while running:
    print(running)
    ptrack()
    q = input("\n Would you like to view something else?(Y/N)\n")
    if q == "Y" or q == "y" or q == "Yes" or q == "yes":
        running = True
    elif q == "N" or q == "n" or q == "No" or q == "no":
        running = False
    else:
        print("\n You deserve to start over.")
        running = False