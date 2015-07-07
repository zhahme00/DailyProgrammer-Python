# https://www.reddit.com/r/dailyprogrammer/comments/3c9a9h/20150706_challenge_222_easy_balancing_words/

def balance(word):
    '''Returns None if word cannot be balanced; returns tuple of 
    (left side, balance point, right side, weight)'''
    weights = [ord(w) - ord('A') + 1 for w in word]   
    for index in range(1, len(word) - 1):
        # maybe the value for left sum would become clear 
        # if zip() and range(a,b,-1) were used instead
        left = sum([i * w for i, w in enumerate(weights[:index][::-1], 1)])
        right = sum([i * w for i, w in enumerate(weights[index + 1:], 1)])
        if left == right:
            return (word[:index], word[index], word[index + 1:], left)
        elif left > right:
            return None
    
words = ['STEAD', 'CONSUBSTANTIATION', 'WRONGHEADED', 'UNINTELLIGIBILITY', 
         'SUPERGLUE', '', 'A', 'AA', 'ABA', 'ABBA']
for w in words:
    res = balance(w)
    if not res:
        print(w, 'DOES NOT BALANCE')
    else:
        print(res[0], res[1], res[2], '-', res[3])
