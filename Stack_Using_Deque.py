from collections import deque

def stack_example():
    """
    Demonstrates the usage of the `deque` class from the `collections` module to implement a stack.
    
    Example Usage:
    >>> stack_example()
    deque(['a', 'b', 'c'])
    c
    b
    a
    
    Inputs: None
    Outputs: None
    """
    mystack = deque()
    mystack.append('a')
    mystack.append('b')
    mystack.append('c')
    print(mystack)

    print(mystack.pop())
    print(mystack.pop())
    print(mystack.pop())

stack_example()
