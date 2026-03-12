import matplotlib.pyplot as plt
import numpy as np 
import math 

def rocket_launch(mass, thrust):
    velocity = 0
    time = 0
    gravity = 9.8
    height = 0
    drymass = 0.1*mass 
    heights = np.zeros(math.ceil(mass - drymass))
    times = np.zeros(math.ceil(mass - drymass))
    i = 0

    print("3,2,1!")
    print("Launch Initiated!")
    
    while mass > drymass:
        acceleration = thrust/mass - gravity
        velocity = velocity + acceleration
        height = height + velocity
        time = time + 1 
        mass = mass - 1  
        heights[i] = height 
        times[i] = time 
        i = i + 1

        

    plt.plot(times, heights) 
    plt.xlabel("Time(s)") 
    plt.ylabel("Height(y)") 
    plt.title("Rocket Launch") 
    plt.show()

    print(f"The rocket successfully reached a height of {height}")
    print(f"It took us {time} seconds")

