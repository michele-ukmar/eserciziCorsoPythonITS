import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Tempo impiegato da {func.__name__}: {end_time - start_time} secondi")
        return result
    return wrapper

def test_function(x):
    total = 0
    for i in range(x):
        total += i
    return total

timer(test_function)(1000000)
