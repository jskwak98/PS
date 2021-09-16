def solution():
    """
    if length(digits whatever) is different, there must be at least one number without 8
    if len(l) == len(r), you only need to consider greedily from the largest digit,
    if they are same and 8, there must be at least one eight.
    you examine through all digits starting from the largest digit, and whenever
    l[i] != r[i] you break and don't need to consider subsequent digits.
    then just print the count of 8
    """
    l, r = input().split()
    if len(l) != len(r):
        print(0)
    else:
        count = 0
        for i in range(len(l)):
            if l[i] == r[i]:
                if l[i] == '8':
                    count += 1
                else:
                    continue
            else:
                break
        print(count)


solution()