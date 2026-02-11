rover_status ={
    "Battery": 100,
    "Heater": "off",
    "Camera": "standby"
}
print(rover_status["Battery"])

#status update
rover_status["Battery"] = 85
print(rover_status["Battery"])
rover_status["Heater"] = "on"
print(rover_status["Heater"])
rover_status["Speed"] = "5"
print(rover_status["Speed"])

mission_log1 = {
    "Site": "Crater A",
    "Radiation": "Low",
    "Water": False
}
mission_log2 = {
    "Site": "Dune B", 
    "Radiation": "High", 
    "Water": True
}
mission_logs = [mission_log1, mission_log2]
for log in mission_logs:
    print("Site " + log["Site"] + " has " + log["Radiation"] + " radiation.")


