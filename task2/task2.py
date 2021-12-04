with open("input2.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

horizontal, vertical, aim = 0, 0, 0
for l in lines:
    a, b = l.split(" ")
    if (a == "forward"):
        horizontal += int(b)
        vertical += aim*int(b)
    elif (a == "up"):
        aim -= int(b)
    else:
        aim += int(b)
    vertical = max(vertical, 0)

print(horizontal, vertical, horizontal*vertical)