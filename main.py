import random

# Generate a list of 30 houses
# Random numbers represent distance from eastern endpoint
house_list = []
for i in range(0, 30):
    house_list.append(random.randint(1,99))

# sort houses by distance from eastern endpoint
house_list = sorted(house_list)

# place first base station 4 miles west of eastern most house
base_station = house_list[0] + 4
num_base_stations = 1

# if current house is greater than 4 miles from the last placed base station
# add a new base station 4 miles west of current house
for i in range(1, len(house_list)):
    if abs(base_station - house_list[i]) > 4:
        base_station = house_list[i] + 4
        num_base_stations += 1
        
print("Base stations needed: {}".format(num_base_stations))

