import matplotlib.pyplot as plt
import numpy as np

app_discount = 3

initial_fuel_cost_pl = 1.35
initial_fuel_volume = 2
initial_fuel_cost = initial_fuel_volume*initial_fuel_cost_pl

secondary_fuel_cost_pl = 1.35
secondary_fuel_volumes = np.linspace(2,80,80)
fuel_bonus_percentages=[]
miles=[]

miles_per_tank = 400
tank_liters = 80
cost_of_tank = tank_liters*initial_fuel_cost_pl
fuel_efficiency_per_pound = miles_per_tank/cost_of_tank
fuel_efficiency_per_litre = miles_per_tank/tank_liters
distance_per_pound = miles_per_tank/cost_of_tank

for volume in secondary_fuel_volumes:
    secondary_fuel_cost = volume*secondary_fuel_cost_pl
    total_cost = initial_fuel_cost + secondary_fuel_cost
    fuel_bonus = total_cost/(total_cost - app_discount)
    fuel_bonus_percent = (fuel_bonus-1)*100
    fuel_bonus_percentages.append(fuel_bonus_percent)

    miles_to_drive = fuel_efficiency_per_litre*volume
    miles.append(miles_to_drive)

plt.figure(figsize=(10,5))
plt.plot(secondary_fuel_volumes, fuel_bonus_percentages, miles, label = "Fuel Bonus %", color='b')
plt.xlabel('Secondary Fuel Volume')
plt.ylabel('Fuel Bonus %')
plt.title('Fuel Bonus vs Secondary Fuel Volume')
plt.legend()
plt.grid()
plt.show()