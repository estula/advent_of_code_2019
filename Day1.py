import math

fuelsum = 0
file1 = open("Day1_input.txt")
masses = file1.readlines()
for x in masses:
    fuel = math.floor(int(x) / 3) - 2
    fuelfuel = 0
    i = math.floor(fuel / 3) - 2
    while i > 0:
        fuelfuel += i
        i = math.floor(i / 3) - 2
    fuelsum += fuel + fuelfuel

print(fuelsum)



