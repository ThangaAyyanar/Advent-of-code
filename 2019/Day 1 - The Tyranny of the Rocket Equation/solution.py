import os

def fuel_required(mass):
    round_of = int(mass/3)
    return round_of-2

def fuel_requires_fuel(mass,total_fuel):
    if mass <= 0:
        return total_fuel
    else:
        return fuel_requires_fuel(fuel_required(mass),mass+total_fuel)

def total_fuel_required(mass_array):
    fuel = 0
    for mass_str in mass_array:
        mass = int(mass_str)
        # part 1 
        # fuel += fuel_required(mass)

        #part 2
        first_fuel = fuel_required(mass)
        fuel += fuel_requires_fuel(first_fuel,0)
    return fuel

with open('input.txt', "r") as input:
    lines = input.read().splitlines()
    print(total_fuel_required(lines))

#test
# print(total_fuel_required([1969,100756]))
