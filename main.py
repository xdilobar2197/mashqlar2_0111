
#1 - masala
sonlar = [22, 3, 6, 3, 99]

kvadratlar =list(map(lambda x: x ** 2, sonlar))
print(kvadratlar)

#2 - masala
sozlar =['salom', 'dunyo', 'kod', 'python']

katta_harif = list(map(lambda x: x.upper, sozlar))
print(katta_harif)

# 3 - masala
son = [1, 2, 3, 4, 5, 6]
uchga = list(filter(lambda x: x % 3 == 0, son))
print(uchga)
