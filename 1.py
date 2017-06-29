# Prime factorization
# I've only basic math background, so I was reinventing wheel
# It's usable for relatively big numbers (still really slow compared to calculatorsoup.com)

# time module is unnecessary to script function, it's added only to time measurement
import time

# my own version of range() which returns only numbers remainig after division by two and three
# saved 0.8 sec on factorization of 12345678901 (my own "benchmark" number, it's multiple of two primes 857, 14405693)
# so it's not so fast to find like something divisible by two/three on high power
# e.g. to determine prime factorization of: 12345678901 takes 1.743 seconds
#                                           34359738368 takes 0.001 second <- 2^35
def range3(number):
    step = 0
    a, b = 0, 2
    while b  < number:
        yield a+5
        yield b+5
        a, b = a + 6, b + 6

def factorization(number):
    lst = []

    # divisibility by two is out of main loop, because I can skip half of numbers latter
    while number % 2 == 0:
        number = number / 2
        lst.append(2)
        if number == 1:
            return lst

    # i found way to remove Multiples of three, so it's out of main loop to
    while number % 3 == 0:
        number = number / 3
        lst.append(3)
        if number == 1:
            return lst
    else:
        # was trying to find some elegant way to remove even more Multiples of low primes
        for i in range3(int(number)):
            while number % i == 0:
                number = number / i
                lst.append(i)
                if number == 1:
                    return lst

x = int(input('Number to factorize> '))
start = time.time()
print(factorization(x))
end = time.time()
print(end - start)
