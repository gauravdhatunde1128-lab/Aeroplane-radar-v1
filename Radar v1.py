import numpy as np
import matplotlib.pyplot as plt

print("\nAIRCRAFT RADAR SIMULATION SOFTWARE\n")

# ==============================
# USER INPUT
# ==============================
num_aircraft = int(input("Enter number of aircraft to track: "))
radar_range = float(input("Enter radar maximum range (km): "))

aircraft_positions = []

for i in range(num_aircraft):
    print(f"\nAircraft {i+1}")
    x = float(input("Enter X position (km): "))
    y = float(input("Enter Y position (km): "))
    aircraft_positions.append((x, y))

# ==============================
# RADAR CALCULATIONS
# ==============================
ranges = []
angles = []

for x, y in aircraft_positions:
    r = np.sqrt(x**2 + y**2)
    theta = np.degrees(np.arctan2(y, x))
    ranges.append(r)
    angles.append(theta)

# ==============================
# OUTPUT
# ==============================
print("\n----- RADAR DETECTION REPORT -----")
for i in range(num_aircraft):
    status = "DETECTED" if ranges[i] <= radar_range else "OUT OF RANGE"
    print(f"Aircraft {i+1}: Range = {ranges[i]:.2f} km | Angle = {angles[i]:.2f}° | {status}")

# ==============================
# RADAR DISPLAY (PPI)
# ==============================
plt.figure(figsize=(6,6))
plt.scatter(0, 0, c='red', label='Radar Station')

for i, (x, y) in enumerate(aircraft_positions):
    if ranges[i] <= radar_range:
        plt.scatter(x, y)
        plt.text(x, y, f"A{i+1}")
    else:
        plt.scatter(x, y, marker='x')

circle = plt.Circle((0,0), radar_range, fill=False, linestyle='--')
plt.gca().add_artist(circle)

plt.xlabel("X Position (km)")
plt.ylabel("Y Position (km)")
plt.title("Aircraft Radar Display (Plan Position Indicator)")
plt.legend()
plt.grid()
plt.axis('equal')
plt.show()
