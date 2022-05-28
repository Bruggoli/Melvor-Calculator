import random
import statistics

starting_resources = int(input("Starting resources: "))
r_cycle = starting_resources
double = int(input("Doubling chance: "))
save = int(input("Saving chance: "))
xp = int(input("XP per action: "))
#crafting_time = float(input())
ITERATIONS = 10
total_list = []
total_xp_list = []
total_xp = 0
crafting_cycles = 0

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
    total_list.append(processed_resources)


print("% resource increase from base ", round((statistics.mean(total_list) - starting_resources), 2))  # fix this line to show % instead of difference
print("Resources produced: ", round((statistics.mean(total_list)), 2))
print("XP gained: ", round(statistics.mean(total_xp_list)), 2)
#print("Crafting cycles: ")
