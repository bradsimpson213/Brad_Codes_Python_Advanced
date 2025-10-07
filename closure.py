# A closure in programming is a function that return another function. The
# benefit is that the inner function “remembers” the variables from the
# scope in which it was created, even after that scope has  executed.

# In other words, when a function is defined inside another function, the inner
# function has access not only to its own local variables but also to the
# variables of the outer function — and it keeps that access even if the outer
# function is no longer active.

def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function



# closure = outer_function(10)  # returns inner_function, with x=10 "remembered"
# print(closure(5))  # 15
# print(closure(20)) # 30


# The outer_function returns inner_function. The inner_function keeps access to
# x, even though the outer_function has finished executing.  The combination of
# the function (inner_function) + its remembered environment (x=10) is the
# closure.


def counter(start=0):
    count = start

    def increase_count(val):
        nonlocal count
        count += val
        return count
    
    def decrease_count(val):
        nonlocal count
        count -= val
        return count
    
    return increase_count, decrease_count

count_up, count_down = counter(1)
print(count_up(2))
print(count_up(4))
print(count_down(4))
