target = 1000
sum = 0
for i in range(3,target,3):
    sum += i
for i in range(5,target,5):
    sum += i
for i in range(15,target,15):
    sum -= i
print(sum)


# version 2
# sum = 0
# for i in range(target):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)