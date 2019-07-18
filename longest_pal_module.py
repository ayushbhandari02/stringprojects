def longest_palindrome_func(string):
    length = len(string)
    length_palindrome = 0
    for i in range(length):
        if length_palindrome > length - i:
            break
        temp_start_index = i
        for j in range(i + 1, length):
            temp_last_index = j
            while string[i] == string[j]:
                if i == j or j == i + 1:
                    if temp_last_index - temp_start_index + 1 > length_palindrome:
                        start_index = temp_start_index
                        last_index = temp_last_index
                        length_palindrome = temp_last_index - temp_start_index + 1
                    break
                i += 1
                j -= 1
            i = temp_start_index
            j = temp_last_index

    return string[start_index:(last_index + 1)]


