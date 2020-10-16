from time import perf_counter
class Timer:
     def __init__(self, func):
         self.fn = func

     def __call__(self, *args, **kwargs):
         start = perf_counter()
         print(f'Function {self.fn.__name__} is calling')
         result = self.fn(*args, **kwargs)
         finish = perf_counter()
         print(f'Function worked {finish - start}')
         return result
@Timer
def fact(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total