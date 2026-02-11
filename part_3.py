
motor_speed = input("Enter Motor Speed: ")
try:
    motor_speed = int(motor_speed)
    print("speed set to " + str(motor_speed))
except ValueError:
    print("Error: Corrupted Signal. Maintaining current speed.")

while True:
    x = input("Enter X coordinate:")
    y = input("Enter Y coordinate:")
    try:
        x = int(x)
        y = int(y)
        print("Coordinates set to (" + str(x) + ", " + str(y) + ")")
        break
    except ValueError:
        print("Invalid coordinate")

if motor_speed < -100 or motor_speed > 100:
    print("Motor speed out of range")
else:
    print("Motor speed is within safe range")
