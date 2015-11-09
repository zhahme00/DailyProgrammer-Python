import random

def scramble_sentence(sentence):
    words = sentence.split(' ')
    for w in words:
        print(w, scramble_word(w))

def scramble_word(word):
    scrambled = []    
    l = []
    for i in range(len(word)):    
        if word[i].isalpha():
            l.append(word[i])
        else:
            if len(l) == 0:
                scrambled.append(word[i])                
            else:
                s = scramble_word_segment(''.join(l))
                scrambled.append(s)
                scrambled.append(word[i])
                l = []
    return ''.join(scrambled)

def scramble_word_segment(word_segment):
    if len(word_segment) < 3:
        return word_segment
    l = list(word_segment)
    upperbound = len(l) - 1
    for current_index in range(1, upperbound):
        new_index = random.randrange(1, upperbound)
        l[current_index], l[new_index] = l[new_index], l[current_index]
    return ''.join(l)

# Does not work, yet!    
scramble_sentence('"\'Twas the best of time; the worst of time!"')
