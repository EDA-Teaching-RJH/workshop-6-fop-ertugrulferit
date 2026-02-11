
travel_log = []

while True:
    try:
        reading = input("Sensor Reading (Slope Angle): ")

        angle = float(reading)

        travel_log.append(angle)

        print(f"Travel log updated: {travel_log}")

    except ValueError:
        print("Sensor Glitch")
        
    if angle >= 45:
        print("CRITICAL TILT! HALTING.")
        print("Mission Terminated.")
        print(f"Total steps taken: {len(travel_log)}")
        print(f"Full travel log: {travel_log}")
        break
    else:
        print("Path Stable. Moving forward.")
   