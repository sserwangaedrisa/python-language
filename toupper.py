before = input('Before: ')
print('After: ', end='')
for c in before:
    print(c.upper(), end='')


print()

# Alternative
wordBefore = input('What is the word: ')
print(wordBefore.upper())
# Another alternative
# x = wordBefore.toupper()
# print(f'Uppercase word: {x}')