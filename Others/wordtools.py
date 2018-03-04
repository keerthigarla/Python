
from collections import Counter
def white_space():
    import re
    filename = input('Enter text: ')
    with open(filename, 'rt') as  f:
        return re.findall('\w+', f.read())

words = white_space()
print(words)

def first(word):
    return word[0]
def last(word):
    return word[-1]
def middle(word):
    return word[1:-1]

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome('keerthi'))
print(is_palindrome('kayak'))

def count_let():
    str = input('Enter a string')
    c={}
    c = Counter(str)
    return c
print(count_let())

def word_freq():
    words = white_space()
    counts ={}
    for word in words:
        counts[word]  = counts.get(word,0) + 1
    return counts
print(word_freq())
