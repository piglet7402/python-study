li = [1, '2', 3, '4', '5']

# for i in range(len(li)):
#     if isinstance(li[i], int) == True:
#         continue
#     else:
#         li[i] = int(li[i])
# print(li)

a = list(map(int, li))
print(a)