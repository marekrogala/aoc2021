with open("input.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

numbers = list(map(int, lines.pop(0).split(",")))
n = len(lines[1].split())

bs=[]
while lines:
    lines.pop(0)
    b = []
    for i in range(n):
        b.append(list(map(int, lines.pop(0).split())))
    bs.append(b)

remaining_to_win = len(bs)
has_won = [False] * len(bs)
for num in numbers:
    for b, bi in zip(bs, range(len(bs))):
        if not has_won[bi]:
            for i in range(n):
                for j in range(n):
                    if b[i][j] == num:
                        b[i][j] = None
                        if all(b[i][k] is None for k in range(n)) or all(b[k][j] is None for k in range(n)):
                            remaining_to_win -= 1
                            has_won[bi] = True
                            if remaining_to_win == 0:
                                rest = 0
                                print(b)
                                for sublist in b:
                                    for item in sublist:
                                        if item is not None:
                                            rest += item
                                print(num, rest, num*rest)
                                import sys
                                sys.exit()
