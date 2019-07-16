string = input("enter the string")
length = len(string)
temp_list = []
longest_substring_list = []
longest_length = 0
i = 0
flag = 0
for j in range(i, length):
    if flag == 1:
        break;
    for i in range(j, length):
        if string[i] not in temp_list:
            temp_list.append(string[i])
            if i - j + 1 > longest_length:
                start_index = j
                last_index = i
                longest_length = i - j + 1
                # print(temp_list)
                if i == length - 1:
                    flag = 1
        else:
            if i == length - 1:
                flag = 1
            temp_list.clear()
            break

for a in range(start_index, last_index + 1):
    longest_substring_list.append(string[a])

str = ""
print(str.join(longest_substring_list), end="")
print(" is the longest substring at index from {0} to {1}".format(start_index, last_index))
