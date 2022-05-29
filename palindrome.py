# palindrome using deque 

import ArrayDeque as AD

def strFilter(string):
    # remove everything except alphabets.
    from string import ascii_lowercase
    string = string.lower()
    store = ""
    for i in string:
        if i in ascii_lowercase:
            store += i
    return store

def palindrome(string):
    deque = AD.ArrayDeque()
    string = strFilter(string)

    for i in string:
        deque.append(i)

    while len(deque) > 1:
        if deque.pop() != deque.popleft():
            return False

    return True
