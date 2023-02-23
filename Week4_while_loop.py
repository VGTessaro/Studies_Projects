count = 0
nums = []
while count < 15:
    if (count % 2) == 0:
        nums.append(count)
    count = count + 1
    print(count)

print(nums)


list1 = [8, 3, 4, 5, 6, 7, 9]

tot = 0
accum = 0

while tot < len(list1):
    accum = accum + list1[tot]
    tot = tot + 1

print(tot)
print(accum)


def stop_at_four(numlist):
    lis = []
    n = 0
    while n < len(numlist):
        if numlist[n] != 4:
            lis.append(numlist[n])
            n = n + 1
        else:
            break
    return lis


lista = (1,5,8,9,6,7,3,4)
print(stop_at_four(lista))