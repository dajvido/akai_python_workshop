MRO - Method Resolution Order

What is it?
set of rules that construct the linearization of class ancestors.

When does it take place?
when evaluating class definitions

What is the benefit?
enables multiple inheritance


```
class Fruit:
    def eat_it(self):
        return "Hmm.. strange taste"

class Mango(Fruit): pass

class Apple(Fruit):
    def eat_it(self):
        return "Yummy, an apple"

class PineApple(Apple): pass

for cls in [Fruit, Mango, Apple, PineApple]:
    print("{0} -> {1}".format(cls, cls().eat_it())) 
    
```

What happens if:

```
class PineApple(Apple, Mango): pass

```


You can check class MRO with the following way:

```
#python3 only
PineApple.__mro__

```


Now what would be MRO of class Z

```

O = object
class A(O): pass
class B(O): pass
class C(O): pass
class D(O): pass
class E(O): pass
class K1(A,B,C): pass
class K2(D,B,E): pass
class K3(D,A): pass
class Z(K1,K2,K3): pass

```

Python uses C3 algorithm to define MRO:

(whiteboard example)




Whats the MRO? 

```
O = object
class F(O): pass
class E(O): pass
class D(O): pass
class C(D,F): pass
class B(D,E): pass
class A(B,C): pass
```


References:

http://en.wikipedia.org/wiki/C3_linearization

https://www.python.org/download/releases/2.3/mro/
