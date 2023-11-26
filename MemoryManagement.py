'''
Memory Management in Python

    Python memory allocation and deallocation method is automatic as the Python developers created a garbage collector for Python so that the user does not have to do manual garbage collection

    Python uses two strategies for memory allocation: 

        1. Reference counting
        2. Garbage collection

    Reference counting
        A reference count, or the number of references that point to an object, is a property of each object in the Python language. 
        When an object’s reference count reaches zero, it becomes un-referenceable and its memory can be freed up.

    Garbage collection is a process in which the interpreter frees up the memory when not in use to make it available for other objects.

    There are two parts of memory
        1. Stack Memory
        2. Heap Memory

    All the function calls and references stored in stack memory , 
    
    All the values of the objects are stored in the heap memory
    '''

x= 10

y = x

print(id(x))  #140735941495512
print(id(y))  #140735941495512 Here the x and y are referring to the same object'

a = 15

b = 15

print(id(a))  #140735941495672
print(id(b))  #140735941495672 Here the a and b are referring to the same object'

b = 16

print(id(a))  #140735941495672
print(id(b))  #140736603736984 Here the a and b are referring to the different object'