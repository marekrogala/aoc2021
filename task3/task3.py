with open("input3.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

n=len(lines)
half=n/2
m=len(lines[0])
print(n)
count = [0] * m
for l in lines:
    for i in range(m):
        count[i]+=int(l[i])

res1, res2 = 0, 0
for i in range(m):
    #print(count[i])
    res1 *= 2
    res2 *= 2
    if(count[i]>half):
        res1 += 1
    elif count[i]*2==n:
        print("EVEN!!!")
    else:
        res2 += 1

print(res1, res2, res1*res2)