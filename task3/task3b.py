with open("input3.txt") as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

def find(numbers, pos, o2):
    if(len(numbers) == 1):
        return numbers[0]
    count_ones = sum(int(number[pos])==1 for number in numbers)
    if o2:
        expected_bit = 1 if count_ones*2>=len(numbers) else 0
    else:
        expected_bit = 0 if count_ones*2>=len(numbers) else 1
    filtered = [number for number in numbers if int(number[pos])==expected_bit]
    return find(filtered, pos+1, o2)


o = int(find(lines, 0, True), 2)
c = int(find(lines, 0, False), 2)
print(o, c, o*c)