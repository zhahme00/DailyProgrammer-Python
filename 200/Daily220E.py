def scramble_words(words=[]):
    for w in words:
        sorted_chars = sorted([c.lower() for c in w if c.isalpha()])
        for i, c in enumerate(w):
            if not c.isalpha():
                sorted_chars.insert(i, c)
            elif c.isupper():
                sorted_chars[i] = sorted_chars[i].upper()

        print(''.join(sorted_chars), end=' ')
    print()

scramble_words("This challenge doesn't seem so hard.".split())
