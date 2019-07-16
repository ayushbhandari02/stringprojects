string = input("enter the string for which you want to find the longest substring without repetition")
flag = 0
for x in range(1, len(string)):
    for x in range(1, len(string)):
        if flag == 1:
            break
        for y in range(x - 1, -1, -1):
            if (string[x] == string[y]):
                index = x
                flag = 1
            else:
                continue
for x in range(index):
    print(string[x], end="")
print(" is the longest substring without repetition")

