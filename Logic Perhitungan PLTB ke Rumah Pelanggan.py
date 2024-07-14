import math

# Constants
AIR_DENSITY = 1.225  # kg/m^3, density of air
EFFICIENCY = 0.4  # efficiency of the wind turbine
BLADE_RADIUS = 20  # meters, radius of the wind turbine

# Function to calculate the power produced by a wind turbine
def calculate_wind_power(wind_speed, blade_radius=BLADE_RADIUS, efficiency=EFFICIENCY):
    swept_area = math.pi * blade_radius**2
    power = 0.5 * AIR_DENSITY * swept_area * (wind_speed ** 3) * efficiency
    return power

# Function to calculate power loss in transmission lines
def calculate_transmission_loss(power, distance, resistance_per_km=0.05):
    loss = power * resistance_per_km * distance
    return loss

# Function to calculate the power received by each house
def power_to_houses(total_power, number_of_houses):
    power_per_house = total_power / number_of_houses
    return power_per_house

# Manual Input
wind_speed = float(input("Masukkan kecepatan angin (m/s): "))
distance_to_houses = float(input("Masukkan jarak ke rumah-rumah (km): "))
number_of_houses = int(input("Masukkan jumlah rumah: "))

# Step 1: Calculate the power produced by the wind turbines
wind_power = calculate_wind_power(wind_speed)

# Step 2: Calculate the power loss in transmission
transmission_loss = calculate_transmission_loss(wind_power, distance_to_houses)

# Step 3: Calculate the power received by the houses
power_after_loss = wind_power - transmission_loss
power_per_house = power_to_houses(power_after_loss, number_of_houses)

# Output results
print(f"Total Daya yang Dihasilkan oleh Turbin Angin: {wind_power:.2f} W")
print(f"Rugi-rugi Daya dalam Transmisi: {transmission_loss:.2f} W")
print(f"Daya yang Diterima oleh Setiap Rumah: {power_per_house:.2f} W")