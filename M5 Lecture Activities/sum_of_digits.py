# Module 4 Lecture Activity 3

def sum_of_digits(num):
    string = str(num)
    total = 0
    for char in string:
        total += int(char)
    print(total)

sum_of_digits(765434567)