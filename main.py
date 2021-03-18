import random


# Generate a list of 30 houses
# Numbers represent distance from eastern endpoint
house_list = []
for i in range(0, 30):
    house_list.append(random.randint(1,99))
# sort houses by closest to eastern endpoint
house_list = sorted(house_list)
# place first base 4 miles west of eastern most house
base = house_list[0] + 4
num_bases = 1

# if mile marker of current house - mile marker of current base > 4
# add a new base 4 miles west
for i in range(1, len(house_list)):
    if abs(base - house_list[i]) > 4:
        base = house_list[i] + 4
        num_bases += 1
print("Towers needed: {}".format(num_bases))

