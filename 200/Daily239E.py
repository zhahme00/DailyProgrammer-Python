# https://www.reddit.com/r/dailyprogrammer/comments/3r7wxz/20151102_challenge_239_easy_a_game_of_threes/
#
# Write a program that plays the Threes game, and outputs a valid sequence of steps you need 
# to take to get to 1. Each step should be output as the number you start at, followed by either
# -1 or 1 (if you are adding/subtracting 1 before dividing), or 0 (if you are just dividing). 
# The last line should simply be 1.

def main(n):
    d = 0
    while n > 1:
        if n % 3 == 0:
            d = 0
        elif (n + 1) % 3 == 0:
            d = 1
        else:
            d = -1
        print(n, d)
        n = (n + d) // 3
    print(n)
    
if __name__ == '__main__':
    main(31337357)
