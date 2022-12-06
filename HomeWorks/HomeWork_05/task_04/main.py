# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Consider a screen containing plain black text on a solid white background. There will be many long runs of white pixels in the blank space, and many short runs of black pixels within the text. A hypothetical scan line, with B representing a black pixel and W representing white, might read as follows:
#
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# With a run-length encoding (RLE) data compression algorithm applied to the above hypothetical scan line, it can be rendered as follows:
#
# 12W1B12W3B24W1B14W

def rle (string):
    count = 1
    coded_string =""
    for i in range (1,len(string)):
        if string[i-1] == string[i]:
            count +=1
            if i == len(string)-1:
                coded_string = coded_string + str(count) + string[i - 1]
                break
        else:
            coded_string = coded_string + str(count) + string[i-1]
            count =1

    return (coded_string)

def rld (string):
    number_str = ""
    res_string = ""
    for i in range(len(string)):
        if string[i].isdigit():
            number_str = number_str + string[i]
        else:
            res_string =res_string + string[i]*int(number_str)
            number_str = ""
    return res_string


string1 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW"

print(string1)
string2 = rle(string1)
print(string2)
print(rld(string2))