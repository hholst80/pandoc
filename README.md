pandoc codeblock filters
========================

This is an example of [Pandoc] filters and [loginteractive] for logging
interactive programs as if they where executed from a terminal.

## Octave

~~~ { .octave .interactive }
A = reshape(1:4,[2 2])
v = eig(A)
~~~

## Python

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
## Ruby

~~~ { .ruby .interactive }
def factorial(n)
return 1 if n <= 1
return n * factorial(n - 1)
end
factorial(20)
~~~

[Pandoc]: http://johnmacfarlane.net/pandoc/
[loginteractive]: https://github.com/hholst80/loginteractive
