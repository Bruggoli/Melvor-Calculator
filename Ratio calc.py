import random
import statistics
from datetime import timedelta

starting_resources = int(input("Starting resources: "))
r_cycle = starting_resources
double = int(input("Doubling chance: "))
save = int(input("Saving chance: "))
xp = int(input("XP per action: "))
crafting_time = float(input("Time per crafting cycle: "))
ITERATIONS = 100
total_list = []
total_xp_list = []
total_xp = 0
crafting_cycles = 0
c_c_list = []

for i in range(ITERATIONS):
    processed_resources = 0
    while starting_resources > 0:
        double_roll = random.randint(1, 100)
        if double_roll <= double:
            processed_resources += 2
        else:
            processed_resources += 1
        save_roll = random.randint(1, 100)
        if save_roll <= save:
            starting_resources += 1
            total_xp += xp
        starting_resources -= 1
        crafting_cycles += 1
        total_xp += xp
    if starting_resources == 0:
        total_xp_list.append(total_xp)
        starting_resources = r_cycle
        total_xp = 0
        c_c_list.append(crafting_cycles)
        crafting_cycles = 0
        total_list.append(processed_resources)

resource_increase = round(((statistics.mean(total_list) - starting_resources) / starting_resources) * 100, 2)

print("% resource increase from base ", "{:,}".format(resource_increase), "%")
print("Resources produced: ", "{:,}".format(round((statistics.mean(total_list)), 2)))
print("XP gained: ", "{:,}".format(round(statistics.mean(total_xp_list), 2)))
print("Crafting time: ", str(timedelta(seconds=crafting_time * round(statistics.mean(c_c_list)))))
