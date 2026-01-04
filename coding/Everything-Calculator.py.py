from math import pi, e, sqrt, sin, cos, tan, asin, acos, atan, atan2, degrees, radians
from math import log, log10, log2, exp, factorial, floor, ceil
from math import pow, fmod, hypot
from math import sinh, cosh, tanh, asinh, acosh, atanh, gamma


def calculator():
    while True: 
        print("=== Calculator ===")
        result = eval(input("Calculate here (enter 'q' to quit): "))
        print(f"The result is {result}\n")
        

def geometry_calculator():
    while True:
        print("=== Geometry Calculator ===")
        print("Available shapes: square, rectangle, circle, triangle, trapezium, cube, cuboid, sphere, cylinder")
        shape = input("Choose a geometrical shape (or 'q' to return to main menu): ").lower()

        if shape == "q":
            return  # go back to main menu

        elif shape == "square":
            length = float(input("Enter the length of the square: "))
            area = length ** 2
            perimeter = 4 * length
            print(f"Area: {area}, Perimeter: {perimeter}\n")

        elif shape == "rectangle":
            length = float(input("Enter the length: "))
            breadth = float(input("Enter the breadth: "))
            area = length * breadth
            perimeter = 2 * (length + breadth)
            print(f"Area: {area}, Perimeter: {perimeter}\n")

        elif shape == "circle":
            radius = float(input("Enter the radius: "))
            area = pi * radius**2
            circumference = 2 * pi * radius
            print(f"Area: {area}, Circumference: {circumference}\n")

        elif shape == "triangle":
            x = input("Do you want to give three sides or base & height? (Enter 'sides' or 'base-height'): ").lower()
            if x == "sides":
                a = float(input("Enter side a: "))
                b = float(input("Enter side b: "))
                c = float(input("Enter side c: "))
                s = (a + b + c) / 2
                area = sqrt(s * (s - a) * (s - b) * (s - c))
                perimeter = a + b + c
                print(f"Area: {area}, Perimeter: {perimeter}\n")
            elif x == "base-height":
                base = float(input("Enter the base: "))
                height = float(input("Enter the height: "))
                area = 0.5 * base * height
                print(f"Area: {area}")
                print("Perimeter cannot be calculated with only base & height.\n")
            else:
                print("Invalid choice.\n")

        elif shape == "trapezium":
            a = float(input("Enter the first base: "))
            b = float(input("Enter the second base: "))
            height = float(input("Enter the height: "))
            area = 0.5 * (a + b) * height
            print(f"Area: {area}\n")

        elif shape == "cube":
            side = float(input("Enter the side length: "))
            area = 6 * side**2
            volume = side**3
            print(f"Surface Area: {area}, Volume: {volume}\n")

        elif shape == "cuboid":
            l = float(input("Enter length: "))
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            area = 2 * (l*w + l*h + w*h)
            volume = l * w * h
            print(f"Surface Area: {area}, Volume: {volume}\n")

        elif shape == "sphere":
            r = float(input("Enter the radius: "))
            area = 4 * pi * r**2
            volume = (4/3) * pi * r**3
            print(f"Surface Area: {area}, Volume: {volume}\n")

        elif shape == "cylinder":
            r = float(input("Enter the radius: "))
            h = float(input("Enter the height: "))
            area = 2 * pi * r * (r + h)
            volume = pi * r**2 * h
            print(f"Surface Area: {area}, Volume: {volume}\n")

        else:
            print("Shape not recognized. Try again.\n")

def profit_calculator():
    print("___=== Simple Profit/Principal Calculator ===___")
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest (in %): "))
    time = float(input("Enter the time (in years): "))
    profit = (principal * rate * time) / 100
    print(f"Profit: {profit}")
    print(f"Total Amount (Principal + Profit): {principal + profit}\n")

def temperature_converter():
    print("___=== Temperature Converter ===___")
    temp = float(input("Enter the temperature: "))
    unit = input("Is this in Celsius, Fahrenheit or Kelvin? (C/F/K): ").upper()

    if unit == "C":
        converted_in_F = (temp * 9/5) + 32
        converted_in_K = temp + 273.15
        print(f"{temp}°C is equal to {converted_in_F}°F\n")
        print(f"{temp}°C is equal to {converted_in_K}K\n")

    elif unit == "F":
        converted_in_C = (temp - 32) * 5/9
        converted_in_K = (temp - 32) * 5/9 + 273.15
        print(f"{temp}°F is equal to {converted_in_C}°C\n")
        print(f"{temp}°F is equal to {converted_in_K}K\n")

    elif unit == "K":
        converted_in_C = temp - 273.15
        print(f"{temp}K is equal to {converted_in_C}°C\n")
        converted_in_F = (temp - 273.15) * 9/5 + 32
        print(f"{temp}K is equal to {converted_in_F}°F\n")

    else:
        print("Invalid unit. Please enter C or F.\n")

def show_menu():
    print("___=== Choose what you wanna use ===___")
    print("1. Calculator")
    print("2. Geometry Calculator")
    print("3. Simple Profit/Principal Calculator")
    print("4. Temperature Converter")
    print("Other complex features are coming soon!\n")
    return input('Enter your choice (Enter "q" to quit): ')


while True:
    choice = show_menu()
    if choice == "1":
        calculator()
    elif choice == "2":
        geometry_calculator()
    elif  choice == "3":
        profit_calculator()
    elif choice == "4":
        temperature_converter()
    elif choice.lower() == "q":
        print("Bye! Thanks for using.")
        break
    else:
        print("Invalid choice.\n")
