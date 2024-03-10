#Task 1

import random

cpu_usage = random.randint(0, 100)
if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

#Task 2

import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

if memory_usage > 50:
    print("High Memory Usage")
else:
    pass

if disk_space < 500:
    print("Low Disk Space")
else:
    pass

#Task 3

import random

cpu_usage = random.randint(0, 100)
memory_usage = random.randint(0, 100)
disk_space = random.randint(0, 100)

if cpu_usage > 90:
    print("High CPU usage!")
elif cpu_usage > 80 and cpu_usage <= 90:
    pass

if memory_usage > 50:
    print("High Memory Usage")
elif memory_usage > 51 and memory_usage <= 60:
    pass

if disk_space < 500:
    print("Low Disk Space")
elif disk_space <= 499 and disk_space >= 400:
    pass