# 2.1.12

# def gcd(a, b):
#     if a < b:
#         a, b = b, a
#
#     while b:
#         a %= b
#         a, b = b, a
#
#     return a
#
# def lcm(a, b):
#     return a / gcd(a, b) * b
#
# a = int(input())
# b = int(input())
#
# print(int(lcm(a, b)))

# # 2.2.4
# while True:
#     num = int(input())
#
#     if num < 10:
#         continue
#     elif num > 100:
#         break
#     else:
#         print(num)




# # 2.3.3
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
#
# incrementRow = 0
#
# for i in range(c, d + 1):
#     print("\t" + str(c + incrementRow), end = '')
#     incrementRow += 1
# print()
#
# increment = 0
# for i in range(a, b + 1):
#     print(str(i), end = '\t')
#     for j in range(c, d + 1):
#         print(str(j * i), end = '\t')
#     print()


# # 2.3.7
#
# # a, b = (int(i) for i in input().split())
# a = int(input())
# b = int(input())
#
# arithmeticMean = 0
# cnt = 0
#
# while True:
#     if a % 3 == 0:
#         break
#     if a % 3 != 0:
#         a += 1
#
# #range(from, to, step)
# for i in range(a, b + 1, 3):
#     arithmeticMean += i
#     cnt += 1
#
# print(arithmeticMean / cnt)



# # 2.4.3
#
# strGC = input()
#
# cntGC = strGC.upper().count("G")
# cntGC += strGC.upper().count("C")
#
# lengthOfGC = len(strGC)
#
# print(cntGC / lengthOfGC * 100)


# # 2.4.7
# # string[start:end:step]
#
# DNA = input()
# DNACoded = ''
# cnt = 1
# x = 1
#
# j = DNA[x:x+1]
# for i in DNA:
#     if i in j:
#         cnt += 1
#     else:
#         print(i, end='')
#         print(cnt, end='')
#         cnt = 1
#     x += 1
#     j = DNA[x:x+1]



# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
#
# for student in students:
#     print(student)



# # 2.5.8
#
# s = 0
#
# arr = [int(i) for i in input().split()]
#
# for a in arr:
#     s += a
#
# print(s)




# # 2.5.9

# arr = [int(i) for i in input().split()]
#
# if len(arr) == 1:
#     print(arr[0], end = ' ')
#
# if len(arr) == 2:
#     print(arr[1] + arr[1], end = ' ')
#     print(arr[0] + arr[0], end = ' ')
#
# if len(arr) > 2:
#     print(arr[1] + arr[-1], end = ' ')
#
# for i in range(len(arr)):
#     if i != 0 and i != len(arr) - 1:
#         print(str(arr[i - 1] + arr[i + 1]), end = ' ')
#
# if len(arr) > 2:
#     print(arr[-2] + arr[0], end = ' ')


# # 2.5.11

# arr = [int(i) for i in input().split()]
#
# arrTmp = []
#
# arr.sort()
#
# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j]:
#             arrTmp.append(arr[i])
#
# result = []
# for i in arrTmp:
#     if i not in result:
#         result.append(i)
#
# for i in result:
#     print(i, end = ' ')

# short solution
# a, c = [str(i) for i in input().split()], []
# for i in a:
#     if i not in c and a.count(i) > 1:
#         c.append(i)
#         print(i, end=' ')


        #2dimensional arrays. generation
        # a = [[0] * n for i in range(n)]
        # a = [[0 for j in range(n)] for i in range(n)]



# # 2.6.7
# sum = int(input())
#
# arr = [sum]
#
# sqrSum = 0
#
# while sum != 0:
#     integer = int(input())
#     sum += integer
#     arr.append(integer)
#
# for i in arr:
#     sqrSum += i ** 2
#
# print(sqrSum)



# # 2.6.8
# n = int(input())
# cnt = n
# flag = False
#
# for i in range(n):
#     for j in range(i + 1):
#         print(i + 1, end = ' ')
#         cnt -= 1
#         if cnt == 0:
#             flag = True
#             break
#     if flag:
#         break




# # 2.6.9
# lst = [int(i) for i in input().split()]
#
# x = int(input())
#
# for i in range(len(lst)):
#     if lst[i] == x:
#         print(i, end = ' ')
#
# if x not in lst:
#     print('Отсутствует')



# # 2.6.10
# rM = []
# m2 = []
#
# while True:
#     strInput = str(input())
#     if strInput == 'end':
#         break
#     else:
#         lst = [int(i) for i in strInput.split()]
#         rM.append(lst)
#
#         lst2 = [0 for j in range(len(lst))]
#         m2.append(lst2)
#
# # # for i in range(len(rM)):
# # #     for j in range(len(rM[i])):
# # #         print(rM[i][j], end=' ')
# # #     print()
# # #
# # # for i in range(len(m2)):
# # #     for j in range(len(m2[i])):
# # #         print(m2[i][j], end=' ')
# # #     print()
#
# lastJ = len(rM[0]) - 1
# lastI = len(rM) - 1
#
# # For a line
# if lastI == 0:
#     for j in range(len(rM[0])):
#
#         # First element
#         if j == 0 and lastJ != 0:
#             m2[0][j] = rM[0][j] + rM[0][j + 1] + rM[0][j] + rM[0][lastJ]
#
#         # Middle element
#         if j != 0 and lastJ != j:
#             m2[0][j] = rM[0][j] + rM[0][j + 1] + rM[0][j] + rM[0][j - 1]
#
#         # Last element
#         if j == lastJ and j != 0:
#             m2[0][j] = rM[0][j] + rM[0][0] + rM[0][j] + rM[0][j - 1]
#
# # For a column
# if lastJ == 0:
#     for i in range(len(rM)):
#
#         # First element
#         if i == 0 and lastI != 0:
#             m2[i][0] = rM[lastI][0] + rM[i][0] + rM[i + 1][0] + rM[i][0]
#
#         # Middle element
#         if i != 0 and lastI != i:
#             m2[i][0] = rM[i - 1][0] + rM[i][0] + rM[i + 1][0] + rM[i][0]
#
#         # Last element
#         if i == lastI and i != 0:
#             m2[i][0] = rM[i - 1][0] + rM[i][0] + rM[0][0] + rM[i][0]
#
#
# # For a matrix
# for i in range(len(rM)):
#     lastJ = len(rM[i]) - 1
#     lastI = len(rM) - 1
#     for j in range(len(rM[i])):
#         # For not end elements
#         if i != 0 and j != 0 and i != lastI and j != lastJ:
#             m2[i][j] = rM[i - 1][j] + rM[i][j + 1] + rM[i + 1][j] + rM[i][j - 1]
#
#         # For first element in first row
#         if i == 0 and j == 0 and 0 != lastI and 0 != lastJ:
#             m2[i][j] = rM[lastI][j] + rM[i][j + 1] + rM[i + 1][j] + rM[i][lastJ]
#
#         # For not first and not last element in first row
#         if i == 0 and j != 0 and j != lastJ and 0 != lastI:
#             m2[i][j] = rM[lastI][j] + rM[i][j + 1] + rM[i + 1][j] + rM[i][j - 1]
#
#         # For last element in first row
#         if i == 0 and j == lastJ and 0 != lastI and 0 != lastJ:
#             m2[i][j] = rM[lastI][j] + rM[i][0] + rM[i + 1][j] + rM[i][j - 1]
#
#         # For last elem in a middle line
#         if i != 0 and i != lastI and j == lastJ and j != 0:
#             m2[i][j] = rM[i - 1][j] + rM[i][0] + rM[i + 1][j] + rM[i][j - 1]
#
#         # For last elem in last line (right bottom corner)
#         if i == lastI and j == lastJ and i != 0 and j != 0:
#             m2[i][j] = rM[i - 1][j] + rM[i][0] + rM[0][j] + rM[i][j - 1]
#
#         # For last line middle column
#         if i == lastI and lastI != 0 and j != 0 and j != lastJ:
#             m2[i][j] = rM[i - 1][j] + rM[i][j + 1] + rM[0][j] + rM[i][j - 1]
#
#         # For first element in last line (left bottom corner)
#         if i == lastI and i != 0 and j == 0 and 0 != lastJ:
#             m2[i][j] = rM[i - 1][j] + rM[i][j + 1] + rM[0][j] + rM[i][lastJ]
#
#         # For element in first column and middle line
#         if i != 0 and i != lastI and j == 0 and 0 != lastJ:
#             m2[i][j] = rM[i - 1][j] + rM[i][j + 1] + rM[i + 1][j] + rM[i][lastJ]
#
#
# # For an element
# if lastJ == 0 and lastI == 0:
#     m2[0][0] = rM[0][0] * 4
#
# for i in range(len(m2)):
#     for j in range(len(m2[i])):
#         print(m2[i][j], end=' ')
#     print()

# # short solution
# c = []
# while True:
#     a = [i for i in input().split()]
#     if a == ['end']:
#         break
#     c.append(a)
# n, m = len(c), len(c[0])
# for i in range(n):
#     for j in range(m):
#         x = int(c[i][j-1]) + int(c[i][j+1-m]) + int(c[i-1][j]) + int(c[i+1-n][j])
#         print(x, end=' ')
#     print()


# 2.6.11
# todo






















