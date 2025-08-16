import sys
import math
import numpy as np
import matplotlib.pyplot as plt

D2R = np.pi/180.0
R2D = 180.0/np.pi

class pose_class:
    def __init__(self, pt=[0.0, 0.0], heading_deg=0.0, state=0):
        self.pt_UTM = pt
        self.heading_deg = heading_deg
        self.state = state
        
# ---------------------------------------------------------------
# make sure the name of the input and output files were specified
if len(sys.argv) != 2:
   print('useage:  plot_pose_list.py input_file.txt\n')
   exit()
   
# ---------------------------------------------------------------
# make sure the input file exists and can be opened 

input_file = sys.argv[1]

try:
    a_file = open(input_file)
except IOError:
    print ("Could not open the file ", sys.argv[1])
    exit()

stream = open(input_file, 'r')
# ---------------------------------------------------------------
pose_list = []

while True:
    line = stream.readline()
    if not line:
        break ;
        
    if(line[0] != '#' ):  # this will eliminate comment lines
        split_text  = line.split(',')

        if len(split_text) == 4 :
            new_pose = pose_class(pt=[float(split_text[0]), float(split_text[1])], \
                                  heading_deg=float(split_text[2]), \
                                  state=int(split_text[3].strip('\n')))
            pose_list.append(new_pose)

#num_poses = len(pose_list)
#print(num_poses)
#for i in range (num_poses):
#    print(f'{pose_list[i].pt_UTM}, {pose_list[i].heading_deg}, {pose_list[i].state}')

# ---------------------------------------------------------------
# now draw the poses

plt.figure()

xh = [0.0, 0.0]  # allocate variables
yh = [0.0, 0.0]
for pose in pose_list:
    c1 = plt.Circle((pose.pt_UTM[0], pose.pt_UTM[1]), 0.5, color='black')
    xh[0] = pose.pt_UTM[0]
    yh[0] = pose.pt_UTM[1]
    xh[1] = xh[0] + 1.0*math.cos(pose.heading_deg*D2R)
    yh[1] = yh[0] + 1.0*math.sin(pose.heading_deg*D2R)
    plt.gca().add_artist(c1)
    plt.plot(xh,yh, color='turquoise')

# now draw a line connecting the poses in order
xline = []
yline = []
for pose in pose_list:
    xline.append(pose.pt_UTM[0])
    yline.append(pose.pt_UTM[1])
plt.plot(xline, yline, color = 'darkred')

plt.xlabel('UTM Easting (m)')
plt.ylabel('UTM Northing (m)')
plt.axis('equal')
plt.show(block = True)