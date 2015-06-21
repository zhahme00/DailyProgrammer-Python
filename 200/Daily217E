# http://www.reddit.com/r/dailyprogrammer/comments/3840rp/20150601_challenge_217_easy_lumberjack_pile/

# input
n = 3
log_count = 7
log_stacks = [1, 1 , 1 , 2 , 1 , 3 , 1 , 4, 1]

smallest = min(log_stacks)
while log_count > 0:
    for i, s in enumerate(log_stacks):
        if s == smallest:
            log_stacks[i] += 1
            log_count -= 1
            if log_count == 0:
                break

    smallest += 1

# print n by n
for i, s in enumerate(log_stacks, 1):
    seperator = '\n' if i % n == 0 else ' '
    print(s, end=seperator)
