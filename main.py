import math

def show_home_screen():
    print("==== Home Screen ====")
    print("1. Basic Calculator")
    print("2. Law of Sines Calculator")
    print("3. Law of Cosines Calculator")
    print("4. Pi to Radians/Radians to Pi Calculator")
    print("5. Scientific Unit Conversion Calculator")
    print("0. Exit")
    print("=====================")

def basic_calculator():
    print("==== Basic Calculator ====")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    operation = int(input("Enter operation number: "))

    if operation == 1:
        result = num1 + num2
        print(f"Result: {result}")
    elif operation == 2:
        result = num1 - num2
        print(f"Result: {result}")
    elif operation == 3:
        result = num1 * num2
        print(f"Result: {result}")
    elif operation == 4:
        result = num1 / num2
        print(f"Result: {result}")
    else:
        print("Invalid operation")

def law_of_sines_calculator():
    print("==== Law of Sines Calculator ====")
    side_a = float(input("Enter the length of side a: "))
    angle_A = float(input("Enter the measure of angle A in degrees: "))
    side_b = float(input("Enter the length of side b: "))

    # Convert the angle from degrees to radians
    angle_A_rad = math.radians(angle_A)

    # Use the Law of Sines to calculate angle B
    angle_B_rad = math.asin((side_b * math.sin(angle_A_rad)) / side_a)

    # Convert angle B back to degrees
    angle_B = math.degrees(angle_B_rad)

    # Calculate angle C (sum of angles in a triangle is 180 degrees)
    angle_C = 180 - angle_A - angle_B

    # Use the Law of Sines to calculate side C
    side_c = (side_a * math.sin(math.radians(angle_C))) / math.sin(angle_A_rad)

    print(f"Angle B: {angle_B} degrees")
    print(f"Angle C: {angle_C} degrees")
    print(f"Side c: {side_c}")

def law_of_cosines_calculator():
    print("==== Law of Cosines Calculator ====")
    side_a = float(input("Enter the length of side a: "))
    side_b = float(input("Enter the length of side b: "))
    angle_C = float(input("Enter the measure of angle C in degrees: "))

    # Convert the angle from degrees to radians
    angle_C_rad = math.radians(angle_C)

    # Use the Law of Cosines to calculate side C
    side_c = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_C_rad))

    print(f"Side c: {side_c}")

def pi_to_radians_calculator():
    print("==== Pi to Radians/Radians to Pi Calculator ====")
    print("1. Pi to Radians")
    print("2. Radians to Pi")

    option = int(input("Enter option number: "))

    if option == 1:
        pi_value = float(input("Enter the value of pi: "))
        radians = pi_value * math.pi
        print(f"Radians: {radians}")
    elif option == 2:
        radians_value = float(input("Enter the value in radians: "))
        pi = radians_value / math.pi
        print(f"Pi: {pi}")
    else:
        print("Invalid option")

def scientific_unit_conversion_calculator():
    print("==== Scientific Unit Conversion Calculator ====")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Kilometers to Miles")
    print("4. Miles to Kilometers")

    option = int(input("Enter option number: "))

    if option == 1:
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = (celsius * 9/5) + 32
        print(f"Temperature in Fahrenheit: {fahrenheit}°F")
    elif option == 2:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5/9
        print(f"Temperature in Celsius: {celsius}°C")
    elif option == 3:
        kilometers = float(input("Enter the distance in kilometers: "))
        miles = kilometers * 0.621371
        print(f"Distance in Miles: {miles} miles")
    elif option == 4:
        miles = float(input("Enter the distance in miles: "))
        kilometers = miles * 1.60934
        print(f"Distance in Kilometers: {kilometers} kilometers")
    else:
        print("Invalid option")

# Main program
while True:
    show_home_screen()
    option = int(input("Enter option number: "))

    if option == 0:
        print("Exiting...")
        break
    elif option == 1:
        basic_calculator()
    elif option == 2:
        law_of_sines_calculator()
    elif option == 3:
        law_of_cosines_calculator()
    elif option == 4:
        pi_to_radians_calculator()
    elif option == 5:
        scientific_unit_conversion_calculator()
    else:
        print("Invalid option")
