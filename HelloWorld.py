import random

x = input("What is your name? ")
print("Hello, " + x + "!")
y = str(random.randint(-10000, 10000))
print("Your lucky number is: " + y)

avg = 0
for x in range(1000):
    found = 0
    for i in range(10000):
        if random.randint(-100, 100) == 0:
            found = found + 1
    print("Percentage " + str(x) + ": " + str(found / 10000 * 100) + "%!")
    avg = avg + found / 10000 * 100
avg = avg / 1000
print("Percentage Average: " + str(avg))
