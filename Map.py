# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_sqr = list(map(lambda x: x**2, numbers))
# list_cubic = list(map(lambda x: x**3, numbers))

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']
print(*sorted(list(filter(lambda x: len(x) == 4 or x.startswith('S'), days))), sep='\n')