# KINDLY GO THROUGH TEST FILE TO UNDERSTAND
from typing import List
import time
import gc
import sys

# Here in this code we will be leaking memory because we are creating cyclic reference.
# Find that we are indeed making cyclic references.
# Eventually memory will be released, but that is currently not happening immediately.
# We have added a function called "clear_memory" but it is not able to do it's job. Fix it.
# Refer to test_clear_memory Test in test_session2.py to see how we're crudely finding that
# this code is sub-optimal.
class Something(object):

    def __init__(self):
        super().__init__()
        self.something_new = None

    def __repr__(self):
        return 'Something : {0}'.format(str(id(self)))

    def __str__(self):
        return '<Something {0}>'.format(str(id(self)))

class SomethingNew(object):

    def __init__(self, i: int = 0, something: Something = None):
        super().__init__()
        self.i = i
        self.something = something

    def __repr__(self):
        return 'SomethingNew of index {0}: '.format(str(self.i), str(id(self)))

    def __str__(self):
        return '<SomethingNew[{0}] {1}>'.format(str(self.i), str(id(self)))

def add_something(collection: List[Something], i: int):
    something = Something()
    something.something_new = SomethingNew(i, something)
    collection.append(something)

def reserved_function():
    # to be used in future if required
    pass

def clear_memory(collection: List[Something]):
    # clear the list and its elements from memory
    collection.clear()
    gc.collect() # removes the objects still in memory due to cyclic references


def critical_function():
    collection = list()
    for i in range(1, 1024 * 128):
        add_something(collection, i)
    clear_memory(collection)


# Here we are suboptimally testing whether two strings are exactly same or not
# After that we are trying to see if we have a particular character in that string or not
# Currently the code is suboptimal. Write it in such a way that it takes 1/10 the current time

# DO NOT CHANGE THIS PROGRAM
def compare_strings_old(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    for i in range(n):
        if a == b:
            pass
    char_list = list(a)
    for i in range(n):
        if 'd' in char_list:
            pass

# YOU NEED TO CHANGE THIS PROGRAM
def compare_strings_new(n):
    # comparison is being done by interning the string
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)
    for i in range(n):
        if a is b:
            pass
        if 'd' in a:
            pass

# comparison is being done by interning the string
def compare_strings_new_interned(n):
    a = sys.intern('a long string that is not intered' * 200)
    b = sys.intern('a long string that is not intered' * 200)
    for i in range(n):
        if a is b:
            pass
        if 'd' in a:
            pass

# comparison is being done by interning the hashes of the string
def compare_strings_new_hash_interned(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    hash_a = sys.intern(str(hash(a)))
    hash_b = sys.intern(str(hash(b)))
    for i in range(n):
        if a is b:
            pass
        if 'd' in a:
            pass

# comparison is being done by hashing, turned out to be slightly faster than interning the string using sys.intern
def compare_strings_new_hash(n):
    a = 'a long string that is not intered' * 200
    b = 'a long string that is not intered' * 200
    hash_a = hash(a)
    hash_b = hash(b)
    for i in range(n):
        if a is b:
            pass
        if 'd' in a:
            pass

if __name__ == '__main__':
    loops = 25
    exper = 3
    n = 10000000

    for i in range(exper):
        for j in range(loops):
            compare_strings_new_interned(n)
            compare_strings_new_hash(n)
            compare_strings_new_hash_interned(n)
