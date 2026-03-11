import matplotlib.pyplot as plt
import numpy as np
def rocket_launch(mass, thrust):
    velocity = 0
    time = 0
    gravity = 9.8
    height = 0
    heights = np.array([])
    times = np.array([])
    drymass = 0.1*mass

    print("3,2,1!")
    print("Launch Initiated!")
    
    while mass > drymass:
        acceleration = thrust/mass - gravity
        velocity = velocity + acceleration
        height = height + velocity
        time = time + 1 
        mass = mass - 1 
        
        heights = np.append(heights, height) 
        times = np.append(times,  time)

        

    plt.plot(times, heights) 
    plt.xlabel("Time(s)") 
    plt.ylabel("Height(y)") 
    plt.title("Rocket Launch") 
    plt.show()

    print(f"The rocket successfully reached a height of {height}")
    print(f"It took us {time} seconds")


