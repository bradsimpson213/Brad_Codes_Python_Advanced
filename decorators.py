# DECORATORS

from datetime import datetime
from time import sleep


def timer(func):

    def inner():
        start = datetime.now()
        result = func()
        print(result)
        end = datetime.now()
        elapsed = end - start
        print("Elapsed time: ", elapsed)
        return elapsed
    
    return inner


@timer
def say_hi():
    sleep(.2)
    return "Hello there!"

@timer
def say_bye():
    sleep(.3)
    return "See you soon!"

# call_hello = timer(say_hi)
# print(call_hello())
# print(say_hi())
# print(say_bye())

@timer
def do_stuff():
    count = 0
    for val in range(100_000_000):
        count += 1

    return count

print(do_stuff())