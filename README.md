pandoc octave filter
====================

This is an example of [Pandoc] filters and [loginteractive].

Octave

~~~ { .octave .interactive }
A = rand(4,4)
v = eig(A)
~~~

Python

~~~ { .python .interactive }
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

isPrime(2)
isPrime(4)
for n in range(2,100):
    if isPrime(n):
        print n,
~~~

[Pandoc]: http://johnmacfarlane.net/pandoc/
[loginteractive]: https://github.com/hholst80/loginteractive
