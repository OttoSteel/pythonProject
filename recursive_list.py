def flatten(iterable):
   result = []
   for x in iterable:
      if hasattr(x, '__iter__'):
         result.extend(flatten(x))
      else:
         result.append(x)
   return result
print(flatten([1, [2,3], [[2], 5], 6]))