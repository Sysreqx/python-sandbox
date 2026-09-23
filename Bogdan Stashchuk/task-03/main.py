# # 3.1.8
# def f(x):
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         return -x / 2
#     elif 2 < x:
#         return (x - 2) ** 2 + 1



# # # 3.1.9
# def modify_list(l):
#     l2 = []
#
#     for i in range(len(l)):
#         if l[i] % 2 != 0:
#             l2.append(l[i])
#
#     for i in l2:
#         l.remove(i)
#
#     for i in range(len(l)):
#         l[i] //= 2
#
#
# lst1 = [1, 2, 3, 4, 5, 6]
# print(modify_list(lst1))  # None
# print(lst1)               # [1, 2, 3]
# modify_list(lst1)
# print(lst1)               # [1]
#
# lst1 = [10, 5, 8, 3]
# modify_list(lst1)
# print(lst1)               # [5, 4]



#
# # 3.2.5
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] = [d[key], value]
#     elif key not in d:
#         if key * 2 in d:
#             d[key * 2] = [d[key * 2], value]
#         elif key * 2 is not d:
#             d[key * 2] = [value]
#
#
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2 * key in d:
#         d[2 * key] += [value]
#     else:
#         d[2 * key] = [value]
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}



# # 3.2.6
# test_str = input()
# s = test_str.lower()
#
# delim = " "
#
# arr = [str(i) for i in s.split(delim)]
#
# dctr = {ele: 0 for idx, ele in
#        enumerate(s.split(delim))}
#
# for key in dctr:
#     dctr[key] = arr.count(key)
#
# for key in dctr:
#     print(key, end=" ")
#     print(dctr[key])




# # 3.2.7
#
# huetenn = {}
# for _ in range(int(input())):
#     x = int(input())
#     if x not in huetenn:
#         huetenn[x] = f(x)
#     print(huetenn[x])

# 3.4.2
with open('tt.txt') as inf:
    for line in inf:
        line = line.strip()
        print(line)

arr = []

for i in line:
    if 97 <= ord(i) <= 122:
        arr.append(i)
        print(i)

print(arr)



