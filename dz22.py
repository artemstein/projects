import logging

logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w",
                    format="We have next logging message: %(asctime)s : %(levelname)s - %(message)s")

import time

def add_numbers(a, b):
    return a + b


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання функції {func.__name__}: {end_time - start_time} секунд")
        return result
    return wrapper

result = add_numbers(5, 10)
print(result)