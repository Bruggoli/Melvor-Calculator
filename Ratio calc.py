import random
import statistics

starting_resources = int(input())
d = int(input())
s = int(input())
xp = int(input())
ITERATIONS = 1000
total_list = []
total_xp_list = []
total_xp = 0



for i in range(ITERATIONS):
    processed_resources = 0
    while starting_resources > 0:
        double = random.randint(1, 100)
        if double <= d:
            processed_resources += 2
        else:
            processed_resources += 1
        save = random.randint(1, 100)
        if save <= s:
            starting_resources += 1
            total_xp += xp
        starting_resources -= 1
        total_xp += xp
    if starting_resources == 0:
        total_xp_list.append(total_xp)
        starting_resources = 100
        total_xp = 0
    total_list.append(processed_resources)

print("Resource gains: ", statistics.mean(total_list) - starting_resources)
print("XP gained: ", statistics.mean(total_xp_list))
