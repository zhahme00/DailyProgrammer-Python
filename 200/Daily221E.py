def snake_print(words):
    # Horizontal, vertical, (left | right) horizonal...
    space_count = 0
    for i, word in enumerate(words):
        if i % 2 == 0:
            if len(word) > space_count:
                # go right
                print(space_count * ' ', word, sep='')
                space_count += len(word) - 1
            else:
                # go left
                space_count -= len(word) - 1
                print(space_count * ' ', word[::-1], sep='')
        else:
            # When printing vertically, always skip the first character. Always skip
            # the last character too unless printing the last vertical word.
            last_index = None if i == len(words) - 1 else -1
            for letter in word[1:last_index]:
                print(space_count * ' ', letter, sep='')

default_text = 'SHENANIGANS SALTY YOUNGSTER ROUND DOUBLET TERABYTE ESSENCE EAR RAINBOW \
                WISDOM MOM MISSION NEVERLAND DOG GAMEBOY'
text = input('Enter snake sequence: ')
snake_print(text.split() if len(text) > 0 else default_text.split())

