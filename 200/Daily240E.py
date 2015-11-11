# https://www.reddit.com/r/dailyprogrammer/comments/3s4nyq/20151109_challenge_240_easy_typoglycemia/

import random

def scramble_sentence(sentence):
    '''Scrambles each word of a sentence and returns a '''
    scrambled = map(lambda w: scramble_word(w), sentence.split(' '))
    return ' '.join(scrambled)

def scramble_word(word):
    '''Scrambles a word but leaves the first 
        and last letter of the word intact.'''
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
    else:
        s = scramble_word_segment(''.join(l))
        scrambled.append(s)
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

if __name__ == '__main__':    
    i = '''
    According to a research team at Cambridge University, it doesn't matter in what order the letters in a word are, 
    the only important thing is that the first and last letter be in the right place. 
    The rest can be a total mess and you can still read it without a problem.
    This is because the human mind does not read every letter by itself, but the word as a whole. 
    Such a condition is appropriately called Typoglycemia.'''
    s = scramble_sentence(i)
    print(s)
