# fib.py
from functools import lru_cache
import time
import matplotlib.pyplot as plt

times = []


def main():
    fib(100)
    x = list(range(100))

    plt.plot(x, times)
    plt.title("Execution Time (sec) of Fibonacci Sequence VS Input Number")
    plt.xlabel("Input Number")
    plt.ylabel("Execution Time (sec)")
    plt.show()


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        times.append(end - start)
        print(f"Finished in {end - start}s: f({args[0]}) -> {result}")
        return result

    return wrapper


@lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    main()
