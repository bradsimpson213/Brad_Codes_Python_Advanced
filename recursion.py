# Recursion is where a function calls itself, either
# directly or indirectly, to solve a problem. It involves breaking down a
# complex problem into smaller, similar sub-problems until a simple,
# non-recursive case (known as the base case) is reached.


foods = ['pizza', 'hamburger', 'salad', 'chicken tenders', 'apple pie']

def recursive_iterator(list_obj):
    print("I RAN", list_obj)

    if len(list_obj) == 0:
        return
    
    print(list_obj[0])

    return recursive_iterator(list_obj[1:])


# recursive_iterator(foods)



# Fibonacci Sequence
# 0 1 1 2 3 5 8 13 21 34 55 ...

def fibonacci_recursive(num):
    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci_recursive(num - 1) + fibonacci_recursive(num -2)
    
print(fibonacci_recursive(37))