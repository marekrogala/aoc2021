with open("example1a.txt") as file:
    lines = file.readlines()
    lines = [int(line.rstrip()) for line in lines]


count = 0
print(lines)
print(sum(lines[i] > lines[i-1] for i in range(1, len(lines))))

sliding_sum = [lines[i]+lines[i-1]+lines[i-2] for i in range(2, len(lines))]
print(sliding_sum)
print(sum(sliding_sum[i] > sliding_sum[i-1] for i in range(1, len(sliding_sum))))