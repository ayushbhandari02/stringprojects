string = input("enter the string")
temp_list = []
length = len(string)
longest_length = 0
for i in range(length):
    for j in range(i+1, length):

        if string[i] == string[j]:
            if j - i > longest_length:
                start_index = i
                last_index = j - 1
                longest_length = j - i
            break
        else:
            temp_list.append(string[j])
        if j == length - 1:
            if j - i + 1 > longest_length:
                longest_length = j - i + 1
            start_index = i
            last_index = j
            break
    if j == length - 1:
        break
for x in range(start_index,last_index + 1):
    print(string[x], end = "")
print(" is the longest substring")