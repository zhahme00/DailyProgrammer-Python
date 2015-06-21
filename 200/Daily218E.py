# http://www.reddit.com/r/dailyprogrammer/comments/38yy9s/20150608_challenge_218_easy_making_numbers/

def Palindrome(number):
    s = str(number)
    i = 0
    length = len(s)
    while (i <= length - 1) and (s[i] == s[length - 1 - i]):
        i += 1
        if (i > length - i):
            return True

    return False


MAX_ITERATION = 1000
mutated_number = input_number = 196196871 

for i in range(0, MAX_ITERATION):
    if Palindrome(mutated_number):
        print("{} gets palindromic after {} steps: {}".format(input_number, i, mutated_number))
        break

    mutated_number = int(str(mutated_number)[::-1]) + mutated_number
