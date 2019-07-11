list = []
while (1):
    try:
        list.append(input('enter the new element'))
    except exception:
        print("enter the valid input")
    if input('enter x to exit or enter to continue appending names') == 'x':
        break
    else:
        continue
min_length = len(min(list, key=len))
print(min_length)
length_list = len(list)
print(length_list)
flag = 0
common_index = -1
for i in range(min_length):

    for j in range(length_list - 1):
        print(j)
        if list[0][i] == list[j + 1][i]:
            continue
        else:
            flag = 1
    if flag == 1:
        break
    common_index = i
print(common_index)
if common_index == -1:
    print("no  prefix found!")
for k in range(common_index+1):
    print(list[0][k], end=" ")
if common_index == 0:
    print(" is the common prefix")
if common_index > 0:
    print("are the common prefix")
