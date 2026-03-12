import numpy as np
import matplotlib.pyplot as plt
class Rocket(): 
    def __init__(self, drymass, thrust, fuel):
        self.drymass = drymass 
        self.thrust = thrust 
        velocity = 0 
        self.times = np.zeros(fuel)
        self.heights = np.zeros(fuel)
        self.height = 0
        self.time = 0
        self.mass = drymass + fuel
        self.acceleration = 0
        self.velocity = 0
        self.i = 0 

        while fuel > 0: 
            self.acceleration = thrust/self.mass - 9.8
            self.velocity += self.acceleration
            self.height += self.velocity
            self.time += 1
            self.heights[self.i] = self.height
            self.times[self.i] = self.time
            fuel -= 1 
            self.mass -= 1
            self.i += 1

        

        print(f"Congratulaitons, the rocket reached a height of {self.height} and time of {self.time}")
        plt.plot(self.times, self.heights)
        plt.xlabel("Time(s)")
        plt.ylabel("Height(m))")
        plt.title("Graphical Representation")
        plt.show()

        
        
    def twr(self):
        return self.thrust/ (self.drymass*9.8) 
    
    def is_powerful (self):
        if self.twr() > 1:  
            return True 
        else: 
            return False
    def __str__(self):
        return f"Mass : {self.drymass}  Thrust: {self.thrust} TWR: {self.twr()}"
    
Xrocket = Rocket(500, 150000, 5000)
