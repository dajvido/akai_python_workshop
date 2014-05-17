First-class functions

What is it?
A property of some programming languages

What does this property require?
enable using functions as variables, other function arguments, return values or storing them in data structures

```
my_int = int
isinstance(my_int("1"), int)


def convert(func, val):
    return func(val)
isinstance(convert(my_int, "1"), int)

def get_my_int():
    return my_int
isinstance(get_my_int()("1"), int)

funcs = [float, int, str]
for f in funcs:
    print(type(f("1")))

```


Task: create a function that returns a list of n-random numbers;
random number generator function should be an optional argument, if not passed we should use random module


```
import random

def rand_series(n, ....):
    numbers = []
    #TODO: implement

    return numbers

```

Anonymous functions, aka lambdas

```
(lambda x, y: x+y)(3,5)

my_int = lambda x: int(x)
my_int("123")


def sort_key(arg):
    return arg < 5:

arr = [1, 2, 5, 3, 10, 20]
sorted(arr, key=sort_key)

sorted(arr, key=lambda x: x < 5)

```

Task: using sorted and lambda as key, put the array into a random order

-hint: 


Higher-order functions usage

```
def passes_exams(course_grades):
    return all(map(lambda x: x>2, course_grades))
    

students = [
    {
        "name": "John",
        "grades": [5, 5, 2, 3],
    },
    {
        "name": "Andy",
        "grades": [3, 3, 4, 4, 3, 5],
    },
    {
        "name": "Anna",
        "grades": [2, 5, 4, 4, 5, 5, 6],
    },
]

graduates = map(lambda x: (x['name'], passes_exams(x['grades'])), students)
#print(list(graduates))

expelled = filter(lambda x: not x[1], graduates)
print(list(expelled))

```


Task: implement a Caesar cipher coder/decoder for text using map/ use filter remove all non-alphabet characters.

-Hint: on conversin to ascii and back ord / chr

