def rocket_launch(mass, thrust, fuel):
    velocity = 0
    time = 0
    gravity = 9.8
    height = 0

    print("3,2,1!")
    print("Launch Initiated!")

    while fuel > 0:
        acceleration = thrust/mass - gravity
        velocity = velocity + acceleration
        height = velocity + height
        fuel = fuel - 1
        time = time + 1

    print(f"The rocket successfully reached a height of {height}")
    print(f"It took us {time} seconds")

rocket_launch(mass=1000, thrust=10000, fuel=260)
