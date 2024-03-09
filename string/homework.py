#https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
def swap_case(s):
    swap_string = ""
    for letter in s:
        if letter.isupper():
            swap_string+=letter.lower()
        else:
            swap_string+=letter.upper()
    return swap_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


#https://www.hackerrank.com/challenges/python-string-split-and-join/problem?isFullScreen=true
def split_and_join(line):
    # write your code here
    new_split = "-".join(line.split())
    return new_split

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true
def print_full_name(first, last):
    # Write your code here
    string_print = f"Hello {first} {last}! You just delved into python."
    print(string_print)


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true
def mutate_string(string, position, character):
    new_string = string[:position]+character+string[position+1:]
    return new_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)


#https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true
def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if sub_string in string[i:i + len(sub_string)]:
            count += 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)


#https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
if __name__ == '__main__':
    s = input()
    check_number = False
    check_alpha = False
    check_digit = False
    check_lower = False
    check_upper = False
    for letter in s:
        if letter.isalnum():
            check_number = True
        if letter.isalpha():
            check_alpha = True
        if letter.isdigit():
            check_digit = True
        if letter.islower():
            check_lower = True
        if letter.isupper():
            check_upper = True
    print(check_number)
    print(check_alpha)
    print(check_digit)
    print(check_lower)
    print(check_upper)


#https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true
#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


#https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
import textwrap

def wrap(string, max_width):
    len_str = len(string)
    wrap = ""
    for i in range(0, len_str, max_width):
        if i+max_width<=len_str:
            wrap = wrap+string[i:i+max_width]+"\n"
        else:
            wrap+=string[i:]
    return wrap
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)


#https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true
def print_formatted(number):
    width = len(bin(number)[2:])
    for i in range(1, number+1):
        deci = str(i)
        octa =oct(i)[2:]
        hexa = hex(i)[2:].upper()
        bina = bin(i)[2:]
        print(deci.rjust(width), octa.rjust(width), hexa.rjust(width),bina.rjust(width))
    # your code goes here

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


#https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
def print_rangoli(size):
    number_row_line = size*4-1
    row = []
    for i in range(size):
        list_letter = [chr(97+size-1-j) for j in range(i+1)]
        if len(list_letter)>1:
            new_text = list_letter[0:len(list_letter)-1]
            new_text.reverse()
            row.append(list_letter+new_text)
        else:
            row.append(list_letter)

    new_row = row.copy()
    for i in range(len(row)-2,-1,-1):
        row.append(new_row[i])

    for i in row:
        text_to_display = "-".join(i)
        number_ = number_row_line - len(text_to_display)
        text = "-"*(int(number_/2)-1)+text_to_display+"-"*(int(number_/2)-1)
        print(text)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


#https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
def solve(s):
    text_split = s.split(" ")
    capitalize = []
    for text in text_split:
        capitalize.append(text.capitalize())
    return ' '.join(capitalize)

if __name__ == '__main__':
    import os
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
def minion_game(string):
    vovel = "AEOUI"
    count_kevin = 0
    count_suart = 0
    for num, letter in enumerate(string):
        if letter in vovel:
            count_kevin += len(string) - num
        else:
            count_suart += len(string) - num
    if count_kevin > count_suart:
        print("Kevin", count_kevin)
    elif count_kevin < count_suart:
        print("Stuart", count_suart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)


#https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        string_new = string[i:i+k]
        string_list= string_new
        char = ""
        for j in string_new:
            if j in string_list:
                char+=j
                string_list = string_list.replace(j,"")
        print(char)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)