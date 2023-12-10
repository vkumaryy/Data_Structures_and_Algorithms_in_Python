"""
This code snippet demonstrates the usage of a stack data structure.

Example Usage:
    stack = []
    stack.append('a')
    stack.append('b')
    stack.append('c')
    print(stack)  # Output: ['a', 'b', 'c']
    print(stack.pop())  # Output: 'c'
    print(stack.pop())  # Output: 'b'
    print(stack.pop())  # Output: 'a'

Inputs: None

Outputs:
    - The output of the first print statement is `['a', 'b', 'c']`.
    - The output of the second print statement is 'c'.
    - The output of the third print statement is 'b'.
    - The output of the fourth print statement is 'a'.
"""

stack = []
stack.append('a')
stack.append('b')
stack.append('c')
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
