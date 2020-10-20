a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

c = 'abcd'

rez = zip(a, b, c)

for t1, t2, t3 in zip(a, b, c):
    print(t1, t2, t3)

# Вернем все из Zip обратно в списки:

# print(list(rez))

col1, col2, col3 = zip(*rez)
print(*col1, *col2, *col3)